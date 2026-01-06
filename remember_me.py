"""
Small routine to save or recognize user names
"""
from pathlib import Path
import json

def greet_user():
    """
    Greets a user by name. If a username is stored in 'username.json',
    it welcomes the user back. Otherwise, it prompts for a name and stores it.
    
    Args:
        None
    Returns:
        None
    """
    
    path = Path('username.json')
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        print(f"Welcome back, {username}.")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents, encoding='utf-8')
        print(f"We'll remember you when you come back, {username}")

if __name__ == "__main__":
    greet_user()

# eof