# Exercise Number 2 Shopping Cart

item = input("What item would you like to buy?: ")
priced = float(input("What is the price in dollars?: "))
quantity1 = int(input("how many would you like to buy?: "))
total = priced * quantity1

print(f"You have bought {quantity1} of {item}/s")
print(f"This will be {total}$ <3")