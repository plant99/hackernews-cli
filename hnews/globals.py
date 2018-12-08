import sys

import textwrap
base_url = "http://news.ycombinator.com"

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'
    PURPLE = '\033[35m'
    GREY_BACK_WHITE_P = '\033[100m'
    YELLOW = '\033[93m'

def print_modified(sentence, color):
	sentence_wrapped = textwrap.wrap(sentence, 50, break_long_words=1)
	length_sr = len(sentence_wrapped)
	for i in range(length_sr):
		line_tbp = '' #to_be_printed
		line_tbp+= '|'
		line_tbp+= ' '*3
		line_tbp+= sentence_wrapped[i]
		line_tbp+= ' '*(55-len(sentence_wrapped[i]))
		line_tbp+= '|'
		if color is 'green':
			print  bcolors.OKGREEN +line_tbp+ bcolors.ENDC 
		elif color is 'blue':
			print  bcolors.HEADER +line_tbp+ bcolors.ENDC 
		elif color is 'red':
			print  bcolors.FAIL +line_tbp+ bcolors.ENDC 
		elif color is 'cyan':
			print  bcolors.CYAN +line_tbp+ bcolors.ENDC 
		elif color is 'purple':
			print  bcolors.PURPLE +line_tbp+ bcolors.ENDC 
		elif color is 'yellow':
			print  bcolors.YELLOW +line_tbp+ bcolors.ENDC 	
		elif color is 'okblue':
			print bcolors.OKBLUE + line_tbp + bcolors.ENDC

def delete_line():
	sys.stdout.write(CURSOR_UP_ONE)
	sys.stdout.write(ERASE_LINE)