#VARIABLES


# Strings

first_name = "Vaja"
food = "Mtsvadi"
email = "mtsvadimail@shashlik.com"

print(f"Hello {first_name}") # F String
print(f"You like {food}")
print(f"Your email is:  {email}")

# Integers
age = 18
quantity = 3
num_of_community = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your Community has {num_of_community} members")

# Float
price = 10.99
gpa = 4.93
distance = 5.5


print(f"The price is {price}")
print(f"Your gpa is {gpa}")
print(f"You walked: {distance} Kilometers")

# Boolean

is_member = True
for_sale = True

if is_member:
    print("You are a member")
else:
    print("You are unregistered")

if for_sale:
    print("You can buy merch")
else:
    print("That item is for members ONLY")