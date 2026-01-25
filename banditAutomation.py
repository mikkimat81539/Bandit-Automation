import os

def automation():
	banditSSH = f"bandit{userInput}@bandit.labs.overthewire.org"
	
	cmd = f'ssh {banditSSH} -p 2220'
	os.system(cmd)

while True:
	userExit = input("Do you want to start? YES or NO: ").upper()

	if userExit == "YES":
		try:
			userInput = abs(int(input("Enter a number between 0 and 34: ")))
			if userInput > 34:
				print("wrong input, enter a number")		

			elif userInput == 'exit':
				print("Program ended")
				break

			else:
				automation()
		except ValueError:
			print("wrong input")

	elif userExit == "NO":
		print("Program ended")
		break

	else:
		print("Invalid Input")
