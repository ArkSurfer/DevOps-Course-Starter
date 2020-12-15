from dotenv import load_dotenv, find_dotenv
from unittest.mock import patch, Mock
from datetime import datetime
import pytest
import app
import os

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_get_requests.side_effect = mock_get_lists

    response = client.get('/')
    response_html = response.data.decode()

def mock_get_lists(url, params):
    if url == f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/cards':
        response = Mock(ok=True)
        response.json.return_value = get_sample_trello_cards_response()
        return response

    return None

def get_sample_trello_cards_response() {
    return  [
        {
            "id": "1",
            "name" : "Task 1",
            "idList" : os.getenv("TODO_LIST_ID"),
            "dateLastActivity" : datetime.today()
        }
    ]
}