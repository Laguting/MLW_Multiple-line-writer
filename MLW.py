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
# Inform the date
from datetime import date
date_now = date.today()
# Open file and allow it to be rewritten
with open("mylife.text", "w") as mylife_file:
# Greet the user and Ask the user to enter any response
    keep_going = True
    while keep_going:
      insert_line = input("\n\n\33[32m Today is " + str(date_now) + " How was your day today? What are your realizations? ｡:ﾟ૮ ˶ˆ ﻌ ˆ˶ ა ﾟ:｡ " ":\33[0m")
      mylife_file.write(str(date_now) + ": " + insert_line + '\n')
# Ask the user for the continuation
      question_usr = input("\n\33[36m\33[3m  ^•ﻌ•^ฅ♡   Are there any more realizations for today? Enter 'Y' for yes and 'N' for no: \33[0m")
      if question_usr.upper() == "N":
                print(" \n\n \33[31mYour one line realizations i snow recorded to the file.     ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა  \33[0m\n")
                print("\33[7m-+°\33[0m" * 45)
                keep_going = False                
# Close the file
    mylife_file.close()
# Close program
clo_sing = Figlet(font = "bubble")
print(colored(clo_sing.renderText("Thank you for availing our service!"), "magenta")) 
print("\33[7m-+°\33[0m" * 45)
closing = Figlet(font = "isometric3")
print(colored(closing.renderText("Closing..."), "white"))
print("\U0001F47E" * 45)