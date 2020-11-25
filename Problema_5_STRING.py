cnp=str(input('CNP-ul: '))
if  len(cnp) == 13:
    i = 0
    while (i != len(cnp)) and (ord(cnp[i]) in range(48,59)): 
        i += 1
    if i == len(cnp):
        print('Ati scris CNP-ul corect')
    else:
        print('Ati scris CNP-ul gresit')
else:
    print('Ati scris CNP-ul gresit')
