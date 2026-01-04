"""
COntinued dictionary manipulations
"""
# alternate layouts and extended lists
poll_invitees = ['mary', 'lisa', 'jen', 'john', 'edward', 'mike', 'sarah']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language}.")

for language in set(favorite_languages.values()):
    print(language.title())

for invitee in poll_invitees:
    if invitee in favorite_languages:
        print(f"Thanks {invitee.title()} for completing the poll.")
    else:
        print(f"{invitee.title()} please complete and return the poll.")