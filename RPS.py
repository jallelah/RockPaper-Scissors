import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    
class Random(Player):
    def move(self):
        throw = random.choice(moves)
        return (throw)
        

class Reflect(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return Player.play(self)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = my_move

class Cycle(Player):
    cycle_move = 'rock'

    def move(self):
        return self.cycle_move

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.cycle_move = 'paper'
        elif my_move == 'paper':
            self.cycle_move = 'scissors'
        elif my_move == 'scissors':
            self.cycle_move = 'rock'


class Human(Player):
    def move(self):
        while True:
            self.user_input = input("Choose rock, paper, scissors?")
            if self.user_input in moves:
                break
        return self.user_input


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You: {move1}  Computer: {move2}")
        if move1 == move2:
            print('**** TIE ****')
        elif beats(move1, move2):
            print('**** YOU WIN!!! ****')
            self.p1_score += 1
        else:
            print('**** COMPUTER WIN ****')
            self.p2_score += 1
        print(f'Score: You {self.p1_score} , Computer {self.p2_score}')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def rounds(self):
        while True:
            try:
                self.user_input = int(input("Choose the number of rounds?"))
                break
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break
        return self.user_input

    def play_game(self):
        self.rounds = self.rounds()
        print("Game start!")
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        print("Thank you for playing")


if __name__ == '__main__':
    game = Game(Human(), Reflect())
    game.play_game()
