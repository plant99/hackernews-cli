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

class Comment:
	author=''
	time=''
	indent=0
	content_array=[]

def explore_handler(id, comments_depth):
	print id, comments_depth
	html = urlopen("https://news.ycombinator.com/item?id="+ str(id))
	bs_obj = BeautifulSoup(html.read(), "lxml")
	comments = bs_obj.find_all("tr", class_="comtr")
	comments_to_be_printed = []
	for i in range(len(comments)):
		comment = comments[i]
		comment_to_be_printed = Comment()
		indent = int(comment.find("td", class_="ind").find("img")['width'])/40
		username = comment.find("a", class_="hnuser").contents[0]
		age = comment.find("span", class_="age").contents[0].contents[0]
		content_array = comment.find("div", class_="comment").find("span")
		x = get_text(content_array,'')
		print x

def get_text(bso, string_output):
	if bso.name is None:
		string_output+= bso
	else :
		for o in bso.contents:
			if o.name == 'div' and o['class'] == ['reply']:
				break
			string_output = get_text(o, string_output)
	return string_output