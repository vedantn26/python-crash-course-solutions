'''Use the third argument of the range() function to make
a list of the odd numbers from 1 to 20. Use a for loop to print each number'''


odd_numbers = []

for num in range(1, 21, 2):
    odd_numbers.append(num)

for num in odd_numbers:
    print(num)    
