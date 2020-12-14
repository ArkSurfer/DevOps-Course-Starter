from item import TrelloItem
from datetime import date

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        return [item for item in self.items if item.status == "To Do"]

    @property
    def done_items(self):
        return [item for item in self.items if item.status == "Done"]
            
    @property
    def show_all_done_items(self):
        return len(self.done_items) <= 4

    @property
    def recent_done_items(self):
        return [item for item in self.done_items if item.last_modified.date() == date.today()]

    @property
    def older_done_items(self):
        return [item for item in self.done_items if not item.last_modified.date() == date.today()]