print("Welcome to the Ticket Machine!")
height = float(input("Please enter your height in cm: "))
total_price = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Please enter your age: "))
    if age <=12:
        total_price = 5
        print("Your ticket price is $5.")
    elif age <=18:
        total_price = 7
        print("Your ticket price is $7.")
    else:
        total_price = 12
        print("Adult ticket price is $12.")
        
        
    whant_photo=input("Do you want a photo taken? (yes/no): ")
    if whant_photo.lower() == "yes":
        total_price += 3
       
        print(f"Your total ticket price including photo is ${total_price}.")
    else:
        print("No photo selected. Enjoy your ride!")
    
else:
    print("Sorry, you must be at least 120 cm tall to ride the roller coaster.")