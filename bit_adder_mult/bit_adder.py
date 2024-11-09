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
    c = carry_out # c inaczej carry in
    
    sum = (a ^ b) ^ c
    carry_out = (a & b) | ((a ^ b) & c)
    
    wynik = str(sum) + wynik
    
if carry_out == 1: wynik=str(carry_out)+wynik # dodajemy ostatnie carry out

print(f'\nSuma (a + b): {int(wynik, 2)} (binary: {wynik})')