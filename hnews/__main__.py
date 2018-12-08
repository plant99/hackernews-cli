import argparse
import requests
import json
import pprint
import textwrap
import bs4
from urllib import urlopen
from bs4 import BeautifulSoup
import jobs
import news
import ask
import explore
#parser setup
def maingl():
	stopped = False
	base_url = "http://news.ycombinator.com"
	parser = argparse.ArgumentParser()
	parser.add_argument("type_of_dq", type=str,choices=['news','ask','jobs','explore']) # dq->data query
	parser.add_argument("-l", "--limit", type=int, help="number of posts you want to query, MAX_VAL={news:200, ask:50,poll:50}, DEFAULT={[news,ask,poll]:50}") 
	parser.add_argument("-r", "--range", type=str, help="range of posts you want in the output of the form (MIN_INDEX-MAX_INDEX)") 
	parser.add_argument("-c", "--comments_depth", type=int, help="Used with <EXPLORE>, integer input to denote the depth of comments one will go, DEFAULT=1, use -1 to display all available comments") 
	parser.add_argument("-i", "--id", type=int, help="Compulsory for <EXPLORE>, Id of the item, beside the title for each displayed item") 
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
			start=int(range_params[0])

	if dq == "news":
		news.news_handler(start, number_of_posts)
	elif dq == 'ask':
		ask.ask_handler(start, number_of_posts)
	elif dq == 'jobs':
		jobs.jobs_handler(start, start+number_of_posts)
	elif dq == 'explore':
		if(args.id):
			#call function
			if(args.comments_depth):
				comments_depth = args.comments_depth
			else:
				comments_depth = 1000
			explore.explore_handler(args.id, comments_depth)
		else:
			print "Pass an integer with -i (or) --id"