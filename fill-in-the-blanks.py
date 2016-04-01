# IPND Stage 2 Final Project

# The game must give out a sample paragraph to get users to enter in correct strings. 
# Must run in terminal. 
# Must have 3 more or more levels. 

easyParagraph = '''A ___1___ is created with HTML, CSS and Java Script. The 49ers are a  ___2___ team. 
Payton Manning is famous for his ablity to play ___2___. And even though he was caught with deflated ___2___s 
he remains one of the best quaterbacks in the ___3___. The NFL barely even fined him for his actions. It basically was
a slap on the ___4___ .'''

#I got this paragraph from https://wiki.python.org/moin/
mediumParagraph = '''___1___ combines remarkable power with very clear syntax. It has ___2___, 
classes, exceptions, very high level ___3___ data types, and ___3___ typing. There are interfaces 
to many system calls and libraries, as well as to various windowing systems. New built-in ___2___ 
are easily written in C or C++ (or other ___4___, depending on the chosen implementation).'''

#I got this paragraph from https://answers.yahoo.com/question/index?qid=20090310220140AAy8ZFx
hardParagraph = '''Perhaps the most misleading aspect of a dinosaur's ___1___ figure may simply 
prove to compromise a reality of ___2___ creatures that demolish and create unique structures thus 
reuniting and additionally eliminating the openly incredibly rescinding factor which could ___3___ 
lead to an overall mental breakdown of an average human fetus and ___3___ pronounce the possibility 
of a technique used often by a large distribution of many possible energetic ___4___ theories that 
completely demolish any chance of penetration in the quartz industrial distribution infatuation.'''


easyAnswers = ["webpage", "football", "NFL", "wrist"]

mediumAnswers = ["Python", "modules", "dynamic", "languages"]

hardAnswers = ["prehistoric", "inhumane", "possibly", "quantum"]

level = ()
answers = ()
guesses = ()

