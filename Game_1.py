import random


def get_a_guess(player):
    while True:
        guess = input(f"{player}, enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            break
        print("I need you to enter a number.")

    return guess


def get_guesses(player1, player2):
    # instructions
    print("I have picked a random number between 1 and 100.")
    print("Can you guess it?")
    print()

    # get guesses
    guess1 = get_a_guess(player1)
    guess2 = get_a_guess(player2)

    return guess1, guess2


def determine_winner(number, player1, player2, guess1, guess2):
    # get differences
    diff1 = abs(number - guess1)
    diff2 = abs(number - guess2)

    # determine winner
    if diff1 == diff2:
        if diff1 == 0:
            print("Wow, you both guessed it!")
        else:
            print(f"You tied! The number was {number} and you were both {diff1} away.")

    elif diff1 < diff2:
        if diff1 == 0:
            print(f"Wow, {player1}, you guessed it exactly. You win!")
        else:
            print(f"{player1} wins! The number was {number} and {player1} was {diff1} away.")
        print(f"Sorry, {player2}, you were {diff2} away.")

    else:
        if diff1 == 0:
            print(f"Wow, {player2}, you guessed it exactly. You win!")

        else:
            print(f"{player2} wins! The number was {number} and {player2} was {diff2} away.")
        print(f"Sorry, {player1}, you were {diff1} away.")


def guessing_game():
    print("Welcome to the guessing game! What are your names?")
    # get names
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # pick a number
    number = random.randint(1, 100)

    # get guesses
    guess1, guess2 = get_guesses(player1, player2)

    determine_winner(number, player1, player2, guess1, guess2)





def adventure():
    advent = input("\nType 1, 2, or 3: ")
    if advent == "1":
        print("\nYou chose the cave, inside you find two tunnels, the tunnel on the left is producing wind, do you:")
        cave()
    elif advent == "2":
        frogs()
    elif advent == "3":
        print("You chose to continue hiking down the trail, unfortunately you ran into a bear and you died.")
    else:
        print("Invalid entry, type 1, 2, or 3")
        adventure()

def cave():
    direction = input("\n(1)stay where you are, (2)go down the windy tunnel to the left, or (3)go down the right tunnel?: ")
    if direction == "1":
        print("You decided to stay put")
        stone = input("You find a large stone, do you pick it up? (Type yes or no): ")
        if stone.upper() == "YES":
            rock = "Y"
            print("You grabbed the stone, but you hear something big approaching the cave!")
            direction = input("Do you go down the left or right tunnel? Type 1 for left and 2 for right: ")
            if direction == "1":
                print("You chose the left tunnel!")
                left_tunnel(rock)
            elif direction == "2":
                print("You chose the right tunnel!")
                right_tunnel(rock)
            else:
                print("I guess you didn't want to go in either, the sound approaches the cave entrance and a bear is the last thing you see!")
        else:
            rock = "N"
            print("You did not grab the stone, but you hear something big approaching the cave!")
            direction = input("Do you go down the left or right tunnel? Type 1 for left and 2 for right: ")
            if direction == "1":
                print("You chose the left tunnel!")
                left_tunnel(rock)
            elif direction == "2":
                print("You chose the right tunnel!")
                right_tunnel(rock)
            else:
                print("I guess you didn't want to go in either, the sound approaches the cave entrance and a bear is the last thing you see!")

    elif direction == "2":
        rock = "N"
        print("You chose the left tunnel")
        left_tunnel(rock)
    elif direction == "3":
        rock = "N"
        print("You chose the right tunnel")
        right_tunnel(rock)
    else:
        print("Invalid entry, type 1, 2, or 3")
        cave()



def left_tunnel(rock):
    print("\n You follow the wind to see where its comming from...")
    print("\n As you crawl down the tunnel you notice the wind is getting stronger and hotter...")
    print("\n You bump into something and see two red eyes looking back at you... looks like you found an undiscovered species of dragon!")
    if rock == "Y":
        print("Luckily you have a rock to defend yourself! You throw it at the dragon and knock the beast out cold. You find a golden sword behind the beast!")
        sword = "Y"
        print("You turn around and exit the cave, but something is waiting for you outside of the cave...")
        frog_boss(sword)
    else:
        print("The dragon's gapping jaws are the last thing you see! If you only had a rock or something...")
        


def right_tunnel(rock):
    print("\nYou travel deep into the tunnel and find a hobo living there, he says he has a golden sword for you but needs a stone for it. Can you trade?")
    if rock == "Y":
        print("Wow lucky me! He says, you do have a rock for me, here is this useless golden sword I found. You decide to take the sword.")
        sword = "Y"
        print("You turn around and exit the cave, but something is waiting for you outside of the cave...")
        frog_boss(sword)
    else:
        print("This hobo looks really upset that you don't have a rock for him, wait why is he so mad, and why is he picking up his sword!?")

def frogs():
    print("\nYou decide to look for frogs, and oh look you found 2! One of them hops into a hole and the other one starts swimming away.")
    froggy = input("Which frog do you grab? Type 1 for the one in the hole and type 2 to grab the one swimming away: ")
    if froggy == "1":
        print("In the hole the frog is gone, but you found a golden sword!")
        sword = "Y"
        print("You hear something big stomping through the forest, its getting closer...")
        frog_boss(sword)
    else:
        sword = "N"
        print("Darn the frog was too fast and swam away! Wait, do you hear something?")
        print("You hear something big stomping through the forest, its getting closer...")
        frog_boss(sword)
    
def frog_boss(sword):
    print("It's the final frog boss! He is huge!!! I hope you have a weapon...")
    if sword == "Y":
        print("\nThe giant frog pounches on you! It's getting hard to breath... \nluckily you raised your sword, and the king frog has died! \nYou go home a happy person with a new golden sword!")
    else:
        print("Too bad you didn't have a weapon, now you live in the king frog's stomach...")



def choose_game():
    print("Welcome to the arcade! Would you like to play the guessing game or choose your own adventure?")
    game = input("Type 1 to play the guessing game or 2 to choose your own adventure: ")
    if game == "1":
        guessing_game()
    elif game == "2":
        print("You are going for a hike! You see a cave a few yards off of the trail near a creek. Do you: (option 1) go into the cave, (option 2) go down to the creak and look for frogs, or (option 3) keep hiking on the trail?")
        adventure()
    else:
        print('---------->Invalid Input please type 1 or 2<----------')
        choose_game()

if __name__ == '__main__':
    choose_game()
