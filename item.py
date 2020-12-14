import os
import datetime

class TrelloItem:
	def __init__(self, id, list_id, title, last_modified):
		self.id = id
		self.title = title
		self.last_modified = datetime.datetime.strptime(last_modified, '%Y-%m-%dT%H:%M:%S.%fZ')

		if list_id == os.environ["TODO_LIST_ID"]:
			self.status = "To Do" 
		else:
			self.status = "Done"	