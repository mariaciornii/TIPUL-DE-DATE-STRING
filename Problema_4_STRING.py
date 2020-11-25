c1=str(input('Primul cuvant : '))
c2=str(input('Al doilea cuvant: '))
c3=str(input('Al treilea cuvant: '))
c4=str(input('Al patrulea cuvant: '))
if len(c1)<3 or len(c2)<3 or len(c3)<3 or len(c4)<3:
    print('Conditia nu se respecta')
else:
    c_nou = c1[0] + c1[1]+ c2[0] + c3[0] + c3[1] + c3[2]
    for i in range(len(c4)//2):
        c_nou += c4[i]
    print(f'Cuvintele introduse: {c1}, {c2}, {c3}, {c4}')
    print('Cuvantul nou = ', c_nou)