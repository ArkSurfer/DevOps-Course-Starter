from item import TrelloItem
from viewmodel import ViewModel
from datetime import date

def test_items_by_status():
    items = [
        TrelloItem(1,'To Do','Task 1','2020-12-10T17:48:14.363Z'),
        TrelloItem(2,'Done','Task 2','2020-12-10T17:48:14.363Z')
    ]

    view_model = ViewModel(items)
    print(view_model.todo_items)
    assert view_model.todo_items == [item for item in items if item.status == 'To Do']
    assert view_model.done_items == [item for item in items if item.status == 'Done']