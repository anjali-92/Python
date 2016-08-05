'''

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''

import sys
Name = raw_input("Enter your name   :")
Age = int(raw_input("Enter your age   :"))
CelebrateThisYear = raw_input("Did u celebrate your birthday this year   :")
if CelebrateThisYear not in ['Y','Yes','YES']:
	Age = Age + 1
if Age<=0:
    sys.exit(1)
from datetime import date
Year = date.today().year

RemainingAge = 100 - Age

year = Year + RemainingAge
print "You will turn 100 in year " + str(year)


#Extras 1
Times = int(raw_input("Enter a number   :"))
#Extras 2
print (("\nYou will turn 100 in year  "  + str(year)) * Times)


