# Napisz program, który dla zadanej liczby naturalnej n oraz liczy k ∈ {1, . . . , n} wypisze
# wszystkie podzbiory k-elementowe zbiory {1, . . . , n}.

def generate_podzbior(binary_number):
    
    list_of_indexes = []
    podzbior = []
    
    nr_of_1s = 0
    
    str_binary_number = bin(binary_number)[2:].zfill(n)
    
    for i in range(len(str_binary_number)):
        if int(str_binary_number[i]) == 1:
            nr_of_1s += 1
            list_of_indexes.append(i)
    
    if nr_of_1s != k:
        return False

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
    zbior_podzbiorow = []
    for non_binary_int in range(generate_number_to_count_to()+1):
        if generate_podzbior(non_binary_int): zbior_podzbiorow.append(generate_podzbior(non_binary_int))
    return zbior_podzbiorow
    

n = int(input('Enter a value for n: '))
k = int(input('Enter a value for k: '))

list_elementy_zbioru = []
for i in range(1, n+1):
    list_elementy_zbioru.append(i)

print("zbior analizowany: ", list_elementy_zbioru)
print(f"zbior poteg o {k} elementach {generate_zbior_podzbiorow()}")
input()