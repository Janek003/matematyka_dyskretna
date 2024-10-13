import time

def main(n):
    pass#content_here

from_n = int(input('from n: '))
to_n = int(input('to n: '))

for n in range(from_n, to_n+1):
    start_time = time.time()
    
    main(n)
    
    execution_time = time.time() - start_time
    print(execution_time)

print('finished')

input()