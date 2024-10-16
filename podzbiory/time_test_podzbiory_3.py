
import time

def main(n):
    
    numbers = []

    for i in range(1, n+1):
        numbers.append(i)

    curr_permutation = []
    for i in range(n):
        curr_permutation.append(0)

    def permute(index, curr_permutation):
        for item in numbers:
            if item not in curr_permutation:
                curr_permutation[index] = item
                if permute(index+1, curr_permutation):
                    curr_permutation[index] = 0

        return True

    permute(0, curr_permutation)


from_n = int(input('from n: '))
to_n = int(input('to n: '))

for n in range(from_n, to_n+1):
    start_time = time.time()
    
    main(n)
    
    execution_time = time.time() - start_time
    print(execution_time)

print('finished')

input()