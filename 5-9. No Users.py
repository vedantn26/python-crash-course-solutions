'''Add an if test to hello_admin.py to make sure the list of
users is not empty.
If the list is empty, print the message We need to find some users!
Remove all of the usernames from your list, and make sure the correct
message is printed.
'''

# List of usernames
usernames = ['admin', 'Jaden', 'Emma', 'Alex', 'Sophia']

# Check if the list of users is empty
if not usernames:
    print("We need to find some users!")
else:
    # Loop through the list and print greetings
    for username in usernames:
        if username.lower() == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")

# Remove all usernames from the list
usernames.clear()

# Check if the list of users is empty again
if not usernames:
    print("We need to find some users!")
