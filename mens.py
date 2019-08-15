import argparse
import datetime
import re

# How to run mens.py
parser = argparse.ArgumentParser()
parser.add_argument("list", help="Type in your previous mens days separated by coma e.g. 6.12.2018,2.1.2019,27.1.2019,23.2.2019,17.4.2019")
#parser.add_argument("date", help="Type in the date of your last mentruation and the menstrual cycle lenght, separated by coma e.g. 23.2.2019,26")
args = parser.parse_args()

# print (args.list)

re.split("\,", args)

#for element in argssplit:
#    print(element)

#args.split(",", s)


# Throw Warning if more than 30 days between mens days. The user can doublecheck the input.
# Throw Warning if for option two, the period lenght is too long, >30 days
