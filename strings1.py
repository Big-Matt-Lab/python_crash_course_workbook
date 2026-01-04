"""
Docstring for String exercises
PCC pg 25 exercises
"""
name = 'Matt'
print(f"Hello, {name}. Would you like to learn about strings today?")
print(name.lower())
print(name.upper())
print(name.title())
#
print("Give me liberty or give me death!  Patrick Henry.")
#
quote = "Give me liberty or give me death!"
famous_speaker = "Patrick Henry"
message = f"{quote}  {famous_speaker}."
print(message)
#
long_name = "   Eileen   "
print(long_name)
print(long_name.lstrip())
print(long_name.rstrip())
print(long_name.strip())
#
filename = "python_notes.txt"
print(filename.removesuffix('.txt'))

#EOF
