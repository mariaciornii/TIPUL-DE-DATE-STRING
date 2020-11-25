cuv1=str(input('Introduceti primul cuvant: '))
cuv2=str(input('Introduceti al doilea cuvant: '))
cuv3=str(input('Introduceti al treilea cuvant: '))
cuv4=str(input('Introduceti al patrulea cuvant: '))
if len(cuv1)<3 or len(cuv2)<3 or len(cuv3)<3 or len(cuv4)<3:
    print('Nu este respectata conditia')
else:
    cuv_nou = cuv1[0] + cuv1[1]+ cuv2[0] + cuv3[0] + cuv3[1] + cuv3[2]
    for i in range(len(cuv4)//2):
        cuv_nou += cuv4[i]
    print(f'Cuvintele introduse sunt: {cuv1}, {cuv2}, {cuv3}, {cuv4}')
    print('Cuvantul nou este', cuv_nou)
