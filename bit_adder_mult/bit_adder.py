a = int(input('a: '))
b = int(input('b: '))

carry_in = 0
carry_out = 0

wynik = '' # jest stringiem dla wygody manipulowania

a_len = a.bit_length()
b_len = b.bit_length()

for i in range(max(a_len, b_len)):
    _a = (a >> i) & 1 # value of bit (from a) nr 'i' looking from right
    _b = (b >> i) & 1 # value of bit (form b) nr 'i' looking from right
    _c = carry_out # c -> carry in
    
    n_a = _a ^ 1 # not(a)
    n_b = _b ^ 1 # not(b)
    n_c = _c ^ 1 # not(c)
    
    sum = (_a & _b & _c)|(n_a & n_b & _c)|(n_a & _b & n_c)|(_a & n_b & n_c)
    carry_out = (_a & _b & _c)|(_a & _b & n_c)|(_a & n_b & _c)|(n_a & _b & _c)
    
    #wynik = (wynik << 1) | sum # wstawia
    wynik = f'{str(sum)}{wynik}'
    
    print(f'\ni: {i}\n_a = {_a}, _b = {_b}, carry in = {_c} \nsum: {sum}, carry_out = {carry_out}, wynik: {wynik}')
    
wynik=f'{str(carry_out)}{wynik}' # dodajemy ostatnie carry out
print(f'\nadded last carry out of {carry_out} and got {wynik}')

print(f'\na = {a} (binary: {bin(a)})')
print(f'b = {b} (binary: {bin(b)})')

print(f'\nSuma (a + b): {int(wynik, 2)} (binary: {wynik})')