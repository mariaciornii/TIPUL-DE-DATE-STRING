CNP=str(input('CNP-ul persoanei: '))
if  len(CNP) == 13:
    i = 0
    while (i != len(CNP)) and (ord(CNP[i]) in range(48,59)): 
        i += 1
    if i == len(CNP):
        print('CNP-ul a fost scris corect')
    else:
        print('CNP-ul a fost scris gresit')
else:
    print('CNP-ul a fost scris gresit')