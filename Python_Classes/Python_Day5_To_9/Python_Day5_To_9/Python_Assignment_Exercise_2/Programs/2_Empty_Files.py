# 2) wap to accept directory name from user and remove all the empty files, from that directory. (os.path.getsize)

import os
dirpath = raw_input(r'Enter directory path : ')

if os.path.exists(dirpath):
    if os.path.isdir(dirpath):
        allfiles = os.listdir(dirpath)
        for eachfile in allfiles:
            filepath = os.path.join(dirpath,eachfile)
            if os.path.isfile(eachfile):
                sizeoffile = os.path.getsize(filepath)
                if sizeoffile == 0 :
                    os.remove(filepath)
                    print('File {0} removed'.format(eachfile))
    else:
        print('Entered dirpath {0} is not a directory'.format(dirpath))
else:
    print('Entered dirpath {0} does not exists'.format(dirpath))
    
