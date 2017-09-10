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
def print_box_jobs(index, title, url, time, id):
	#print index,title,url,author,time,score
	print "+--------+"
	print bcolors.OKGREEN + "|"+"S.No:"+ str(index) + ' '*(3-len(str(index))) + '|' + bcolors.ENDC
	print("+--------+-------------------------------------------------+")
	print_modified(title, 'yellow')
	print("+----------------------------------------------------------+")
	print bcolors.CYAN + url + bcolors.ENDC
	print ''
	print bcolors.GREY_BACK_WHITE_P + " Created:" + time + bcolors.ENDC
	print "--------------------------------------------------------------------------------"

#jobs handler
def jobs_handler(start, end):
	print 'Request sent...'
	r = requests.get('https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty')
	print 'Request recieved'

	count=0
	index=0
	last_id=0
	last_id = r.json()[0]
	while count<= end :
		result = print_page_jobs(last_id, index, count, start, end)
		last_id = result[0]
		index = result[1]
		count = result[2]

	
#printing page 

def print_page_jobs(last_id, index, count, start, end):
	print 'Request sent...'
	html = urlopen(base_url+'/jobs?next='+str(last_id))
	print 'Request recieved'
	bs_obj = BeautifulSoup(html.read(), "lxml")
	job_ads_chipped=bs_obj.find_all("tr", class_="athing")
	for i in range(len(job_ads_chipped)):
		count+=1
		if count <= end and count>= start:
			index +=1
			if index%5 is 0 and index != 0:
				print bcolors.FAIL + "PROMPT:If you want to continue press ENTER else press q+ENTER to exit" + bcolors.ENDC
				x = raw_input()
				globals.delete_line()
				globals.delete_line()
				if x is 'q':
					print "Bye!"
					global stopped
					stopped=True
					break
			job_ad = job_ads_chipped[i]
			last_id = job_ad['id']
			dataset1 = job_ad.findAll("td", class_="title")[1].find("a")
			title = dataset1.contents[0]
			url = dataset1['href']
			dataset2 = job_ad.next_sibling.find("td", class_="subtext").find("span").find("a").contents[0]
			time = dataset2
			print_box_jobs(index, title, url, time, last_id)



	return last_id, index,count