import random
def generateRandomNumber():
	randomNumber = random.randint(1,3)
	return randomNumber

def getComputerChoice(randomNumber):
	if randomNumber == 1:
		computerChoice = "Paper"
	elif randomNumber == 2:
		computerChoice = "Rock"
	elif randomNumber == 1:
		computerChoice = "Sissors"
	return computerChoice

def getUserChoice():
	userChoice = input("Please choose Rock,Paper or Scissors? ")
	return userChoice

def determineWinner(computerChoice,userChoice):

	Rockm ="The Rock Smashes The Scissors!"
	Scissorsm="The Scissors Cuts The Paper!"
	Paperm="The Paper Wraps The Rock!"
	winner = "No Winner"
	message = " "

	if computerChoice == "Paper" and userChoice == "Rock":
		Winner ="Computer"
		Message = Paperm
	elif computerChoice == "Rock" and userChoice == "Paper":
		Winner ="You"
		Message = Paperm
	if computerChoice == "Scissors" and userChoice == "Paper":
		Winner ="Computer"
		Message = Scissorm
	elif computerChoice == "Paper" and userChoice == "Scissors":
		Winner ="You"
		Message = Scissorsm
	if computerChoice == "Rock" and userChoice == "Scissors":
		Winner ="Computer"
		Message = Rockm
	elif computerChoice == "Scissors" and userChoice == "Rock":
		Winner="You"
		Message = Rockm

	return winner, message

def startAgain():
	randomNumber = generateRandomNumber()
	computerChoice = getComputerChoice(randomNumber)
	userChioce = getUserChoice()
	print("The Computer chose",computerChoice)
	winner,message = determineWinner(computerChoice,userChoice)

	if winner !="No Winner!":
			print(winner, " won(",message, ")" )

	return winner

def main():
	randomNumber = generateRandomNumber()
	computerChoice = getComputerChoice(randomNumber)
	userChioce = getUserChoice()
	print()
	print("The Computer chose",computerChoice)
	winner,message = determineWinner(computerChoice, userChoice)

	if winner !="No Winner!":
			print(winner, " won(",message, ")" )

	while winner == "No Winner":
		print("You Both Chose The Same, It's A Tie")
		winner = startAgain()

main()
