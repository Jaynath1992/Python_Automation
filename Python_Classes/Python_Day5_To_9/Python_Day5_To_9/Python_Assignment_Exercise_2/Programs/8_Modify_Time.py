# wap to accept directory name from user and remove if it is modify 30days
# older and if size is 100kb(use fun m10)

import os
import datetime

dirpath = raw_input(r'Enter directory path :')

if os.path.exists(dirpath):
    if os.path.isdir(dirpath):
        modify_time = os.path.getmtime(dirpath)
        print(datetime.datetime.fromtimestamp(modify_time))
        datetime.datetime.strftime('')
        if os.path.getsize(dirpath) >= 100 :
            os.remove(dirpath)
    else:
        print('Directory {0} is not a directory'.format(dirpath))
else:
    print('Directory path {0} does not exists'.format(dirpath))
