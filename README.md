# Bandit Automation

## Overview

Bandit Automation is a Python command-line tool I developed to simplify connecting to [OverTheWire Bandit](https://overthewire.org/wargames/bandit/). I created it because I was tired of repeatedly typing SSH commands and manually looking up saved passwords for each level.

The program prompts users to select a Bandit level, retrieves the corresponding password from a local text file, and launches an SSH connection to the selected remote account.

## Features

- **Level Selection:** Prompts users to select a Bandit level between 0 and 34.
- **Password Lookup:** Reads saved passwords from a local text file and retrieves the entry corresponding to the selected level.
- **SSH Automation:** Constructs and executes an SSH command to connect to the selected Bandit account on the OverTheWire server.
- **Input Handling:** Includes basic validation for invalid level inputs and missing password entries.
- **Password Management:** Provides an option to append password entries to the local password file.

## Technologies Used

- Python
- SSH
- Linux command-line tools
- File I/O
- Exception handling
- OverTheWire Bandit

## How It Works

1. The user starts the program.
2. The user selects a Bandit level.
3. The program reads the corresponding password from `banditPasswords.txt`.
4. The program initiates an SSH connection to the selected Bandit account.
5. The user can repeat the process to connect to another level.

## What I Learned

- Automating repetitive command-line tasks with Python.
- Reading and managing data stored in text files.
- Connecting to remote systems using SSH.
- Handling invalid input and file lookup errors.
- Understanding the importance of protecting credentials and managing sensitive information.


## Disclaimer

This project is intended for educational purposes with the OverTheWire Bandit wargame. Use it only with systems you own or have permission to access.
