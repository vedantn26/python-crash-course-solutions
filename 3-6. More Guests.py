'''You just found a bigger dinner table, so now more space
is available. Think of three more guests to invite to dinner.
Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.'''

guests = ['andrew tate', 'president trump', 'elon musk', 'cesar augustes']

guests_wont_come = "president trump"
print(f"Unfortunately, {guests_wont_come} can't make it to the dinner.")

new_guest = "adolf hitler"
guests[guests.index(guests_wont_come)] = new_guest

new_guests = ['nikola tesla', 'leonardo dicaprio', 'cristiano ronaldo']

print("Great news! We found a bigger dinner table. More space is available!")

guests.insert(0, new_guests[0])

guests.insert(len(guests) // 2, new_guests[1])

guests.append(new_guests[2])

invitation_template = """Dear {g},
You are cordially invited to a special dinner event. We would be honored to have your presence.
Date: 2 April 2023
Time: 8 PM
Location: Fifth Avenue, NY.
"""
for g in guests:
    print(invitation_template.format(g=g))
    




