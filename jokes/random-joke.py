#! /usr/bin/env python3
"""
This script will print a random joke from the index.json file that has the following structure.

[
  {
    "type": "general",
    "setup": "What did the fish say when it hit the wall?",
    "punchline": "Dam."
  }
]
"""
import json
import random

def get_random_joke():
    with open("random-joke.json", "r") as file:
        jokes = json.load(file)
        return jokes[random.randint(0, len(jokes) - 1)]
    
if __name__ == "__main__":
    joke = get_random_joke()
    print(f"{joke['setup']}\n\n{joke['punchline']}")
