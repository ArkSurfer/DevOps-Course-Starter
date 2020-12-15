import os
import datetime

class TrelloItem:
	# def __init__(self, id, list_id, title, last_modified):
	# 	self.id = id
	# 	self.title = title
	# 	self.last_modified = datetime.datetime.strptime(last_modified, '%Y-%m-%dT%H:%M:%S.%fZ')

	# 	if list_id == os.environ["TODO_LIST_ID"]:
	# 		self.status = "To Do" 
	# 	else:
	# 		self.status = "Done"	

	def __init__(self, id, status: str, title, last_modified):
		self.id = id
		self.title = title
		self.last_modified = last_modified
		self.status = status

	@classmethod
	def from_raw_trello_card(cls, card):
		last_modified = datetime.datetime.strptime(card["dateLastActivity"], '%Y-%m-%dT%H:%M:%S.%fZ')

		status = ""
		if card["idList"] == os.environ["TODO_LIST_ID"]:
			status = "To Do" 
		else:
			status = "Done"	

		return cls(card["id"], status, card["name"], last_modified)