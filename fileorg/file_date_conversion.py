# ------------------------------------------------------------------------
# Page 240 of ATBS
# Project: Renaming Files with American Style Dates
# to European Style Dates
#
# Problem Statement:
# 
# Say your boss emails you thousands of files with American-style dates
# (MM-DD-Y Y Y Y) in their names and needs them renamed to European st-
# yle dates (DD-MM-Y Y Y Y). This boring task could take all day to do 
# by hand! Let’s write a program to do it instead.
# ------------------------------------------------------------------------

import re
import os
import shutil

# Colours to be used in printing.
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Confirm that the user wants to do this:
print(WARNING + f'Are you sure that you want to convert dates in filenames of all filenames in {os.getcwd()}? (y/n)' + ENDC)
confirmation = input()

if confirmation not in 'yY':
	quit()

print('======================== Beginning search... ======================== ')

# - Search all filenames in the cwd for MM-DD-YYYY dates. ----------------

# Create a regular expression.
datePattern = re.compile(r"""^(.*?)
	((0|1)?\d)-
	((0|1|2|3)?\d)-
	((19|20)\d\d)
	(.*?)$
	""", re.VERBOSE)

# Store filenames with MM-DD-YYYY dates in a list.
matches = []

# Use os.listdir() to find all files in cwd.
for file in os.listdir('.'):
	# Use the regex to check if each file has a date.
	match = datePattern.search(file)
	print("{:<25}".format(file), end='')
	# Skip files without a date.
	if match == None:
		print(FAIL + 'Not a match.' + ENDC)
		continue

	# Find the different components of the filename.
	priorText = match.group(1)
	month 	  = match.group(2)
	day		  = match.group(4)
	year      = match.group(6)
	after     = match.group(8)

	# Form the new filename.
	euroFilename = priorText + day + '-' + month + '-' + year + after

	# Get absolute paths.
	absoluteCwd = os.path.abspath('.')
	amerFilename = os.path.join(absoluteCwd, file)
	euroFilename = os.path.join(absoluteCwd, euroFilename)

	# Rename the files.
	print(OKGREEN + f'Renaming to "{euroFilename}".' + ENDC)
	#shutil.move(amerFilename, euroFilename)