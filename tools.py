# Function for user selecting bandit level
def levelChoice():
	passwordList = []
	try:
		lvlInput = int(input("Enter a bandit level between 0 - 34: "))
		
		if lvlInput > 34:
			print("Invalid response, input numbers between 0 - 34")
			return sshConnection() # applied recursion to loop back to start of function

		else:
			with open("banditPasswords.txt") as file:
				for i in file:
					passwordList.append(i)	
			
			try:
				joinPasswords = "".join(passwordList[lvlInput])
				print(joinPasswords)

			except IndexError:
				print("Password does not exist")			
	except ValueError:
		print("Invalid response")
		return sshConnection()

# MAIN LOOP
while True:
	start = input("Do you want to start? Y or N: ").upper()

	try:
		if start == "Y":
			levelChoice()			

		elif start == "N":
			print("Program Ended")
			break
		else:
			print("Invalid response, enter Y or N")

	except TypeError:
		print("Invalid response, enter Y or N")
