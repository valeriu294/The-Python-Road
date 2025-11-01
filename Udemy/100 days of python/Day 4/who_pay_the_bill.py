import random 


print("Let's find out who will pay the bill today!")

friends = input("Enter the names of your friends, separated by commas: ").split(", ") #create a list of names by splitting the input string at each comma
payer = random.choice(friends) #randomly choose one name from the list

print(f"{payer} is going to pay the bill today!")
