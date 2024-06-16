import csv
""" 
this read funtion return whole csv file content 

with open("example.csv","r") as csv_file:
    print(csv_file.read())

"""

with open("example.csv", "r") as csv_file:
    """ return as a list """
    csv_reader = csv.reader(csv_file)
    """ to escape the first header row use next(csv_reader) """
    next(csv_reader)
    for row in csv_reader:
        print(row)


