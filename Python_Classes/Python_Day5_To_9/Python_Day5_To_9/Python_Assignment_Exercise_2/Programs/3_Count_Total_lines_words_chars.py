# wap to find out total no of lines total no of words total no of characters
# in file

import os
filepath = raw_input(r'Enter file path :')
if os.path.exists(filepath):
    if os.path.isfile(filepath):
        infile = open(filepath,'r')
        data = infile.readlines()
        print(data)
        infile.close()
        total_lines = len(data)
        count_word = 0
        count_char = 0
        for line in data:
            words_in_a_line =len(line.split(' '))
            count_word = count_word + words_in_a_line

        for line in data:
            for word in line.split(' '):
                for char in word:
                    count_char = count_char + 1
            

        print('Total lines = {0} '.format(total_lines))
        print('Total words = {0}'.format(count_word))
        print('Total chars = {0}'.format(count_char))
    else:
        print('Entered path {0} is not a file'.format(filepath))
else:
    print('Entered path {0} does not exists'.format(filepath))
    

