import argparse
import datetime

# How to run mens.py
parser = argparse.ArgumentParser()
parser.add_argument("Type in your previous mens days separated by coma e.g. 6.12.2018,2.1.2019,27.1.2019,23.2.2019,17.4.2019")
args = parser.parse_args()
print (args)
# Throw Warning if more than 30 days between mens days. The user can doublecheck the input.
