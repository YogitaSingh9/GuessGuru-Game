# GuessGuru-Game
Description:

Welcome to GuessGuru🤔, an addictive and challenging word guessing game developed in Python. 

Approch:

1. Import Necessary Module:
Begin by importing any necessary libraries. For a basic word guess game. I used Python Random module, which is an in-built module of Python that is used to generate random numbers in Python

2. Create a Word List:
Prepare a list of words that players will guess from. You can store these words in a Python list variable.

3. Select a Random Word:
Randomly select a word from the list to be guessed by the player. with the use of random module.

4. Display Initial Guessing Status:
Show the player the initial state of the word they need to guess. for example you can provide them the first and the last character of the word and can add one hint about the question.

5. Accept Player Input:
Prompt the player to guess a letter. Accept the input from the player using the input() function and store it in a variable.

6. Check the Guessed Letter:
Compare the guessed letter with the letters of the selected word. Update the displayed word accordingly, revealing any correctly guessed letters.

7. Keep Track of Incorrect Guesses:
Create a mechanism to keep track of the number of incorrect guesses made by the player.

9. Limit the Number of Guesses:
Set a maximum number of incorrect guesses allowed for the player. If the player exceeds this limit, the game is over.

10. End Game Conditions:
Define the conditions for ending the game. The game should end either when the player correctly guesses the word or when they exhaust their allowed incorrect guesses.

11. Display Game Outcome:
After the game ends, inform the player whether they won or lost and display the correct word.

12. Wrap the Game in a Loop:
To allow continuous gameplay, wrap the entire game logic in a loop that asks the player if they want to play again after each round.
