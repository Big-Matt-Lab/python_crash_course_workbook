"""
Reads a list of numbers from a JSON file and prints them.
"""
from pathlib import Path
import json

path = Path('numbers.json')

try:
    contents = path.read_text(encoding='utf-8')
    numbers = json.loads(contents)
except FileNotFoundError:
    print(f"Error: The file '{path}' was not found.")
    numbers = [] # Initialize to an empty list or handle as appropriate
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from '{path}'. The file might be corrupted or empty.")
    numbers = []

if numbers: # Only print if there are numbers to display
    print(numbers)
