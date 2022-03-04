def main():
    print("Welcome to the game")
    player_name=input("What is your name? ")
    print("Hi "+player_name)
    lives=3
    print(f"You have {lives} lives remaining")
    print("There are four doors presented to you, Forward, Right, Left, Backwards")
    direction=input("Which direction do you want to go? ")
    while direction != "Forward"+"Left"+"Right"+"Backwards":
     if direction=="Forward":
       print("You walk forwards towards the door infront of you")
       break
     elif direction=="Right":
       print("You walk through the door on your right")
       break
     elif direction=="Left":
       print("You walk towards the door on your left")
       break
     elif direction=="Backwards":
       print("You turn around and walk through the door")
       break
     else:
       print("There is no door in that direction and you walked into a solid wall")
       print("You lose a life")
       lives -=1
       if lives<=0:
        print("You have just died")
        break
       print(f"You have {lives} lives remaining")
       direction=input("Which direction do you want to go? ")
main()