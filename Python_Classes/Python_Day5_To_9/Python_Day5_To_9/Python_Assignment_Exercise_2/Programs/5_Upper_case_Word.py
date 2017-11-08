# wap to convert each n every word in upper case in file

path = r'C:\Users\Jaynath\Desktop\Python_Classes\Python_Assignment_Exercise_2\data.txt'
infile = open(path,'r')
data = infile.readlines()
infile.close()
writefile = open(path,'w')
for line in data:
    writefile.write(line.replace(line,line.upper()))
    #print line.upper()
writefile.close()
        


