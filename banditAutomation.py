import os

def terminalAutomation():
	banditSSH = f"bandit{userInput}@bandit.labs.overthewire.org"
	
	# cmd = f'ssh {banditSSH} -p 2220'
	# os.system(cmd)
	
	passwordList = []

	with open("banditPasswords.txt") as file:
		for i in file:
			passwordList.append(i)
			
	try:
		passwordJoin = "".join(passwordList[userInput])
		print(passwordList[userInput])
	except IndexError:
		print("Line does not exist")

while True:
	userExit = input("Do you want to start? Y or N: ").upper()

	if userExit == "Y":
		try:
			userInput = abs(int(input("Enter a number between 0 and 34: ")))
			if userInput > 34:
				print("wrong input, enter a number")		

			elif userInput == 'exit':
				print("Program ended")
				break

			else:
				terminalAutomation()
		except ValueError:
			print("wrong input")

	elif userExit == "N":
		print("Program ended")
		break

	else:
		print("Invalid Input")
