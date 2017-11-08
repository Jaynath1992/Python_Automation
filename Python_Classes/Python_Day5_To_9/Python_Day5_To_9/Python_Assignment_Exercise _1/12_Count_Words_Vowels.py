# 12)	WAP to get the count of words in the statement string and the
# count of vowels in complete statement.

def Get_Count_Words_Vowels(string):
    count = len(string.split(' '))
    print 'No of words in statement is = %d'%(count)
    for char in string:
        if char == 'a' or char=='e' or char=='i' or char=='o' or char=='u' or char == 'A' or char=='E' or char=='I' or char=='O' or char=='U':
            print char,
        


# Making call to above function

string = raw_input('Enter Statement : ')
Get_Count_Words_Vowels(string)
