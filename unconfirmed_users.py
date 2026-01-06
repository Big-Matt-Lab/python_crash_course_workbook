"""
Manages user confirmation by moving users from an unconfirmed list to a confirmed list.
"""
from collections import deque # For more efficient left-side popping

new_users = ['alice', 'brian', 'candace']
confirmed_users = []

def user_confirmation(unconfirmed_users_queue: deque):
    """
    Verifies users from a queue of unconfirmed users and adds them to a global confirmed list.
    
    Args:
        unconfirmed_users_queue (deque): A deque containing unconfirmed usernames.
    """
    # print(unconfirmed_users_queue) # Debugging print, can be removed
    while unconfirmed_users_queue:
        current_user = unconfirmed_users_queue.popleft() # Use popleft for O(1) efficiency
        print(f"Verifying user: {current_user.title()}.")
        confirmed_users.append(current_user)
    # print(unconfirmed_users_queue) # Debugging print, can be removed

def display_confirmed_users(confirmed_list: list):
    """
    Displays the list of confirmed users.
    
    Args:
        confirmed_list (list): A list of confirmed usernames.
    """
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_list:
        print(confirmed_user.title())

if __name__ == "__main__":
    # Create a deque from a copy of new_users for efficient processing
    unconfirmed_queue = deque(new_users[:])
    
    user_confirmation(unconfirmed_queue)
    display_confirmed_users(confirmed_users)
    
    # The original new_users list remains unchanged due to slicing
    print(f"\nOriginal unconfirmed users list: {new_users}")
    print(f"Confirmed users list: {confirmed_users}")
    print(f"Remaining unconfirmed users in queue: {list(unconfirmed_queue)}") # Should be empty
