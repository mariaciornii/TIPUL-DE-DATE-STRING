sir=str(input('Sir: '))
maj=0
cif=0
cr_sp=0
for i in sir:
    if ord(i) in range(65,91):
        maj+=1
    if ord(i) in range(48,58):
        cif+=1
    if ord(i) in range(32,48) or ord(i) in range(58,65) or ord(i) in range(91,97) or ord(i) in range(123,127):
        cr_sp+=1
print(f'a) Numarul de majuscule in sir: {maj}')
print(f'b) Numarul de cifre in sir: {cif}')
print(f'c) Numarul de caractere speciale in sir: {cr_sp}')