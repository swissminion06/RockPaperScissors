import random as r
import os
import time as t

from gevent import sleep
ChoiceList = ["rock", "paper", "scissors"]

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print("Possible moves are: Rock, Paper or Scissors")

while True:
    InputUser = input("Make your move: ")
    InputUserlowercase = InputUser.lower()
    pcmove = r.choice(ChoiceList)
    if InputUserlowercase == pcmove:
        print(InputUserlowercase + " VS " + pcmove)
        print("Draw")
        t.sleep(2)
        clearConsole()
    else:     
        if InputUserlowercase == "paper" and pcmove == "rock" or InputUserlowercase == "rock" and pcmove == "scissors" or InputUserlowercase == "scissors" and pcmove == "paper":
            print(InputUserlowercase + " VS " + pcmove)
            print("Player Won")
            t.sleep(2)
            clearConsole()
        elif InputUserlowercase != "rock" or "paper" or "scissors":
            print("Not a valid input!")
            t.sleep(2)
            clearConsole()
        else: 
            print(InputUserlowercase + " VS " + pcmove)
            print("PC Won")
            t.sleep(2)
            clearConsole()