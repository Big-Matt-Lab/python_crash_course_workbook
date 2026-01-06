"""
Writes a list of numbers to a JSON file.
"""
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers, indent=4) # Added indent for readability in JSON file
path.write_text(contents, encoding='utf-8')
