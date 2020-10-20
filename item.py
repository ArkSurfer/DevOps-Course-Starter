import os

class TrelloItem:
	def __init__(self, id, list_id, title):
		self.id = id
		self.title = title

		if list_id == os.environ["TODO_LIST_ID"]:
			self.status = "To Do" 
		else:
			self.status = "Done"	