import requests

class TrelloClient: 
    def __init__(self, key, token):
        self.key = key
        self.token = token

    def get_auth_params(self):
        return {"key": self.key, "token": self.token}

    def get_all_cards_for_board(self, board_id):
        response = requests.get(f"https://api.trello.com/1/boards/{board_id}/cards", params=self.get_auth_params())
        response_json = response.json()
        return response_json

    def add_card_to_list (self, list_id, card_name):
        response = requests.post(f"https://api.trello.com/1/cards/{list_id}/{card_name}", params=self.get_auth_params())