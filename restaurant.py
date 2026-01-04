""" More work with classes"""
class Restaurant:
    """
    Defining a group of restaurants
    """
    def __init__(self, name, cuisine_type,):
        """
        Docstring for __init__
        
        :param self: Description
        :param name: Description
        :param cuisine_type: Description
        """
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """
        Docstring for describe_restaurant
        
        :param self: Description
        """
        print(f"{self.name} restaurant is a family friendly establishment serving "
              f"{self.cuisine_type} with a kid-friendly menu and crowd.")
    
    def open_restaurant(self):
        """
        Docstring for open_restaurant
        
        :param self: Description
        """
        print(f"{self.name} is now open!")
    
    def customers_served(self):
        """
        Docstring for set_number_served
        
        :param self: Description
        """
        print(f"{self.name} has served over {self.number_served} customers!")

class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream', flavors= ['Rocky Road', 'Mint Chocolate Chip', 'Pistachio']):
        """Initialize attributes of the parent class."""
        super().__init__(name, cuisine_type)
        self.flavors = flavors if flavors else ['Rocky Road', 'Mint Chocolate Chip', 'Pistachio']
    
    def display_flavors(self):
        """Display the flavors available."""
        print(f"\n{self.name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
        



ice_cream_stand = Restaurant('Freeze', 'frozen treats')
restaurant_one = Restaurant("Luigi's", 'Italian')
restaurant_one.number_served = 12500
restaurant_two = Restaurant("Burger Heaven", 'American')
restaurant_three = Restaurant("Xenos", 'Greek')
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()
print()
restaurant_three.describe_restaurant()
restaurant_one.customers_served()
ice_cream_stand.describe_restaurant()
ice_cream_stand =IceCreamStand('Freeze', 'frozen treats')
ice_cream_stand.display_flavors()
