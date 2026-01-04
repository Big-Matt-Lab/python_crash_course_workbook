"""Dog class creation"""
import time
class Dog:
    """An intro to classes starting with modeling a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(f"\n{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"\n{self.name} rolled over!")
# End of class Dog

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

my_dog.sit()
time.sleep(2)
my_dog.roll_over()
your_dog.sit()
