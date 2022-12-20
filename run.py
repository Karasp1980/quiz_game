def start_game():
    """
    Allow player to enter name and start quiz.
    """
    print("⭐⭐⭐⭐⭐ Welcome to Our Planets quiz! ⭐⭐⭐⭐⭐")
    player_name = input("Please enter your name: \n")

    if player_name == " ":
        print("A name is required to start the quiz, please try again.")
        start_game()

    else:
        # Capitalizes the first letter in the name in case
        # user enteres only lowercase letters
        player_name = player_name.capitalize()
        start = input(f"Hi {player_name} and welcome! Would you like to start the game? (y/n) \n")
        start = start.lower()

        
        while start != 'y' and start != 'n':
            start = input("Invalid input! Do you want to play? (y/n): ")
            start = start.lower()

        if start == "y":
            print("Lets start the game!⭐ \n")
            new_game()
        elif start == "n":
            print("Welcome back next time, bye! \n") 


def new_game():
    """
     Creates a new game and starts the game and starts displaying questions.
    """

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("* * * * * * * * * * * * * * * * * * * * * * * * *")
        print(key)
        
        while True:
        
            valid_inputs = ["a", "b", "c"]

            for i in options[question_num-1]:
                print(i)
            guess = input("Enter (a, b or c): ")
            guess = guess.lower()
                
            if guess in valid_inputs:
                guesses.append(guess)

                correct_guesses += check_answer(questions.get(key), guess)
                question_num += 1
                break
                
            else:
                print("Invalid input, please enter a, b or c")
        
    display_score(correct_guesses, guesses)

    while play_again():
        new_game()

# -------------------------
def check_answer(answer, guess):
    """
    Displays correst or wrong answer after every question 
    (after the player has answered) in order to let the 
    user see directly if the anser was correct.
    """

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    """
    When the game is finished and all the question has 
    been answered a display of scores shows in order to 
    let the user see the answers compared to the right
    answers as well as the total score contained.
    """
    print("* * * * * * * * * * * * * * * * * * * * * * * * *")
    print("Your results:")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # Print out number of stars according to number of scores
    stars = []
    j = 0
    while j < correct_guesses:
        stars.append("⭐")
        j += 1   
  
    print(f"Good job, you scored: {correct_guesses} out of {len(questions)} {''.join(stars)}")

# -------------------------
def play_again():
    """
    Allows the player to chose to play again or quit the game.
    """

    response = input("Do you want to play again? (y/n): ")
    response = response.lower()

    while response != 'y' and response != 'n':
            response = input("Invalid input! Do you want to play again? (y/n): ")
            response = response.lower()

    if response == "y":
        return True
    elif response == "n":
        print("Thanks for playing!")
        return False 
        
        

questions = {
 "⭐ Which is the 5th planet from the sun?: ": "a",
 "⭐ Which is one of Saturns moons?: ": "b",
 "⭐ Which planet is closest to the sun: ": "c",
 "⭐ Which atmospheric color does Neptune have?: ": "a",
 "⭐ How long time does it take for the sunlight to reach the earth?: ": "b",
 "⭐ Which year was the first moon landing: ": "b",
 "⭐ What is the characteristic anticyclonic storm on Jupiter called: ": "c",
 "⭐ How many years ago did the solar system form?: ": "b"
}

options = [
          ["a. Jupiter", "b. Saturnus", "c. Mars"],
          ["a. Europa", "b. Titan", "c. Io"],
          ["a. Saturn", "b. Venus", "c. Mercury"],
          ["a. Blue", "b. Red", "c. White"],
          ["a. 8 seconds", "b. 8 minutes", "c. 8 hours"],
          ["a. 1989", "b. 1969", "c. 1949", "d. 1972"],
          ["a. Great Blue Spot", "b. Elfa", "c. Great Red Spot"],
          ["a. 140 million", "b. 4,5 billion", "c. 2,5 billion"]
          ]

start_game()





