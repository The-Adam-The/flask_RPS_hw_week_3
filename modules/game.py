
class Game:
    
    def decide_winner(player1, player2):

        if player1.move == player2.move:
            return None

        if player1.move == "rock":
            if player2.move == "paper":
                return f"{player2.name} wins"
            else:
                return f"{player1.name} wins"

        if player1.move == "paper":
            if player2.move == "scissors":
                return f"{player2.name} wins"
            else:
                return f"{player1.name} wins"

        if player1.move == "scissors":
            if player2.move == "rock":
                return f"{player2.name} wins"
            else:
                return f"{player1.name} wins"
        