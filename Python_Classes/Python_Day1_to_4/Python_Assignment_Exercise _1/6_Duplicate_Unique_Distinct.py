# WAP to find the distinct, duplicate and unique elements in a list

def find_distinct_duplicate_unique_in_list(user_list):
    
    for i in range(len(user_list)):
        count = 1
        for j in range(len(user_list)):
            if i == j:
                continue
            else:
                if user_list[i] == user_list[j]:
                    count = count + 1
        if count >= 2:
            print('%r has %d duplicate elements' %(user_list[i],count))
        elif count == 1:
            print('%r is unique elements' %(user_list[i]))
    
        
                
         







# Making call to above function

user_list = ['Ram',20,30,40,10,20,30,'Jaynath','50','Ram','Mohan',20.45,90.6,30]

find_distinct_duplicate_unique_in_list(user_list)
