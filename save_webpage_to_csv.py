
### Dan Stober 
### 2018-02-16

### Parses webpage. Result is a CSV listing the states, with populations from
### 2010 Census vs 2000 Census and delta.  Also shown is number of electoral
### and number of representatives for 2010 and 2000 with deltas.
###
### Headers do not line up because some had multi-column "span" and others
### contained line breaks


## NOTE: urllib worked in 2.7, but in 3+, it is split into components
##  one of which is "request"
#import urllib as urllib

from urllib import request 


# Constants for file operations
READ = "r"
WRITE = "w"
APPEND = "a"
READWRITE = "w+"
BINARY = "b"

## Open webpage and save HTML to a local file, then open the local HTML and parse it
## Intermediate step of saving to a local file because urlopen returns the HTML source in binary format

webpage = "https://www.thegreenpapers.com/Census10/HouseAndElectors.phtml"
filename ="data\\apportionment2010.html"


u = request.urlopen ( webpage )
data = u.read()

f = open (filename,WRITE + BINARY)
f.write(data)
f.close()

#HTML Source has been written to a file in the data directory
#Now, open it and parse it to CSV


from html.parser import HTMLParser

# This class was not my original work. Unfortunately, I modified it a few times while trying to
#  learn how it works, so it is not exactly the way it was when I first discovered it, and I no
#  longer remember where I found it.  I'm not trying to plagiarize; I just lost track of my source.
# Sorry

class MyHTMLParser(HTMLParser):

    th_count = 0
    tr_count = 0
    td_count = 0

    th_list = []
    th_lists = []

    td_list = []
    td_lists = []

    th_inside = 0
    td_inside = 0
    tr_inside = 0

    span_list = []
    span_count = 0    
    span_inside = 0

    data_list = []
    data_count = 0    


#    def __init__(self):
#
#        HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        if tag == 'th' :
            self.th_count += 1

            self.th_inside = 1

            
        if tag == 'tr' :
            self.tr_count += 1
            
            self.tr_inside = 1

        if tag == 'td' :
            self.td_count += 1

            self.td_inside = 1


        if tag == 'span' :
            self.span_count += 1

            self.span_inside = 1


    def handle_endtag(self, tag):

        if tag == 'tr' :
            self.tr_inside = 0
            self.th_inside = 0
            self.td_inside = 0

            if len ( self.th_list) > 0:
                #This means that this row has contained TH tags
                self.th_lists.append ( self.th_list )
                self.th_list = []

            if len ( self.td_list) > 0:
                #This means that this row has contained TD tags
                self.td_lists.append ( self.td_list )
                self.td_list = []

        if tag == 'th' :
            self.th_inside = 0

        if tag == 'td' :
            self.td_inside = 0

        if tag == 'span' :
            self.span_inside = 0


    def handle_data(self, data):
        if self.th_inside == 1:
            self.th_list.append ( data.strip() ) 

        elif self.td_inside == 1:
            self.td_list.append ( data.strip() ) 

        elif self.span_inside == 1:
            self.span_list.append ( data.strip() ) 

        else:
            self.data_list.append ( data.strip() ) 
            self.data_count += 1    

parser = MyHTMLParser()

#Reopen same file we saved above -- same variable name, too
#filename ="data\\apportionment2010.html"

myfile = open (filename, mode=READ)

x = myfile.read ()
myfile.close()


parser.feed(x)

#parser.feed (data)

outfile = "data\\apportionment2010.csv"

f = open (outfile,WRITE)

csv_line = ""

for i in range ( 1,len ( parser.td_lists )-2 ):
    for j in range ( len ( parser.td_lists[i] ) ):
        csv_line += "\"" + parser.td_lists [i][j] + "\","

    f.write(csv_line)
    f.write("\n")
    csv_line = ""

f.close()

print ("ALL DONE")

