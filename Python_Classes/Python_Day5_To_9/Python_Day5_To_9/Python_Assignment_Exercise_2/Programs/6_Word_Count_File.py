# Find count of each and every word in file

filepath = r'C:\Users\Jaynath\Desktop\Python_Classes\Python_Assignment_Exercise_2\data.txt'

infile = open(filepath,'r')
data = infile.readlines()

word_count = 0
for line in data:
    for word in line.split(' '):
        word_count+= 1
print word_count
