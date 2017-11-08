infile = open(r'C:\Users\Jaynath\Desktop\Python_Classes\Python Day_6\file1.csv','r')

'''
for line in infile.readlines():
    columns=line.split('\t')
    if columns[2]=='IT\n':
        print columns[1]
 '''

for line in infile:
    line=line.strip()
    columns=line.split(',')
    if columns[0] == 'ID':
        continue
    if columns[2] == 'IT':
        print columns[1]






































