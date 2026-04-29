# Function for user selecting bandit level
def levelChoice():
	lvlInput = int(input("Enter a bandit level between 0 - 34: "))
		
	if lvlInput > 34:
		print("Invalid response, input numbers between 0 - 34")
		return lvlChoice() # applied recursion to loop back to start of function

	else:
		os.system(f"ssh bandit{lvlInput}@bandit.labs.overthewire.org -p 2220")			

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
