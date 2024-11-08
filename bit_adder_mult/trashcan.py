#binary length
def get_bin_len(x):
    bin_len = 0
    n = 0

    while x // 2**n >= 1:
        bin_len += 1
        n += 1
        
    return bin_len

while True:
    x = int(input('x: '))
    if x == 0: break

    print(get_bin_len(x))
    
# alternative to that is:
x = int(input('x: '))
n = x.bit_length()
print(n)