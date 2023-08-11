'''
You just heard that one of your guests can't
make the dinner, so you need to send out a new set of invitations. You'll
have to think of someone else to invite.
Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can't make it.
Modify your list, replacing the name of the guest who can't make it with the
name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still in
your list.
'''

guests = ['andrew tate', 'president trump', 'elon musk', 'cesar augustes']

guests_wont_come = "president trump"
print(f"Unfortunately, {guests_wont_come} can't make it to the dinner.")

new_guest = "adolf hitler"
guests[guests.index(guests_wont_come)] = new_guest

for guest in guests:
    print(f"Dear {guest},\nYou are cordially invited to a special dinner event. ")


          

