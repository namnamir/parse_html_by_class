#for parsing HTML files 
from BeautifulSoup import BeautifulSoup
#for json files
import simplejson
#for going 
import os

# for the unicode stuff
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# opening the json file
with open('json_file.json', 'rb') as json_input:
	json = simplejson.load(json_input)

k = 0 #for counting the number of files
l = 0 #for counting the number of elements

# go through all .htm or .html files in the folder
for files in os.listdir(os.getcwd()):
	if files[-4:] != ".htm" and files[-5:] != ".html":
		continue
	k += 1
	inputf = open(files, "r")
	print "=========> I am working on {} <=========".format(files)
	try:
		#read more: https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html
		input_soup = BeautifulSoup (inputf.read())
		#here the classes goes. In each of the following it says that it should find a specific class of <span> tag
    Titles = input_soup.findAll("span", {"class":"artTitle ng-binding"})
		ASCII  = input_soup.findAll("span", {"class":"artWork ng-binding"})
		Tags   = input_soup.findAll("span", {"class":"artCategory ng-binding"})
		l += len(Titles)
		#writing into json file
    for i in range(0, len(Titles)):
	 		json.append({"Title":str(Titles[i].contents[0]),
	 					 "Quote":str(ASCII[i].contents[0]),
						 "Type": "ASCII",
						 "Source": "1 Line Art",
						 "Author": None,
						 "Tag": str(Tags[i].contents[0]),
						 "Language": None,
						})
	except IOError:
		#If the file cannot be opened.
		print "\nThe \033[38;5;23mfile\033[0m is not readable; make sure if it is there."
	except KeyboardInterrupt:
		print "\nYou cancelled the operation."
	except Exception, e:
		print "\nAn error occured:",e
	finally:
		
		with open('json.txt', 'w') as json_outfile:  
			simplejson.dump(json, json_outfile)
		json_outfile.close()
print "=====> Done <====="
print "{} ASCII artworks in {} files are prased".format(l,k)
