from sys import stdout
from time import sleep
from bs4 import BeautifulSoup
from urllib2 import urlopen
html = '<html><body><div>this is cool <p>one</p><p>two</p><p>three<a>anchor</a></p></div></body></html>'
bs_obj = BeautifulSoup(html, "lxml")
"""def get_text(bso, string_output):
	if bso.name is None:
		string_output+= bso
	else :
		for o in bso.contents:
			try:
				if bso['class'] is 'reply':
					continue
			except:
				print("Oops!",sys.exc_info()[0],"occured.")
        		print("Next entry.")
			string_output = get_text(o, string_output)
	return string_output
	"""


for i in range(0,56):
	continue
	print i