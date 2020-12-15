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

def test_to_do_items_returns_items_in_done_column(view_model):
    assert len(view_model.done_items) == 1
    assert view_model.done_items[0].title == 'Task 2'


@pytest.fixture
def to_do_item():
    return TrelloItem('to-do-id', 'To Do','Task 1',datetime.now())

@pytest.fixture
def done_item():
    return TrelloItem('done-id', 'Done', 'Task 2',datetime.now())


def test_show_done_items_if_less_than_5(to_do_item, done_item):
    view_model = ViewModel(
        [
            done_item,
            done_item,
            done_item,
            done_item
        ]
    )
    assert view_model.show_all_done_items


def test_show_done_items_is_5_or_more(to_do_item, done_item):
    view_model = ViewModel(
        [
            done_item,
            done_item,
            done_item,
            done_item,
            done_item
        ]
    )
    assert not view_model.show_all_done_items