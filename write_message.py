"""
Writes a simple message to a text file.
"""
from pathlib import Path

path = Path('programming.txt') # Changed filename to a more conventional .txt extension
path.write_text('I love programming', encoding='utf-8')
