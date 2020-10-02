from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from item import TrelloItem
from trello import TrelloClient
import session_items as session
import os
import requests
import json

app = Flask(__name__)
app.config.from_object('flask_config.Config')

client = TrelloClient(
    os.getenv('API_KEY'),
    os.getenv('TOKEN')
)

@app.route('/')
def index():   
    items = []
    trello_cards = client.get_all_cards_for_board(os.getenv('BOARD_ID'))
    for card in trello_cards:
        items.append(TrelloItem(card["id"], card["idList"], card["name"]))
    return render_template('index.html', items = items)

@app.route('/', methods=['POST'])
def add_todo_card():
     new_card = request.form.get('todoitem')
     add_card = client.add_card_to_list(os.getenv('TODO_LIST_ID'),new_card)
     return redirect(url_for('index'))

@app.route('/items/<id>/complete')
def complete_item(id):
    return redirect(url_for('index'))
#     board_lists = board.list_lists()
#     todo_list = next((x for x in board_lists if x.name == "Things To Do"), None)
#     done_list = next((x for x in board_lists if x.name == "Done"), None)

#     cards = todo_list.list_cards()
#     card = next((x for x in cards if x.id == id), None)   
#     card.change_list(done_list.id)  
      

if __name__ == '__main__':
    app.run()