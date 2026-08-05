print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You typed a wrong input.")
    exit()

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
elif pepperoni not in ["Y", "N"]:
    print("You typed a wrong input.")
    exit()

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1
elif extra_cheese not in ["Y", "N"]:
    print("You typed a wrong input.")
    exit()

print(f"Your final bill is: {bill}")
