import random
from capitals import states

print("Greetings! How well do you know the geography of the United States? Guess the capitals of each state and test your knowledge!")

def guess_capital():
    score = 0

    random.shuffle(states)
    for i in range(len(states)):
        x = input(f"What is the capital of {states[i]['name']}? ")
        if x == states[i]['capital']:
            score += 1
            print(f"That's correct. Score:{score}")
        elif x != states[i]['capital']:
            score -= 1
            print(
                f"Sorry, the answer is {states[i]['capital']} Score:{score}.")
    play_again = input(f"Play again?? Y/N?")
    if play_again == "y":
        guess_capital()
    elif play_again == "n":
        f"Bye!"


guess_capital()
