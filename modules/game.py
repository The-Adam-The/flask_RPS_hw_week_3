
class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def decide_winner(self):

        if self.player1.move == self.player2.move:
            return None

        if self.player1.move == "rock":
            if self.player2.move == "paper":
                return f"Paper beats rock! {self.player2.name} wins!"
            else:
                return f"Rock beats Scissors! {self.player1.name} wins!"

        if self.player1.move == "paper":
            if self.player2.move == "scissors":
                return f"Scissors beat rock! {self.player2.name} wins!"
            else:
                return f"Paper beats rock! {self.player1.name} wins!"

        if self.player1.move == "scissors":
            if self.player2.move == "rock":
                return f"Rock beats scissors! {self.player2.name} wins!"
            else:
                return f"Scissors beat paper! {self.player1.name} wins!"
        