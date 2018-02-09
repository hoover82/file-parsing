
### This can parse the CSV

import csv

## Constants defined for file operations
READ = "r"
WRITE = "w"
APPEND = "a"
READWRITE = "w+"
BINARY = "b"

#Data came from https://github.com/justmarkham/pandas-videos 
filename = "c:\\dan\\how_to\\python\\data\\ufo.csv"

column0 = []
column1 = []
column2 = []
column3 = []
column4 = []

with open( filename ,READ ) as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')
 
#    fields_count = len ( list( readCSV)[1])
 
	# skip the first row -- contains headers
    next (readCSV)   
	
    for row in readCSV:

		#Each subscrpted position in "row" is the next delimited field, numbered 0 to 4
        column0.append ( row [0])
        column1.append ( row [1])
        column2.append ( row [2])
        column3.append ( row [3])
        column4.append ( row [4])

#print ( fields_count )

print ( column0 )		
print ( column1 )		
print ( column2 )		
print ( column3 )		
print ( column4 )		
