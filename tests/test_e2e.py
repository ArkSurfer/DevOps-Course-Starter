from threading import Thread
from selenium import webdriver
from dotenv import load_dotenv
import os
import requests
import pytest

load_dotenv()
TRELLO_URL = 'https://api.trello.com/1'
TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')


def create_trello_board():
    response = requests.post(
        url=f'{TRELLO_URL}/boards',
        params={
            'key': TRELLO_API_KEY,
            'token': TRELLO_TOKEN,
            'name': 'Selenium Test Board'
        }
    )
    return response.json()['id']


def delete_trello_board(board_id):
    requests.delete(
        url=f'{TRELLO_URL}/boards/{board_id}',
        params={
            'key': TRELLO_API_KEY,
            'token': TRELLO_TOKEN,
        }
    )
    
@pytest.fixture(scope='module')
def test_app():


    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id

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

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    
    assert driver.title == 'To-Do App'