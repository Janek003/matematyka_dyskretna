import time
def time_test(number_used_as_n):
    n = number_used_as_n
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

    list_elementy_zbioru = []
    for i in range(1, n+1):
        list_elementy_zbioru.append(i)

    start_time = time.time()
    generate_zbior_podzbiorow()
    execution_time = time.time() - start_time

    print(execution_time)

highest_n = int(input('Highest n tested: '))
for i in range(10,highest_n+1):
    time_test(i)

print('finished')

input()