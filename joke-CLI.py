import requests
import time
import random
import sys

category = ["Any","Programming","Pun","Spooky","Dark","Misc"]

Range = 3,4,5,6,7,8,9

while True:

	try:
		print("*" * 30)
		print("which type of joke you want:"
		      "\nAny : 0"
		      "\nProgramming : 1"
		      "\nPun : 2"
		      "\nSpooky : 3"
		      "\nDark : 4"
		      "\nMisc : 5"
		      "\nQuit : q")

		user_input = input(
			"type any number from above as per the type of joke you want (or q to quit): "
		).strip().lower()

		if user_input in ("q", "quit", "exit"):
			print("\nExiting joke app.")
			break

		user = int(user_input)

		if not 0 <= user < len(category):
			print("Invalid choice. Try again.")
			continue

		print("*" * 30)
		print("Loading joke", end="")
		
		for _ in range(random.choice(Range)):
			time.sleep(0.5)
			print(".", end="")
			sys.stdout.flush()

		url = f"https://v2.jokeapi.dev/joke/{category[user]}?type=single"

		response = requests.get(url)

		if response.status_code == 200:
			data = response.json()
			print("\nJoke:", data.get("joke", "No joke found."))
		else:
			print("\nSorry, we can't reach the API.")
		print("*" * 30)
	except ValueError:
		print("\nPlease enter numbers only.")
	except Exception as e:
		print(f"\nUnexpected error: {e}")