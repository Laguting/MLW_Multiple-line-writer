# Laguting, Maricon Jane G.
# BSCPE 1-4 
# Task: Write a method in python to write multiple line of text contents into a text file mylife.txt. 
# Welcome the user
from pyfiglet import Figlet
from termcolor import colored
ti_tle = Figlet(font = "starwars")
print("\33[7m-+°\33[0m" * 45)
print ("")
print(colored(ti_tle.renderText("WELCOME!"), "cyan"))
print("\33[33m\33[21m ฅ՞•ﻌ•՞ฅ \33[0m" * 15)
print("\33[7m-+°\33[0m" * 45)
   # Loading feature
print("\n\n")
from tqdm import tqdm 
import time
for i in tqdm (range (100), desc="Loading...\U0001F973"):
    time.sleep(0.05)
    pass
print("\n\n")
print("\33[31mThank you for your patience!˶^•ﻌ•^˵ \33[0m\n")
print("\33[7m-+°\33[0m" * 45)
# Open file and allow it to be rewritten
# Your One line Diary
# greet the user
# Ask the user to enter any response
# Close the file
# Close program