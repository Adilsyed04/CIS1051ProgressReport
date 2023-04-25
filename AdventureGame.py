def introScene():
   print("You wake up in a forest. As you look around, you see a stranger.")
   print("The stranger notices you and walks up to you.")
   print("Stranger: Hello sir, would you like some help?")
   choice= input("Do you want to receive some help from this stranger?(y/n)")
   if choice.lower() == 'y':
       print("Stranger: That's great to hear.")
       print("Stranger: My name is Hywell and I'll be glad to help.")
       introScene2()
   elif choice.lower() == 'n':
      print("Stranger: Oh, well be prepared to die!")
      print("You are killed by the stranger")
      print("###--- GAME OVER ---###")
      quit()
   else:
      print("I didn't quite understand that.\n")
      introScene()

def introScene2():
    inventory=[]
    directions = ["left","right"]
    userInput = ""
    print("Hywell: For starters, here is a map to help you see where you are.")
    print("###--- You have been given a Map--- ###")
    inventory.append('Map')
    print("You look at the map to see two different options.")
    print("If you go left, then you'll find a town.")
    print("If you go right, then you'll encounter a dungeon.")
    while userInput not in directions:
        print("Do you go left or right?")
        userInput = input()
        if userInput == "left":
            print("You go the town with Hywell and end your adventure there.")
            quit()
        elif userInput == "right":
            print("Well then, let us continue on our adventure.")
            print("Hywell: I will not be able to assist you on your journey to the dungeon.")
            print("Hywell: However, please take this sword to help you instead.")
            print("###--- YOU HAVE BEEN GIVEN AN IRON SWORD ---###")
            inventory.append('Iron Sword')
            print("Hywell: I wish you the best of luck!")
            print("You and Hywell part ways.")
            dungeon()
        else:
            print("Please enter a valid option.")
    
def dungeon():
    inventory=[]
    userInput= ""
    fight = ["y","n"]
    print("As you enter the dungeon, you see an enemy.")
    while userInput not in fight:
        print("Do you fight the enemy?(y/n)")
        userInput = input()
        if userInput == "y":
            print("You overpower the enemy with your Iron Sword and emerge victorious!")
            print("Defeating that enemy opens up a path that lets you complete the dungeon.")
            print("Congratulations! You completed your adventure!")
            quit()
        elif userInput == "n":
            print("You are too scared to approach the enemy.")
            print("This fear that you have causes you to leave the dungeon and run away.")
            print("You are a pathetic loser.")
            quit()
        else:
            print("Please enter a valid option.")
    
def main():
        answer = input('Would you like to play the game?(y/n)')

        if answer.lower() == 'y':
            print('Let us Begin')
            start = True
            inventory=[]
        elif answer.lower() == 'n':
            print('Okay, some other time')
            quit()
        else:
            print("I didn't quite understand that.\n")
            main()


        while True:
           name = input("Please State Your Name:\n")
           print("Greetings, "+ name +". Let us begin our adventure!")
           introScene()


              
if __name__ == "__main__":
    main()
              
            
            

                   
