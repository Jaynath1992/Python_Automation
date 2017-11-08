# Wap to accept a file name and directory name from user and create a backup of this file in same directory

import os
import shutil
dirpath = raw_input(r'Ente rdirectory path :')
filename = raw_input(r'Enter file name :')

if os.path.exists(dirpath):
    if os.path.isdir(dirpath):
        filepath = os.path.join(dirpath,filename)
        if os.path.exists(filepath):
            if os.path.isfile(filepath):
                # create backup of that file by reading lines of that file into other
                backup_file = dirpath + '\\' + 'backup_file' + '.txt'
                if os.path.exists(backup_file):
                    os.remove(backup_file)  # First remove that old backup existing file
                    shutil.copy(filepath,backup_file)
                    print('Back up file of {0} is {1} created successfully'.format(filepath,backup_file))
                else:
                    readfile = open(filepath,'r')       # Here we can use shutil.copy() or as mentioned below
                    readdata = readfile.read()
                    readfile.close()
                    writefile = open(backup_file,'w')
                    writefile.write(readdata)
                    writefile.close()
                    print('Back up file of {0} is {1} created successfully'.format(filepath,backup_file))
            else:
                print('Entered file {0} is not a file'.format(filepath))
        else:
            print('File path {0} does not exists'.format(filepath))
    else:
        print('Entered path {0} is not a directory'.format(dirpath))        
    
else:
    print('Entered directory path {0} does not exists'.format(dirpath))
    
