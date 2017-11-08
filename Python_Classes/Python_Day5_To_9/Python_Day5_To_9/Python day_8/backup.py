import sys

try:
    infile = raw_input('Enter the filename : ')
    outfile = raw_input('Enter the backup file name : ')
    infile1 = open(infile,'r')
    outfile1 = open(outfile,'w')
    outfile1.write(infile1.read())
    outfile1.write('This is one more line')

except IOError:
    print 'Error: ',sys.exc_info()[1]
finally:
    if 'outfile1' in globals():
        outfile1.close()
try:
    a = 10
    print a
except Exception as e:
    print e
else:
    print('Got error')
finally:
    print 'all block executed successfully'
