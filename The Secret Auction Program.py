# Key - the persons name
# Value - The bid value
# Add all names and bid values into dictionaries
# Finally we will loop through the dictionary to see which person had the highest bid.

from logo_secret import logo
print(logo)

# Prints 50 blank lines
def clear():
    print("\n" * 50)

empty_dict = {}

# Players can bid, and their name and bid get appended into the empty dictionary
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What is your bid?: $ "))
empty_dict[name] = bid

continuing = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

while continuing == "yes":
    clear()
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    empty_dict[name] = bid
    continuing = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
print(empty_dict)
highest_bidder = 0

if continuing == "no":
    '''
    This will loop through the dictionary to see who has bid the highest amount;
    they will win the auctioned item. 
    '''

    for bidder in empty_dict:
        value = empty_dict[bidder]
        if value > highest_bidder:
            highest_bidder = value
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")

# If they did not say yes or no.
else:
    print("You have added a invaild input")
    