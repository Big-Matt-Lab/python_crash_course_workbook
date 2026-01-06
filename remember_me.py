"""
Small routine to save or recognize user names
"""
from pathlib import Path
import json


def get_stored_user_info(path: Path) -> dict | None:
    """
    Retrieve stored user information (a dictionary) from a JSON file.
    Handles cases where the file doesn't exist or contains invalid JSON.
    If the file contains an old string-based username, it will be treated as not found.
    
    Args:
        path (Path): The path object to the JSON file where user info is stored.
        
    Returns:
        dict | None: A dictionary containing user information if found and valid,
                     otherwise None.
    """
    try:
        contents = path.read_text(encoding='utf-8')
        loaded_data = json.loads(contents)
        # Validate that the loaded data is a dictionary and contains a 'username' key
        if isinstance(loaded_data, dict) and "username" in loaded_data:
            return loaded_data
        else:
            # If it's not the expected dictionary format (e.g., old string format),
            # treat as if not found and prompt for new info.
            print(f"Warning: Stored user data in '{path}' is not in the expected dictionary format. Re-prompting.")
            return None
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        # Handles cases where the file exists but is empty or contains malformed JSON
        print(f"Warning: Could not decode JSON from '{path}'. File might be corrupted or empty. Re-prompting.")
        return None

def get_new_user_info(path: Path) -> dict:
    """
    Prompts the user for new information (username, age, favorite food)
    and stores it in a JSON file.
    
    Args:
        path (Path): The path object to the JSON file where user info will be stored.
        
    Returns:
        dict: A dictionary containing the newly entered user information.
    """
    username = input("What is your name?: ")
    user_age = input("What is your age?: ")
    user_favorite_food = input("What is your favorite food?: ")

    user_info = {
        "username": username,
        "age": user_age,
        "favorite_food": user_favorite_food
    }

    try:
        contents = json.dumps(user_info, indent=4) # Added indent for readability
        path.write_text(contents, encoding='utf-8')
        print(f"We'll remember you when you come back, {username}!")
    except IOError as e:
        print(f"Error: Could not save user information to '{path}'. {e}")

    return user_info

def greet_user():
    """
    Greets a user by name. If user information is stored, it offers to
    welcome them back or prompt for new information if it's not them.
    Otherwise, it prompts for new user information.
    
    """
    path = Path('username.json')
    user_info = get_stored_user_info(path)
    if user_info:
        username = user_info["username"]
        # Add a confirmation step
        confirmation = input(f"Is this you, {username}? (y/n): ").lower().strip()
        if confirmation == 'y':
            print(f"Welcome back, {username}!")
            # Display additional info
            print(f"Your age: {user_info.get('age', 'Not provided')}")
            print(f"Your favorite food: {user_info.get('favorite_food', 'Not provided')}")
        else:
            print("No problem, let's get your new information.")
            user_info = get_new_user_info(path)
            # get_new_user_info already prints a welcome message
    else:
        user_info = get_new_user_info(path)
        # get_new_user_info already prints a welcome message

if __name__ == "__main__":
    greet_user()

# eof
