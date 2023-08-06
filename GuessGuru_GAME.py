import random
print("Hint! Words are related to python programming\n")

words = ['module', 'tuple', 'mongodb', 'django',
		'dictionary', 'inheritance', 'lambda', 'class',
		'list', 'import', 'function', 'Python']
print("First letter is :\n")
word = random.choice(words)
print(word[0])
print("\nlast letter is :\n")
print(word[-1])
   
print("\nGuess the characters")

guess = ''
choice = 10
while choice > 0:
	failed = 0

	for i in word:

		if i in guess:
			print(i, end=" ")

		else:
			print("_")

			failed += 1

	if failed == 0:
		
		print("You Win")

	
		print("The word is: ", word)
		break

	
	print()
	user_guess = input("guess a character:")

	
	guess += user_guess

	
	if user_guess not in word:

		choice -= 1

		
		print("Better luck next time")

		print("BUCKLE UP! You have", + choice, 'more guesses')

		if choice == 0:
			print("You Loose")
