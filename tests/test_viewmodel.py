import pytest
import os

from item import TrelloItem
from viewmodel import ViewModel
from datetime import datetime


@pytest.fixture
def view_model():
    return ViewModel(
        [
            TrelloItem('to-do-id','To Do','Task 1',datetime.now()),
            TrelloItem('done-id','Done','Task 2',datetime.now())
        ]
    )

def test_to_do_items_returns_items_in_to_do_column(view_model):
    assert len(view_model.todo_items) == 1
    assert view_model.todo_items[0].title == 'Task 1'