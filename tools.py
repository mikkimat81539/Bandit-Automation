import os, sys

# Function for user selecting bandit level
def levelChoice():
	passwordList = []
	try:
		lvlInput = int(input("Enter a bandit level between 0 - 34: "))
		
		if lvlInput > 34:
			print("Invalid response, input numbers between 0 - 34")
			return levelChoice # applied recursion to loop back to start of function

		else:
			with open("banditPasswords.txt") as file:
				for i in file:
					passwordList.append(i)	
			
			try:
				joinPasswords = "".join(passwordList[lvlInput])
				print(joinPasswords)
				os.system(f"ssh bandit{lvlInput}@bandit.labs.overthewire.org -p 2220")

			except IndexError:
				print("Password does not exist")			
	except ValueError:
		print("Invalid response")
		return levelChoice()

# MAIN LOOP
def main():
	start = input("Do you want to start? Y or N or INPUT: ").upper()

	try:
		if start == "Y":
			levelChoice()			
			return main()

		elif start == "N":
			print("Program Ended")
			sys.exit()

		elif start == "INPUT":
			with open("banditPasswords.txt", "a") as file:
				password_input = input("Type password: ");
				file.write(f"{password_input}")		
				return main()

		else:
			print("Invalid response, enter Y or N")

	except TypeError:
		print("Invalid response, enter Y or N")

main()
