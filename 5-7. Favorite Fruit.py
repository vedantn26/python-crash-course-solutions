''': Make a list of your favorite fruits, and then write a
series of independent if statements that check for certain fruits in your list.
Make a list of your three favorite fruits and call it favorite_fruits.
Write five if statements. Each should check whether a certain kind of fruit is
in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas'''



#we will complete this using input method 

fruit = input('What fruit do you want?: ')
fruit = fruit.lower() #due to case sensitive

fruits_available = ['apple', 'mango', 'banana', 'pineapple', 'grapes', 'orange']

if fruit in fruits_available:
    print('This fruit is available!')

else:
    print('This fruit is not available.')