def playGame():
	"""This takes a user from choosing which level to play, to choosing how many wrong 
	answers they can go through, to entering all of their guesses and be returned with 
	the results of their guesses. It's not pretty but it gets the job done :) """
	user_input = raw_input("""Please select a game difficulty by typing it in!
Possible choices include easy, medium and hard.""" + """ 
""")
	if user_input == "easy":
		print "You chose easy!"
		level = easyParagraph
		answer = easyAnswers
		n_of_guesses = raw_input("""How many total wrong guesses would you like to have access to? Please enter a possitive integer number: """)
		while n_of_guesses > 0:
			print "The current paragraph reads as such:"
			print level 
			firstGuess = raw_input("What should be substituted in for ___1___?")
			if firstGuess == easyAnswers[0]:
				while n_of_guesses > 0:
					print "Congrats! That's correct."
					print "The current paragraph reads as such:"
					level = level.replace("___1___", easyAnswers[0])
					print level
					secondGuess = raw_input("what should be substituted in for ___2___?")
					if secondGuess == easyAnswers[1]:
						while n_of_guesses > 0:
							print "Congrats! That's correct."
							print "The current paragraph reads as such:"
							level = level.replace("___2___", easyAnswers[1])
							print level
							thirdGuess = raw_input("what should be substituted in for ___3___?")
							if thirdGuess == easyAnswers[2]:
								while n_of_guesses > 0:
									print "Congrats! That's correct."
									print "The current paragraph reads as such:"
									level = level.replace("___3___", easyAnswers[2])
									print level
									fourthGuess = raw_input("what should be substituted in for ___4___?")
									if fourthGuess == easyAnswers[3]:
										while n_of_guesses > 0:
											print "Congrats! That's correct."
											level = level.replace("___4___", easyAnswers[3])
											print level
											return "You won!"
									else: 
										n_of_guesses = int(n_of_guesses)-1
										if n_of_guesses == 0:
											return "Sorry, that's all your guesses! Game Over."
										print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
							else: 
								n_of_guesses = int(n_of_guesses)-1
								if n_of_guesses == 0:
									return "Sorry, that's all your guesses! Game Over."
								print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
					else: 
						n_of_guesses = int(n_of_guesses)-1
						if n_of_guesses == 0:
							return "Sorry, that's all your guesses! Game Over."
						print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
			else: 
				n_of_guesses = int(n_of_guesses)-1
				if n_of_guesses == 0:
					return "Sorry, that's all your guesses! Game Over."
				print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"


	elif user_input == "medium":
		print "You chose medium!"
		level = mediumParagraph
		answer = mediumAnswers
		n_of_guesses = raw_input("""How many total wrong guesses would you like to have access to? Please enter a possitive integer number: """)
		while n_of_guesses > 0:
			print "The current paragraph reads as such:"
			print level 
			firstGuess = raw_input("What should be substituted in for ___1___?")
			if firstGuess == mediumAnswers[0]:
				while n_of_guesses > 0:
					print "Congrats! That's correct."
					print "The current paragraph reads as such:"
					level = level.replace("___1___", mediumAnswers[0])
					print level
					secondGuess = raw_input("what should be substituted in for ___2___?")
					if secondGuess == mediumAnswers[1]:
						while n_of_guesses > 0:
							print "Congrats! That's correct."
							print "The current paragraph reads as such:"
							level = level.replace("___2___", mediumAnswers[1])
							print level
							thirdGuess = raw_input("what should be substituted in for ___3___?")
							if thirdGuess == mediumAnswers[2]:
								while n_of_guesses > 0:
									print "Congrats! That's correct."
									print "The current paragraph reads as such:"
									level = level.replace("___3___", mediumAnswers[2])
									print level
									fourthGuess = raw_input("what should be substituted in for ___4___?")
									if fourthGuess == mediumAnswers[3]:
										while n_of_guesses > 0:
											print "Congrats! That's correct."
											level = level.replace("___4___", mediumAnswers[3])
											print level
											return "You won!"
									else: 
										n_of_guesses = int(n_of_guesses)-1
										if n_of_guesses == 0:
											return "Sorry, that's all your guesses! Game Over."
										print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
							else: 
								n_of_guesses = int(n_of_guesses)-1
								if n_of_guesses == 0:
									return "Sorry, that's all your guesses! Game Over."
								print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
					else: 
						n_of_guesses = int(n_of_guesses)-1
						if n_of_guesses == 0:
							return "Sorry, that's all your guesses! Game Over."
						print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
			else: 
				n_of_guesses = int(n_of_guesses)-1
				if n_of_guesses == 0:
					return "Sorry, that's all your guesses! Game Over."
				print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"

	elif user_input == "hard": 
		print "You chose hard!"
		level = hardParagraph
		answer = hardAnswers
		n_of_guesses = raw_input("""How many total wrong guesses would you like to have access to? Please enter a possitive integer number: """)
		while n_of_guesses > 0:
			print "The current paragraph reads as such:"
			print level 
			firstGuess = raw_input("What should be substituted in for ___1___?")
			if firstGuess == hardAnswers[0]:
				while n_of_guesses > 0:
					print "Congrats! That's correct."
					print "The current paragraph reads as such:"
					level = level.replace("___1___", hardAnswers[0])
					print level
					secondGuess = raw_input("what should be substituted in for ___2___?")
					if secondGuess == hardAnswers[1]:
						while n_of_guesses > 0:
							print "Congrats! That's correct."
							print "The current paragraph reads as such:"
							level = level.replace("___2___", hardAnswers[1])
							print level
							thirdGuess = raw_input("what should be substituted in for ___3___?")
							if thirdGuess == hardAnswers[2]:
								while n_of_guesses > 0:
									print "Congrats! That's correct."
									print "The current paragraph reads as such:"
									level = level.replace("___3___", hardAnswers[2])
									print level
									fourthGuess = raw_input("what should be substituted in for ___4___?")
									if fourthGuess == hardAnswers[3]:
										while n_of_guesses > 0:
											print "Congrats! That's correct."
											level = level.replace("___4___", hardAnswers[3])
											print level
											return "You won!"
									else: 
										n_of_guesses = int(n_of_guesses)-1
										if n_of_guesses == 0:
											return "Sorry, that's all your guesses! Game Over."
										print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
							else: 
								n_of_guesses = int(n_of_guesses)-1
								if n_of_guesses == 0:
									return "Sorry, that's all your guesses! Game Over."
								print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
					else: 
						n_of_guesses = int(n_of_guesses)-1
						if n_of_guesses == 0:
							return "Sorry, that's all your guesses! Game Over."
						print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"
			else: 
				n_of_guesses = int(n_of_guesses)-1
				if n_of_guesses == 0:
					return "Sorry, that's all your guesses! Game Over."
				print "That isn't the correct answer!  Let's try again; you have " + str(n_of_guesses) + " trys left!"

	else: 
		print "User input invalid."
    	return None






print playGame()


