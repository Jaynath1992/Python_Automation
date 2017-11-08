# WAP to create a DS of students (define DS as per the protocols) and
# print the sum of scores in five subjects and gets the each student percentage

students = {'Jaynath':{'Math':95,'Physics':80,'Chemistry':87,'Hindi':80,'English':82},
            'Mohan':{'Math':90,'Physics':70,'Chemistry':67,'Hindi':85,'English':85},
            'Rajesh':{'Math':80,'Physics':75,'Chemistry':65,'Hindi':55,'English':95},
            'Shreya':{'Math':70,'Physics':79,'Chemistry':62,'Hindi':82,'English':65},
            'Shristi':{'Math':95,'Physics':60,'Chemistry':77,'Hindi':55,'English':76}
            }

for key in students:

    print ('Average marks of student : %s ='%(key))
    print str(( students[key]['Math'] + students[key]['Physics'] + students[key]['Chemistry']
        + students[key]['Hindi'] + students[key]['English'])/float(len(students[key])))+'%'

 
