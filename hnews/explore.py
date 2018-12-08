#class colors https://gist.github.com/vratiu/9780109
import sys
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

#Supposed to store the comments as objects in lists, but printing them directly would be more efficient
"""
class Comment:
	author=''
	time=''
	indent=0
	content_array=[]
"""
def explore_handler(id, comments_depth):
	html = urlopen("https://news.ycombinator.com/item?id="+ str(id))
	bs_obj = BeautifulSoup(html.read(), "lxml")
	comments = bs_obj.find_all("tr", class_="comtr")
	comments_to_be_printed = []
	story = bs_obj.find("a", class_="storylink")
	title = story.text
	url = story['href']
	author = bs_obj.find("a", class_="hnuser").text
	score = bs_obj.find("span", class_="score").text
	time = bs_obj.find("span", class_="age").text
	print("+----------------------------------------------------------+")
	print_modified(title, 'yellow')
	print_modified('ID: '+str(id), "okblue")
	print("+----------------------------------------------------------+")
	print ''
	print bcolors.CYAN + url + bcolors.ENDC
	print ''
	print bcolors.GREY_BACK_WHITE_P + ' Author:' + author + " Score:" + score + " Created:" + time + bcolors.ENDC
	print ""
	print bcolors.HEADER + "COMMENTS:" + bcolors.ENDC
	count = 0
	for i in range(len(comments)):
		comment = comments[i]
		indent = int(comment.find("td", class_="ind").find("img")['width'])/40
		username = comment.find("a", class_="hnuser").contents[0]
		age = comment.find("span", class_="age").contents[0].contents[0]
		content_array = comment.find("div", class_="comment").find("span")
		x = get_text(content_array,'')
		if(indent < comments_depth):
			count+=1
			print_comment_modified(x, indent, username, age)
		if(count%4 == 0 and count!=0):
			x = raw_input("PROMPT:Press q+ENTER to exit, and ENTER to continue!")
			count+=1
			globals.delete_line()
			if(x == 'q'):
				print 'Bye'
				break
		#print x

def get_text(bso, string_output):
	if bso.name is None:
		string_output+= bso
	else :
		for o in bso.contents:
			if o.name == 'div' and o['class'] == ['reply']:
				break
			string_output = get_text(o, string_output)
	return string_output

def print_comment_modified(string, indent, username, age):
	print +4*indent*' ' + '->' +bcolors.GREY_BACK_WHITE_P + "Author: "+ username +"Age: "+ age + bcolors.ENDC
	sentences_wrapped = textwrap.wrap(string, 80-indent*4, break_long_words=1)
	for sentence in sentences_wrapped:
		sentence = 4*indent*' '+ sentence
		print sentence

	print ""

