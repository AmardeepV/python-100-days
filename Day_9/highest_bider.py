from os import system

bidders = {}
bidder_available = True
max_bid_value = 0
highest_bider = ''

print("Welcome to the secret auction program")
while bidder_available:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    check_bidder = input(
        "Are there any other bidders? Type \'yes\'or \'no\'. ").lower()
    if check_bidder == 'yes':
        pass
    elif check_bidder == 'no':
        bidder_available = False
    else:
        print("Wrong input: please either enter \'yes\' or \'no\'")

    print("\n" * 20)

for i in bidders:
    if bidders[i] > max_bid_value:
        highest_bider = i
        max_bid_value = bidders[i]
print(f"The winner is {highest_bider} with a bid of {bidders[highest_bider]}")
