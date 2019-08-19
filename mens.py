import argparse
from datetime import datetime

# How to run mens.py
parser = argparse.ArgumentParser()
parser.add_argument("list", help="Type in your previous mens days separated by coma e.g. 6.12.2018,2.1.2019,27.1.2019,23.2.2019,17.4.2019", type=str)
#parser.add_argument("date", help="Type in the date of your last mentruation and the menstrual cycle lenght, separated by coma e.g. 23.2.2019,26")
args = parser.parse_args()

print ("Your dates", args.list)

argssplit= args.list.split(",")

for item, next_item in zip(argssplit, argssplit[1:]):
    print (abs((datetime.strptime(item, '%d.%m.%Y'))-(datetime.strptime(next_item, '%d.%m.%Y'))).days)

# Throw Warning if more than 30 days between mens days. The user can doublecheck the input.
# Throw Warning if for option two, the period lenght is too long, >30 days

