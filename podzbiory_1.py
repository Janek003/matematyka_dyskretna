# Napisz program, który dla zadanej liczy naturalnej n wypisze wszystkie podzbiory zbioru {1, 2, . . . , n}.

# picking number that is of length of N and goes through combinations of off and on for every number
# basicly i need to count up in binary to the highest number (in binary) with number of bits being equal to N

# part that calculates what number to count to?
# part that adds to another list, a list of elements that were chosen by binary number

# it needs to go through all digits from whichever side of binary number and track the digit
# if the digit is 0 then go to next, if the digit is 1 save digit number into a list and go to next, also if the "digit" is 'b' then end proces and do next steps
# then we have a list with all digits that are indexes of numbers that we must use in a podzbior, we append a list by those and append a metalist with that list, then repeat for next binary number

# kontynuujemy loop tak długo aż len(str(binary_counter))-2 nie będzie większa od n
import time
print("Zestaw 1, zadanie 13")
print("Napisz program, który dla zadanej liczy naturalnej n wypisze wszystkie podzbiory zbioru {1, 2, . . . , n}.")
print("time complexity O(2^n)")

def generate_podzbior(binary_number):
    list_of_indexes = []
    podzbior = []
    str_binary_number = bin(binary_number)[2:].zfill(n)
    for i in range(len(str_binary_number)):
        if int(str_binary_number[i]) == 1:
            list_of_indexes.append(i)
    for index in list_of_indexes:
        to_be_appended = list_elementy_zbioru[index]
        podzbior.append(to_be_appended)
    return podzbior

def generate_number_to_count_to():
    result = 0
    for i in range(n):
        result += 2**i
    return(result)

def generate_zbior_podzbiorow():
    for non_binary_int in range(generate_number_to_count_to()+1):
        generate_podzbior(non_binary_int)

n = int(input('Enter a value for n: '))

list_elementy_zbioru = []
for i in range(1, n+1):
    list_elementy_zbioru.append(i)

print(f"wszystkie podzbiory zbioru {list_elementy_zbioru}: ", )

start_time = time.time()
generate_zbior_podzbiorow()
print("--- %s seconds ---" % (time.time() - start_time))

input()