"""
Docstring for toppings
NOT conditional
"""
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # NOT conditional
    # since mushrooms are NOT anchovies, this evaluates as True
    print("Hold the anchovies!")

# Numercial comparisions >, <, >=, <=, etc
answer = 17
if answer != 42: # evals as True
    print("That is not correct.")
print() # readibilty space
requested_toppings = ['mushrooms', 'onions', 'peppers']
if 'pepperoni' in requested_toppings:
    print("Yes, we have mushrooms.")
else:
    print('sorry, we\'re out of that.')
#
