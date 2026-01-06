"""Dictionary looping"""
user_0 = {
    'username': 'enfermi',
    'first_name': 'enrico', # Renamed for clarity
    'last_name': 'fermi'    # Renamed for clarity
}


print("--- User Profile ---") # More descriptive separator
    
for key, value in user_0.items(): # Using 'key', 'value' for better readability
    print(f"\nKey: {key}")
    print(f"Value: {value}")