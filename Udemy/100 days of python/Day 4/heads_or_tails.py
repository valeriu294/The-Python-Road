import random 


print ("Welcome to Heads or Tails Game!")

choose = input("Choose (h) for heads or (t) for tails: ").lower()
toss = random.choice(['h', 't'])
if choose == toss:
    print("You win!")
else:
    print("You lose!")
    