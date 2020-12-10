import os

class TrelloItem:
	def __init__(self, id, list_id, title, last_modified):
		self.id = id
		self.title = title
		self.last_modified = last_modified

		if list_id == os.environ["TODO_LIST_ID"]:
			self.status = "To Do" 
		else:
			self.status = "Done"	