# wap to convert the content of files in reverse order

path = r'C:\Users\Jaynath\Desktop\Python_Classes\Python_Assignment_Exercise_2\data.txt'
infile = open(path,'r')
data = infile.read()
infile.close()

reverse_data = data[::-1]
print(reverse_data)
