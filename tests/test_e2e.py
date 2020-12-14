import os
from threading import Thread
from selenium import webdriver
import requests

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
    
def create_list(list_name):
    response = requests.post(
            url=f'{TRELLO_URL}/lists',
            params={
                'key': TRELLO_API_KEY,
                'token': TRELLO_TOKEN,
                'name': list_name,
                'idBoard': os.getenv("TRELLO_BOARD_ID"),
            }
        )
    return response.json()['id']

#@pytest.fixture(scope='module')
def test_app():
    
    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id
    
    create_list('ToDo')
    create_list('Done')

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