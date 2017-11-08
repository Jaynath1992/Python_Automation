# Wap to find out count of all the python files in any specific directory
# and subdirectory

import os
dirpath = r'C:\Users\Jaynath\Desktop\Python_Classes\Python_Assignment_Exercise_2'

for root,dirs,files in os.walk(dirpath):
    print root
    print files
    print dirs
