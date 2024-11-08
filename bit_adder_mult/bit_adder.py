_a = int(input('a: '))
_b = int(input('b: '))

carry_in = 0
carry_out = 0

wynik = '' # jest stringiem dla wygody manipulowania

a_len = _a.bit_length()
b_len = _b.bit_length()

for i in range(max(a_len, b_len)):

    a = (_a >> i) & 1 # value of bit (from a) nr 'i' looking from right
    b = (_b >> i) & 1 # value of bit (form b) nr 'i' looking from right
    c = carry_out # c -> carry in
    
    na = a ^ 1 # not(a)
    nb = b ^ 1 # not(b)
    nc = c ^ 1 # not(c)
    
    sum = (a & b & c)|(na & nb & c)|(na & b & nc)|(a & nb & nc)
    carry_out = (a & b & c)|(a & b & nc)|(a & nb & c)|(na & b & c)
    
    wynik = f'{str(sum)}{wynik}'
    
    #print(f'\ni: {i}\n_a = {_a}, _b = {_b}, carry in = {_c} \nsum: {sum}, carry_out = {carry_out}, wynik: {wynik}')
    
if carry_out == 1: wynik=f'{str(carry_out)}{wynik}' # dodajemy ostatnie carry out
#print(f'\nadded last carry out of {carry_out} and got {wynik}')

#print(f'\na = {a} (binary: {bin(a)})')
#print(f'b = {b} (binary: {bin(b)})')

print(f'\nSuma (a + b): {int(wynik, 2)} (binary: {wynik})')