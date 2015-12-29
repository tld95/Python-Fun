from datetime import datetime
import re

document_found = False

while(True):
	document_name = str(raw_input("Enter document name: "))	
	try:
		document = open(document_name, 'r')
		break
	except:
		print "Document not found."

document_text = document.read()
print "Searching: %s" % (document_name)
continue_exit = "c"

while(continue_exit == "c"):
	keyword = str(raw_input("\nEnter a keyword: "))
	date = datetime.now()
	date = str(date.month) + "/" + str(date.day) + "/" + str(date.year)
	keyword_count = len(re.findall(keyword,document_text))
	print "The word count of your keyword is: %s" % (keyword_count)
	continue_exit = str(raw_input("Enter 'c' to continue searching, or any other key to exit: "))

	

