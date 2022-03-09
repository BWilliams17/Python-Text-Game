def main():
    key1=0
    key2=0
    key3=0
    key4=0

    print("Welcome to the game")
    player_name=input("What is your name?\n\n")
    print("\nHi "+player_name)
    lives=3
    print(f"You have {lives} lives remaining")
    print("\nYou wake up in the middle of a room with no recollection of anything before that.")
    print("There are four doors presented to you, One, Two, Three, Four.")
    direction1=input("Which direction do you want to go?\n\n")
    while direction1 != "One"+"Two"+"Three"+"Four":
     if direction1== "One":
        print("\nYou walk through door One")
        if key1==0:
         print("You walk into a room and filled with the immense hear of fire embers floating aroud the room.")
         print("A message reveals itself over a roaring flame.")
         print("It reads: There is a man that can never enjoy the fireplace, Who is this man?\n")
         print("You can either type; Answer or Hub.\n")
         action1=input("What do you do?\n\n")
         if action1=="Answer":
           answer=input("\nWhat is your answer?\n\n")
           if answer=="Snowman":
            key1=1
            print("\nThe flame distinguishes and a light glows in the middle room.")
            print("A light grows in the Hub room.")
            print("\nYou have unlocked key1 and cleared a room.")
            direction2=input("Where do you want to go? \n\nYou can go to: Hub\n\n")
            if direction2==("Hub"):
             print("\nYou walk back to the Hub")
             direction1=input("Where do you want to go?\n\n")
            else:
             print("That is not a option")
             direction2=input("Where do you want to go?\n\nYou can go to: Hub\n\n")
           else:  
            print("\nYour answer is wrong, You lose a life.\n\n")
            lives-=1
            if lives<=0:
             print("You have just died.")
             break
            print(f"You have {lives} lives remaining.\n")
         elif action1=="Hub":
           print("You walk back to the Hub\n\n")
           direction1=input("Where do you want to go?\n\n")
         else:
           print("\nThat is not an option.")
        if key1==1:
          print("You have already conquered this room.")
          direction1=input("Where do you want to go?\n\n")
     elif direction1=="Two":
        print("\nYou walk through door Two.")
        if key2==0:
          print("\nAs you walk into the room a gust of wind almost knocks you off your balance.")
          print("A strong current can be felt coming out of a crack in the wall infront of you.")
          print("A message reveals itself infront of you, it reads:")
          print("All about, but cannot be seen, Can be captured, cannot be held.")
          print("\nYou can either type; Answer or Hub.\n")
          action2=input("What do you do?\n\n")
          if action2=="Answer\n":
            answer2=input("\nWhat is your answer?\n\n")
            if answer2=="Wind":
             key2=1
             print("\nThe flow of wind suddenly diminishes.")
             print("A light grows in the Hub room.")
             print("\nYou have unlocked key2 and cleared a room.")
             direction2=input("Where do you want to go?\n\nYou can go to: Hub\n\n")
             if direction2=="Hub":
              print("\nYou walk back to the Hub.")
              direction1=input("Where do you want to go?\n\n")
             else:
              print("\nThat is not a option")
              direction2=input("Where do you want to go?\n\nYou can go to: Hub\n\n")
            else:
             print("\nYour answer is wrong, you lose a life.")
             lives-=1
             if lives<=0:
              print("You have just died.")
              break
             print(f"You have {lives} remaining.\n")
          elif action2=="Hub":
           print("You walk back to the hub.")
           direction1=input("Where do you want to go?\n\n")
          else:
           print("\nThat is not an option.\n")
        if key2==1:
          print("You have already conquered this room.")
          direction1=input("Where do you want to go?")
     elif direction1=="Three":
        print("You walk through door Three.")
        if key3==0:
           print("\nYou walk into the room with water filled to your ankle height.")
           print("Water seems to be puring out from a high hole however the water never rises or lowers.")
           print("\nA message appears infront of you, it reads:\nBright as diamonds, Loud as thunder, What am i?")
           print("\nYou can either type; Answer or Hub.")
           action3=input("\nWhat do you do?\n\n")
           if action3=="Answer":
              answer3=input("\nWhat is your answer?\n\n")
              if answer3=="Waterfall":
                 key3=1
                 print("\nThe waterfall stops flowing and everything becomes silent.")
                 print("A light grows in the Hub room.")
                 print("\nYou have unlocked key3 and cleared a room.")
                 direction2=input("Where do you want to go?\n\nYou can go to: Hub\n\n")
                 if direction2=="Hub":
                    print("\nYou walk back to the hub")
                    direction1=input("Where do you want to go?\n\n")
                 else:
                    print("\nThat is not an option")
                    direction2=input("Where do you want to go?\n\nYou can go to: Hub\n\n")
              else:
                 print("Your answer is wrong, you lose a life.")
                 lives-=1
                 if lives<=0:
                    print("You have just died.")
                    break
                 print(f"You have {lives} remaining.")
           elif action3=="Hub":
              print("You walk back to the Hub.")
              direction1=input("Where do you want to go?\n\n")
           else:
              print("\nThat is not an option.")
        if key3==1:
           print("\nYou have already conquered this room.")
           direction1=input("Where do you want to go?")
     elif direction1=="Four":
        print("You walk through door 4.")
        if key4==0:
           print("\nYou walk through the door stepping into a room filled with dirt and grass.")
           print("A message reveals itself infront of you, it reads:")
           print("The more you take, The more you leave behind.")
           print("\nYou can either type; Answer or Hub.")
           action4=input("What do you do?\n\n")
           if action4=="Answer":
              answer4=input("\nWhat is your answer?\n\n")
              if answer4=="Footprints":
                 print("\nGrass suddenly grows over the dirt areas.")
                 print("A light grows in the Hub room.")
                 print("\nYou have unlocked key4 and cleared a room.")
                 direction2=input("Where do you want to go?\n\nYou can go to: Hub\n\n")
                 if direction2=="Hub":
                    print("\nYou walk back to the hub")
                    direction1=input("Where do you want to go?\n\n")
                 else:
                    print("\nThat is not an option")
                    direction2=input("Where do you want to go?\n\nYou can go to: Hub\n\n")
              else:
                 print("Your answer is wrong, you lose a life.")
                 lives-=1
                 if lives<=0:
                    print("You have just died.")
                    break
                 print(f"You have {lives} remaining.")
           elif action4=="Hub":
              print("You walk back to the hub.")
              direction1=input("Where do you want to go?")
           else:
              print("That is not an option.")
              action4=input("What do you want to do?")
        if key4==1:
           print("\nYou have already conquered this room.")
           direction1=input("Where do you want to go?\n\n")
     elif direction1=="Hub":
        print("You are already in the Hub room.")
        direction1=input("Where do you want to go?\n\n")
     else:
        print("\nThere is no door in that direction and you have walked into a solid wall")
        print("You lose a life")
        lives -=1
        if lives<=0:
         print("You have just died")
         break
        print(f"You have {lives} lives remaining\n\n")
        direction1=input("Which direction do you want to go?\n\n")
    if key1==1 and key2==1 and key3==1 and key4==1: 
     print("A spiral staircase reveals itself in the hub room leading upwards.\nYou end up on the surface int he middle of an open grass plain.")
     print("\n\nYou have beaten the game, CONGRATULATIONS!")
     exit()
main()
