def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        with open ('results.txt','a') as file: #save each response
            file.write(guess)

        correct_guesses  += check_answer(questions.get(key),guess)
        question_num += 1

    with open ('results.txt','a') as file: #split trial by space
        file.write(" ")

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        print("Correct Answer:", answer)
        return 0
    
def display_score(correct_guesses, guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")
    print("Answers: ", end="")

    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():
    response = input("Do you want to play again? (Y/N): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?:  ": "C",
    "Is the Earth round?: ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates"],
    ["A. 1989", "B. 1991", "C. 2019"],
    ["A. Greed Island", "B. Hey Guys", "C. Monty Python"],
    ["A. True", "B. False", "C. Depends"]
]

new_game()

while play_again():
    new_game()

print("Bye!")