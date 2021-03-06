#class colors https://gist.github.com/vratiu/9780109
import argparse
import requests
import json
import pprint
import textwrap
import bs4
from urllib import urlopen
from bs4 import BeautifulSoup
import globals
base_url = globals.base_url
bcolors = globals.bcolors
print_modified = globals.print_modified


stopped = False
def print_box_ask(index, title, url, author, time, score, id):
	#print index,title,url,author,time,score
	print "+--------+"
	print bcolors.OKGREEN + "|"+"S.No:"+ str(index) + ' '*(3-len(str(index))) + '|' + bcolors.ENDC
	print("+--------+-------------------------------------------------+")
	print_modified(title, 'yellow')
	print_modified('ID: '+str(id), "okblue")
	print("+----------------------------------------------------------+")
	print bcolors.CYAN + url + bcolors.ENDC
	print ''
	print bcolors.GREY_BACK_WHITE_P + ' Author:' + author + " Score:" + score + " Created:" + time + bcolors.ENDC
	print "--------------------------------------------------------------------------------"


#ask handlers
def ask_handler(start, count):
	page_indices=[0]
	page_indices=range(start//30+1,start//30+(start+count)//30+2)
	print_pages_ask(page_indices,start,start+count)

def print_pages_ask(page_indices, start, end):
	count=(page_indices[0]-1)*30
	index = 1
	for j in range(len(page_indices)):
		result = []
		result_dum = print_page_ask(page_indices[j],count,start,end,index)
		result = list(result_dum)
		count = result[0]
		index = result[1]
		if count >= end:
			break
		

def print_page_ask(page_index,count,start,end, index):
	print "Request sent..."
	html = urlopen(base_url+'/ask?p='+str(page_index))
	print "Recieved, parsing..."
	bs_obj = BeautifulSoup(html.read(), "lxml")
	ask_chipped = bs_obj.find_all("tr",class_="athing")
	for i in range(len(ask_chipped)):
		count+=1
		if count>start and count<=end: 
			single_ask = ask_chipped[i]
			id_single_ask= single_ask['id']
			dataset1 = single_ask.find_all("td", class_="title")[1].find("a")
			title = dataset1.contents[0]
			link = 'http://news.ycombinator.com/ask?p='+dataset1['href']

			dataset2_block = single_ask.next_sibling.find("td", class_="subtext")
		 	score = dataset2_block.find("span", class_="score").contents[0].split(' ')[0]
		 	author = dataset2_block.find("a",class_="hnuser").contents[0]
		 	time = dataset2_block.find("span",class_="age").contents[0].contents[0]
			print_box_ask(index, title, link, author, time, score, id_single_ask)

		 	index+=1

		 	#prompt at every 4 items
			if (index%4 is 0):
			 	print bcolors.FAIL + "PROMPT:If you want to continue press ENTER else press q+ENTER to exit" + bcolors.ENDC
				x = raw_input()
				globals.delete_line()
				globals.delete_line()
				if x is 'q':
					print "Bye!"
					global stopped
					stopped=True
					break

	return count,index



