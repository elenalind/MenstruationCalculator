import argparse
import time
from datetime import datetime, timedelta

# How to run mens.py
parser = argparse.ArgumentParser()
parser.add_argument("list", help="Type in your previous mens days separated by coma e.g. 6.12.2018,2.1.2019,27.1.2019,23.2.2019,20.3.2019,17.4.2019,11.5.2019,5.6.2019,3.7.2019,30.7.2019", type=str)
args = parser.parse_args()

print ("Your dates", args.list)

argssplit= args.list.split(",")

print ("Your cycle lengths are:")
sum_days = 0 
for item, next_item in zip(argssplit, argssplit[1:]):
    cyclelength = ((datetime.strptime(next_item, '%d.%m.%Y'))-(datetime.strptime(item, '%d.%m.%Y'))).days
    sum_days = sum_days + cyclelength
    print (cyclelength)

print ("Your average cycle length is:", int(sum_days / (len(argssplit) - 1)))

last_mens = datetime.strptime(argssplit[len(argssplit)-1], '%d.%m.%Y')
next_mens = last_mens + timedelta(days=cyclelength)
print ("Your next menstrutation will probably be on:", next_mens)
next_next_mens = next_mens + timedelta(days=cyclelength)
print ("Your second next menstrutation will probably be on:", next_next_mens)


# Throw Warning if more than 30 days between mens days. The user can doublecheck the input.
# Calculate even the next next mens
