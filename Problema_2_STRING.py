s=str(input('Sirul: '))
m=0
c=0
csp=0
for i in s:
    if ord(i) in range(65,91):
        m+=1
    if ord(i) in range(48,58):
        c+=1
    if ord(i) in range(32,48) or ord(i) in range(58,65) or ord(i) in range(91,97) or ord(i) in range(123,127):
        csp+=1
print('Majuscule in sir:', m)
print('Cifre in sir:', c)
print('Caractere speciale in sir:', csp)
