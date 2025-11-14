"""Simple interactive Rock-Paper-Scissors game.

Run the script and follow on-screen prompts. You can enter full names
('rock', 'paper', 'scissors') or their first letters ('r', 'p', 's').
Type 'q' or 'quit' to stop when playing indefinitely.
"""

import random
import sys

CHOICES = ("rock", "paper", "scissors")


def normalize_choice(raw: str) -> str | None:
	if not raw:
		return None
	s = raw.strip().lower()
	if s in CHOICES:
		return s
	if s in ("r", "p", "s"):
		return {"r": "rock", "p": "paper", "s": "scissors"}[s]
	if s in ("q", "quit", "exit"):
		return "quit"
	return None


def decide_winner(user: str, comp: str) -> str:
	# returns 'user', 'comp', or 'tie'
	if user == comp:
		return "tie"
	wins = {
		"rock": "scissors",
		"scissors": "paper",
		"paper": "rock",
	}
	return "user" if wins[user] == comp else "comp"


def prompt_user_choice() -> str | None:
	raw = input("Your move (rock/paper/scissors or r/p/s). Type 'q' to quit: ")
	return normalize_choice(raw)


def main():
	print("Welcome to Rock - Paper - Scissors!")
	print("You can type rock/paper/scissors or r/p/s. Type 'q' to quit.")

	# Ask for a fixed number of rounds or indefinite play
	rounds = None
	try:
		raw_rounds = input("Enter number of rounds to play (odd number recommended) or press Enter to play until you quit: ").strip()
		if raw_rounds:
			rounds = int(raw_rounds)
			if rounds <= 0:
				print("Number of rounds must be positive. Playing until quit instead.")
				rounds = None
	except ValueError:
		print("Invalid number, playing until you quit.")

	user_score = 0
	comp_score = 0
	ties = 0
	round_no = 0

	try:
		while True:
			if rounds is not None and round_no >= rounds:
				break
			round_no += 1
			print(f"\nRound {round_no}")
			user = prompt_user_choice()
			if user is None:
				print("I didn't understand that — please enter rock, paper, scissors, or q to quit.")
				round_no -= 1
				continue
			if user == "quit":
				print("Quitting early.")
				break

			comp = random.choice(CHOICES)
			print(f"Computer chose: {comp}")

			winner = decide_winner(user, comp)
			if winner == "tie":
				print("It's a tie!")
				ties += 1
			elif winner == "user":
				print("You win this round!")
				user_score += 1
			else:
				print("Computer wins this round.")
				comp_score += 1

			print(f"Score -> You: {user_score}  Computer: {comp_score}  Ties: {ties}")

			# If playing a fixed number of rounds, continue until done
			if rounds is None:
				# indefinite mode: continue until user quits
				continue

		# summary
		print("\nGame over.")
		print(f"Rounds played: {round_no}")
		print(f"Final score -> You: {user_score}  Computer: {comp_score}  Ties: {ties}")
		if user_score > comp_score:
			print("Overall result: You win!")
		elif comp_score > user_score:
			print("Overall result: Computer wins.")
		else:
			print("Overall result: It's a draw.")

	except KeyboardInterrupt:
		print("\nInterrupted. Showing current score:")
		print(f"You: {user_score}  Computer: {comp_score}  Ties: {ties}")


if __name__ == "__main__":
	main()


