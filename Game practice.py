def main():
    print("Welcome to the game")
    player_name=input("What is your name?\n\n")
    print("\nHi "+player_name)
    lives=3
    print(f"You have {lives} lives remaining")
    print("\nYou wake up in the middle of a room with no recollection of anything before that.")
    print("There are four doors presented to you, Forward, Right, Left, Backwards.")
    direction=input("Which direction do you want to go?\n\nI walked ")
    if direction != "Forward"+"Left"+"Right"+"Backwards":
     if direction=="Forward" or "Fire":
       print("\nYou walk forwards towards the door infront of you")
       print("You walk into a room and filled with the immense hear of fire embers floating aroud the room.")
       print("A message reveals itself over a roaring flame.")
       print("It reads: There is a man that can never enjoy the fireplace, Who is this man?\n")
       print("You can either type; Answer or Hub.\n")
       action=input("What do you do?\n\n")
       if action=="Answer":
         answer=input("\nWhat is your answer?\n\n")
         if answer="snowman":
           print("The flame distinguishes and a light glows in the middle room")
         else:
           print("")

     elif direction=="Right":
       print("You walk through the door on your right")
     elif direction=="Left":
       print("You walk towards the door on your left")
     elif direction=="Backwards":
       print("You turn around and walk through the door")
     else:
       print("There is no door in that direction and you have walked into a solid wall")
       print("You lose a life")
       lives -=1
       if lives<=0:
        print("You have just died")
        end
       print(f"You have {lives} lives remaining")
       direction=input("Which direction do you want to go? ")
main()
