from flask import Flask, render_template, request, redirect, url_for
from item import TrelloItem
from trello import TrelloClient
from viewmodel import ViewModel
import os

client = TrelloClient(
        os.getenv('API_KEY'),
        os.getenv('TOKEN')
    )

    
def get_items(client):   
        items = []
        trello_cards = client.get_all_cards_for_board(os.getenv('BOARD_ID'))
        for card in trello_cards:
            items.append(TrelloItem(card["id"], card["idList"], card["name"], card["dateLastActivity"]))
        return items


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')

    @app.route('/')
    def index():   
        items = []
        trello_cards = client.get_all_cards_for_board(os.getenv('BOARD_ID'))
        for card in trello_cards:
            items.append(TrelloItem(card["id"], card["idList"], card["name"], card["dateLastActivity"]))
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/', methods=['POST'])
    def add_todo_card():
        new_card = request.form.get('todoitem')
        add_card = client.add_card_to_list(os.getenv('TODO_LIST_ID'),new_card)
        return redirect(url_for('index'))

    @app.route('/items/<id>/complete')
    def complete_item(id):

        client.move_card_to_done(id)
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    create_app().run()