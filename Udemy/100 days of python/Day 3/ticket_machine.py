print("Welcome to the Ticket Machine!")
height = float(input("Please enter your height in cm:   "))


if height < 120:
    print("Sorry, you have to be at least 120 cm to ride.")
elif height >= 120 and height < 160:
    print("You can ride the rollercoaster.")
else:
    print("You can ride but you need to pay an extra fee of $5.")


    