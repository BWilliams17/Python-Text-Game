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
    direction=input("Which direction do you want to go?\n\n")
    while direction != "One"+"Two"+"Three"+"Four":
     if direction== "One":
        print("\nYou walk forwards towards the door infront of you")
        if key1==0:
         print("You walk into a room and filled with the immense hear of fire embers floating aroud the room.")
         print("A message reveals itself over a roaring flame.")
         print("It reads: There is a man that can never enjoy the fireplace, Who is this man?\n")
         print("You can either type; Answer or Hub.\n")
         action=input("What do you do?\n\n")
         if action=="Answer":
          answer=input("\nWhat is your answer?\n\n")
          if answer=="Snowman":
            key1=1
            print("The flame distinguishes and a light glows in the middle room.")
            print("A light grows in the Hub room")
            print("You have unlocked key1 and cleared a room")
            direction2=input("Where do you want to go? Hub, Two, Three or Four?\n\n")
            if direction2==("Hub"):
             print("You walk back to the Hub")
             direction=input("Where do you want to go?\n\n")
          else:  
              print("\nYour answer is wrong, You lose a life.\n\n")
              lives-=1
              if lives<=0:
               print("You have just died")
               break
              print(f"You have {lives} lives remaining\n")
              action=input("Do you want to try again or leave?\n\nYou can either type; Answer or Hub.\n\n")
              if action=="Hub":
               print("You walk back to the hub\n\n")
               direction=input("Where do you want to go?\n\n")
         elif action=="Hub":
          print("You walk back to the Hub\n\n")
          direction=input("Where do you want to go?\n\n")
        if key1==1:
          print("You have already conquered this room.")
          direction=input("Where do you want to go?\n\n")
     elif direction=="Two":
        print("You walk through the door under Two.")
     elif direction=="Left":
        print("You walk towards the door on your left.")
     elif direction=="Backwards":
        print("You turn around and walk through the door.")
     elif direction=="Hub":
        print("You are already in the Hub room.")
     else:
        print("\nThere is no door in that direction and you have walked into a solid wall")
        print("You lose a life")
        lives -=1
        if lives<=0:
         print("You have just died")
         break
        print(f"You have {lives} lives remaining\n\n")
        direction=input("Which direction do you want to go?\n\nI walked ")
main()
        print("You have just died")
        end
       print(f"You have {lives} lives remaining")
       direction=input("Which direction do you want to go? ")
main()
