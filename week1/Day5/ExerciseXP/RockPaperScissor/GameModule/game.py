import random


class Game:

    def __init__(self):
        self.user_win = 0
        self.computer_win = 0
        self.draw = 0

    def get_user_item(self):

        while True:

            user_ask = input("Select an item (rock/paper/scissors) : ").lower()

            if user_ask in ["rock", "paper", "scissors"]:
                return user_ask

            print("Invalid move! Please choose rock, paper, or scissors.")

    def get_computer_item(self):

        computer_actions_choice = ["rock", "paper", "scissors"]

        computer_item = random.choice(computer_actions_choice)

        return computer_item

    def get_game_result(self, user_item, computer_item):

        print(f"\nThe user chose {user_item} and the computer chose {computer_item}")

        # USER WINS
        if user_item == "paper" and computer_item == "rock":
            print("The user wins!")
            print("===============================")
            self.user_win += 1
            return "win"

        elif user_item == "rock" and computer_item == "scissors":
            print("The user wins!")
            print("===============================")
            self.user_win += 1
            return "win"

        elif user_item == "scissors" and computer_item == "paper":
            print("The user wins!")
            print("===============================")
            self.user_win += 1
            return "win"

        # DRAWS
        elif user_item == computer_item:
            print("It's a draw!")
            print("===============================")
            self.draw += 1
            return "draw"

        # COMPUTER WINS
        else:
            print("The computer wins!")
            print("===============================")
            self.computer_win += 1
            return "loss"

    def play(self):

        user_playing = self.get_user_item()

        computer_playing = self.get_computer_item()

        result = self.get_game_result(user_playing, computer_playing)

        return result