"""
This wasn't in lecture, but I considered adding it!
It runs 10,000 games of nimm where both players play randomly
It then counts how many games player 1 wins.
"""
import random
NUM_EXPERIMENTS = 10000
N_STONES = 20

def main():
	n_player_1_wins = 0
	for i in range(NUM_EXPERIMENTS):
		winner = simulate_random_nimm()
		if winner == 1:
			n_player_1_wins += 1
	print(n_player_1_wins)

def simulate_random_nimm():
	stones = N_STONES
	turn = 1
	while stones > 0:
		take = random.randint(1, 2)
		stones -= take
		if turn == 1:
			turn = 2
		else:
			turn = 1
	return turn

if __name__ == "__main__":
    main()
