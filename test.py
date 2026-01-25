import os

userInput = abs(int(input("Enter a number between 0 and 34: ")))

banditSSH = f"bandit{userInput}@bandit.labs.overthewire.org"

cmd = f'ssh {banditSSH} -p 2220'

os.system(cmd)
