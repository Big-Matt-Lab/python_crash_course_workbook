"""
Docstring for unconfirmed-users
"""
new_users = ['alice', 'brian', 'candace']
confirmed_users = []

def user_confirmation(unconfirmed_users):
    """
    Docstring for user_confirmation    
    :param unconfirmed_users: Description
    """
    print(unconfirmed_users)
    while unconfirmed_users:
        current_user = unconfirmed_users.pop(0)

        print(f"Verifying user: {current_user.title()}.")
        confirmed_users.append(current_user)
    print(unconfirmed_users)

def users(newly_confirmed_users):
    """
    Docstring for users
    :param confirmed_users: Description
    """
    print("\nThe following users have been confirmed:")
    for confirmed_user in newly_confirmed_users:
        print(confirmed_user.title())

user_confirmation(new_users[:])
users(confirmed_users)
print(new_users)
