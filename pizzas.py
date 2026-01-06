""" Saving a module"""
def make_pizza(*toppings):
    """
    Docstring for make_pizza
    Prepares a pizza with the specified toppings.
    
    Args:
        *toppings (str): A variable number of topping ingredients.
    """
    print("Preparing a pizza with:")
    for topping in toppings:
        print(f"    {topping}")

# End of module
