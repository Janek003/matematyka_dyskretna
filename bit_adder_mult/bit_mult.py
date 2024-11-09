product = 0

first_input = int(input('\nfirst: '))
second_input = int(input('second: '))

a = max(first_input, second_input)
b = min(first_input, second_input)

print(f'a: {a} = {bin(a)}\nb: {b} = {bin(b)}\n')

m = a.bit_length()
n = b.bit_length()

for i in range(n):
    _b = (b >> i) & 1
    if _b == 1: product += a << i
    print(f'_b:{_b}; product:{bin(product)}')

print(product)