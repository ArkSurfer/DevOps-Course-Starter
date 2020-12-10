import pytest
from dotenv import load_dotenv, find_dotenv
import app
from unittest.mock import patch, Mock

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

@patch('app.get_items')
def test_index_page(get_items, client):
    #get_items.side_effect = mock_get_items