"""
Docstring for motorcycles
list manipulations
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'# replace honda with ducati
print(motorcycles)

motorcycles[0] = 'honda' # replace ducati with honda
motorcycles.append('ducati') # append ducati to list
print(motorcycles)

motorcycles = [] # empty list
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati') # insertion by index
print(motorcycles)

# Removing list elements
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# using pop method
# restore list
motorcycles.insert(1, 'yamaha')
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# using 'remove' to remove an item from a list when the index isn't known
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(2, 'suzuki')
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)



