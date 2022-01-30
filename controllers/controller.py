from flask import render_template, request
from app import app
from modules.player_list import player_list, player1, player2
from modules.player import Player
from modules.game import Game
import random


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/play', methods=['GET', 'POST'])
def game_start():
    player1.name = request.form["player1_name"].capitalize()
    print(player1.name)
    player2.name = random.choice(player_list)
    return render_template('game.html', player1=player1, player2=player2)

@app.route('/result', methods=['GET', 'POST'])
def play_game():
    player1.move = request.form["move"]
    player2.move = random.choice(["rock", "paper", "scissors"])
    game = Game(player1, player2)
    outcome = game.decide_winner()
    return render_template('game_result.html', player1=player1, player2=player2, outcome=outcome)

