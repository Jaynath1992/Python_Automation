# Wap to read csv file which contain following columns
# emp id, emp name, empsal, empdept

filepath = r'C:\Users\Jaynath\Desktop\Python_Classes\Python_Assignment_Exercise_2\csvfile.csv'

infile = open(filepath,'r')
data = infile.readlines()

for line in data:
    print line
