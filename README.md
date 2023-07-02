## Quiz Game
The Python code provided is a quiz game where the player is asked a series of multiple-choice questions and their answers are evaluated to determine their score. Here's a breakdown of the code:

The `new_game()` function initializes the necessary variables, including an empty list guesses to store the player's answers, a variable `correct_guesses` to keep track of the number of correct answers, and `question_num` to iterate through the questions dictionary.

Inside the for loop in `new_game()`, the program prints each question and its corresponding options from the questions and options dictionaries. It then prompts the user to enter their guess (A, B, C, or D), which is converted to uppercase and added to the guesses list.

The user's guess is written to a file called 'results.txt' using the with open statement, which appends the guess to the file.

The `check_answer(answer, guess)` function compares the user's guess with the correct answer. If the guess is correct, it prints "CORRECT!" and returns 1. Otherwise, it prints "WRONG!" and the correct answer, and returns 0.

The `display_score(correct_guesses, guesses)` function prints the results of the quiz, including the correct answers, the user's guesses, and their score percentage.

The `play_again()` function prompts the user to enter whether they want to play again (Y/N) and returns True if the response is "Y" (yes) and False otherwise.

The questions dictionary stores the questions as keys and their corresponding correct answers as values.

The options list is a nested list that contains the options for each question in the same order as the keys in the questions dictionary.

The initial quiz is started by calling `new_game()`.

After the initial quiz, the program enters a while loop that continues as long as the `play_again()` function returns True. Inside the loop, a new game is started by calling `new_game()` again.

If the user chooses not to play again, the loop ends, and the program prints "Bye!" to indicate the end of the game.
