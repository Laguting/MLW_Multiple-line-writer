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
print("\33[31m\33[1mThank you for your patience!˶^•ﻌ•^˵ \33[0m\n")
print("\33[7m-+°\33[0m" * 45)

# Your One line Diary
print("\n✧ ✧ ✧ ૮ • ﻌ • აฅ HI ✧ ✧ ✧\n")
one_line_diary = Figlet(font = "slant")
print(colored(one_line_diary.renderText("Your One Line Diary"), "yellow"))
print("\33[7m-+°\33[0m" * 45)
# Open file and allow it to be rewritten
# greet the user
# Ask the user to enter any response
# Close the file
# Close program