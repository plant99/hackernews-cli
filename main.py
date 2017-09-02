import argparse
import requests
import json
import pprint
import textwrap
import bs4
from urllib import urlopen
from bs4 import BeautifulSoup

#class colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#functions
def news_handler(start, count):
	html = urlopen(base_url+'/news')
	bs_obj = BeautifulSoup(html.read(), "lxml")
	news_chipped = bs_obj.find_all("tr",class_="athing")
	for i in range(len(news_chipped)):
		single_news = news_chipped[i]
		id_single_news = single_news['id']
		dataset1 = single_news.find_all("td", class_="title")[1].find("a")
		if(dataset1.has_attr('rel')):
			continue #Job Advertisements
		title = dataset1.contents[0]
		link = dataset1['href']
		
		#checking if it is Ask HN
		if not title.find("Ask HN:"):
			continue
		print title, link
		dataset2_block = single_news.next_sibling.find("td", class_="subtext")
	 	score = dataset2_block.find("span", class_="score").contents[0].split(' ')[0]
	 	print score
	 	author = dataset2_block.find("a",class_="hnuser").contents[0]
	 	time = dataset2_block.find("span",class_="age").contents[0].contents[0]
	 	print author, time

#parser setup
base_url = "http://news.ycombinator.com"
parser = argparse.ArgumentParser()
parser.add_argument("type_of_dq", type=str,choices=['news','ask','poll']) # dq->data query
parser.add_argument("-l", "--limit", type=int, help="number of posts you want to query, MAX_VAL={news:200, ask:50,poll:50}, DEFAULT={[news,ask,poll]:50}") 
parser.add_argument("-r", "--range", type=str, help="range of posts you want in the output of the form (MIN_INDEX-MAX_INDEX)") 
args = parser.parse_args()

#variable declaration
number_of_posts = 0
start = 0
dq = args.type_of_dq 

#number of posts assignment
if not (args.limit or args.range):
	number_of_posts = 20
else:
	if args.limit:
		number_of_posts = args.limit
	elif args.range:
		range_params = args.range.split('-')
		number_of_posts = int(range_params[1])-int(range_params[0])
		start=range_params[0]

if dq == "news":
	news_handler(start, number_of_posts)
elif dq == 'ask':
	ask_handler(start, number_of_posts)
elif dq == 'poll':
	poll_handler(start, number_of_posts)
