''' Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do
the following:
Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas.
Prove that you have two separate lists. Print the message My favorite pizzas
are:, and then use a for loop to print the first list. Print the message My
friend's favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.
'''

my_pizza = ['paneer', 'tomato', 'sweet corn',]

friend_pizza = my_pizza[:]

my_pizza.append('extra cheese')

friend_pizza.append('italian')

print("My pizza: ", my_pizza)

print("friend's pizza: ", friend_pizza)

#proved that both lists are not same
