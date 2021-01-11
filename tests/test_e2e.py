from threading import Thread
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.common.keys import Keys
from trello import TrelloClient
import os
import requests
import pytest
import app

TRELLO_URL = "https://api.trello.com/1"

def create_trello_board():
    response = requests.post(
        url=f'{TRELLO_URL}/boards',
        params={
            'key': os.getenv("API_KEY"),
            'token': os.getenv("TOKEN"),
            'name': 'Selenium Test Board',
        }
    )
    return response.json()['id']

def delete_trello_board(board_id):
    requests.delete(
        url=f'{TRELLO_URL}/boards/{board_id}',
        params={
            'key': os.getenv("API_KEY"),
            'token': os.getenv("TOKEN"),
        }
    )
    
@pytest.fixture(scope='module')
def test_app():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['BOARD_ID'] = board_id
    board_list = TrelloClient(os.getenv("API_KEY"),os.getenv("TOKEN")).get_board_lists(board_id)

    os.environ['TODO_LIST_ID'] = board_list[0]['id']

    # construct the new application
    application = app.create_app()
    
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    
    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)

@pytest.fixture(scope='module')
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
        yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

    new_input = driver.find_element_by_name("todoitem")
    new_input.send_keys("Module Test")
    new_input.send_keys(Keys.RETURN)

    assert find_task_in_section('todo-section', driver) is not None

def find_task_in_section(section_name, driver):
    section = driver.find_element_by_xpath(f"//*[@data-test-id='{section_name}']")
    tasks = section.find_elements_by_xpath("//*[@data-test-class='task']")
    return next(task for task in tasks if task.find_element_by_xpath("//*[contains(text(), 'Module Test')]") is not None)