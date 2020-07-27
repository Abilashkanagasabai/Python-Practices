import random
 
hidden = random.randrange(1, 15)
chances=0
# print hidden
while chances<10:
    
    
     
    guess = int(input("Please enter your guess: "))
    chances+=1
 
    if guess == hidden:
        print ("Hit!")
        break
    elif guess < hidden:
        print ("Your guess is too low")
    else:
        print ("Your guess is too high")