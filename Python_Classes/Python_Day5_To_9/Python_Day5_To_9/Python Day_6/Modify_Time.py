# wap to accept directory name from user and remove if it is modify 30days older
# and if size is 100kb(use fun m10)

import os
import time
import datetime

dirpath = raw_input('Enter directory path: ')

if os.path.exists(dirpath):
    if os.path.isdir(dirpath):
        modify_time = os.path.getmtime(dirpath)
        modify_time_value = datetime.datetime.fromtimestamp(modify_time)
        old_days = datetime.datetime.now() - modify_time_value
        print old_days.days
        if old_days.days > 30 :
            os.remove(dirpath)
            print('directory {0} deleted'.format(dirpath))
    else:
        print('Entered path {0} is not a directory'.format(dirpath))
else:
    print('Entered directory path {0} does not exists'.format(dirpath))
