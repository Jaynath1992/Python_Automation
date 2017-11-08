import os

indir = raw_input(r'Enter directory path : ')

if os.path.isdir(indir):
    allfiles = os.listdir(indir)
    for f in allfiles:
        path = indir + '\\'+ f
        if os.path.isfile(path):
            s = os.path.getsize(path)
            if s==0:
                os.remove(path)
                print 'deleted file is : ',f
        
