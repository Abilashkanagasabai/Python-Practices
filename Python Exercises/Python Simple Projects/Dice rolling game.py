from random import randint
Sum1=0
Sum2=0

user1=True
user2=True
user1_name=input("enter the name of user 1 :")
user2_name=input("enter the name of user 2 :")

while Sum1<20 and Sum2<20:
    while user1:
        roll=input("{0} want to roll?".format(user1_name))
        if roll=="y":
        
            current_roll1=randint(1,6)
            print(current_roll1)
            if current_roll1==2 or current_roll1 == 3 or current_roll1==4:
                print("Unlucky!! you missed the chance")
                break
            else:
                Sum1+=current_roll1
                print(Sum1)
                if Sum1>=20:
                    print("{0} won the game".format(user2_name))
                    print("Thanks for playing")
                    break
        else:
            print("{0} is not rolling".format(user1_name))
        if Sum1>20:
            break
           
       
    while user2:
        roll=input("{} want to roll?".format(user2_name))
        if roll=="y":
        
            current_roll2=randint(1,6)
            print(current_roll2)
            if current_roll2==2 or current_roll2 == 3 or current_roll2==4:

               print("Unlucky!! you missed the chance")
               break
            else:
                Sum2+=current_roll2
                print(Sum2)
                if Sum2>=20:
                    print("{0} won the game".format(user2_name))
                    print("Thanks for playing")

                    break
        else:
            print("{0} is not rolling".format(user2_name))
        if Sum2>20:
            break
        
    
   