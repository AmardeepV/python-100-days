print("Welcome to Python Pizza deliveries!")
# small pizza $15, medium $20 and large $25
size = input("What size pizza do yo want? S, M or L ")
# extra $2 on small, $3 for medium and large
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")  # extra $1

bill = 0

# 2: Calculate the final amount based on the size and the topings selected
if size == 'S':
    bill = 15
    if pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
elif size == 'M':
    bill = 20
    if pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
elif size == 'L':
    bill = 25
    if pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
else:
    print("Wrong size selection, please select correct size")

if pepperoni == 'Y':
    if extra_cheese == 'Y':
        print(
            f"For {size} pizza with pepperoni and extra cheese, your total is ${bill}")
    else:
        print(f"For {size} pizza with pepperoni, your total is ${bill}")
else:
    if extra_cheese == 'Y':
        print(f"For {size} pizza with extra cheese, your total is ${bill}")
    else:
        print(f"For {size} pizza, your total is ${bill}")
