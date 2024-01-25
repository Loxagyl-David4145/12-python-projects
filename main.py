
import random

def play():
    user = input("'R' for rock, 'P' for paper, 'S' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'


def is_win(player, opponent):
        if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
            return True

print(play())