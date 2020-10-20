from flask import Flask, render_template, request, redirect, url_for
from item import TrelloItem
from trello import TrelloClient
import os

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

    client.move_card_to_done(id)
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run()