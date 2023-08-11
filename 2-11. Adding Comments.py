'''Choose two of the programs you've written, and
add at least one comment to each. If you don't have anything specific to
write because your programs are too simple at this point, just add your
name and the current date at the top of each program file. Then write one
sentence describing what the program does.'''

# Author: codingGPT
# Date: 2023-08-01
# Description: This program converts temperature from Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    """
    Function to convert temperature from Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    """
    return (celsius * 9/5) + 32

# Test the function
temperature_celsius = 25
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius} degrees Celsius is equal to {temperature_fahrenheit:.2f} degrees Fahrenheit.")
