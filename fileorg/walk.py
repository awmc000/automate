import os

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

for folderName, subfolders, filenames in os.walk('/home/alex/Documents'):
	print(UNDERLINE + 'The current folder is ' + folderName + ENDC)

	for subfolder in subfolders:
		print(OKCYAN + 'Subfolder of ' + folderName + ': ' + subfolder + ENDC)

	for filename in filenames:
		print(OKGREEN + 'File in ' + folderName + ': ' + filename + ENDC)

	# newline
	print('')