from flask import render_template, request
from app import app
from modules.player_list import player_list



@app.route('/home')
def index():
    return render_template('index.html', player_list=player_list)


@app.route('/<player>')
def game_start(player):
    return render_template('game.html', player=player)

@app.route('/game', methods=['POST'])
def play_game(player):
    move = request.form["move"]
    
   
    return render_template('game.html', player=player, move=move)


