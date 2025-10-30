print("Welcome to the Ticket Machine!")
height = float(input("Please enter your height in cm:   "))


if height < 120:
    print("Sorry, you have to be at least 120 cm to ride.")
    age = int(input("Please enter your age:  "))
    if age < 12:
        print("Your ticket price is $5.")
    elif age <= 18:
        print("Your ticket price is $7.")
    else:
        print("Your ticket price is $12.")
elif height >= 120 and height < 160:
    print("You can ride the rollercoaster.")
else:
    print("You can ride but you need to pay an extra fee of $5.")


    