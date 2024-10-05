# wybieramy na pierwsze miejsce opcje > wybieramy na drugie z pozostałych > wybieramy na trzecie ostatnią opcje
# cofamy się o krok do tyłu czyli znowu wybieramy na drugą pozycję za każdym razem oznaczając że opcja została wykorzystana
# pierwsze wybrane > drugie jedyne pozostałe > trzecie jedyne pozostałe
# cofamy się znowu o krok resetując przy tym wykorzystane dla kroku drugiego
# oznaczamy to wybrane na pierwszej pozycji jako tam wykorzystane 
# wybieramy następne dla pierwszego > wybieramy na drugie z pozostałych > wybieramy na trzecie ostatnią opcje
# cofamy się do opcji drugiej

numbers = []

n = int(input('n: '))
for i in range(1, n+1):
    numbers.append(i)

permutations = []

print(f'calculating all permutations of a following list: {numbers}')

curr_permutation = []
for i in range(n):
    curr_permutation.append(0)

# print(curr_permutation)

def permute(index, curr_permutation):
    # przeiteruje przez elementy listy dla current index poza tymi już użytymi w liscie curr_permuation
    # dla każego elementu listy curr_permutation wybierany jest element, po czym jest uruchamiany dla następnego tak długo aż nie zwróci fałszu (czyli kiedy wszystkie opcje zostały wyrbane)
    # kiedy zwróci fałsz przechodzi do następnej iteracji
    # kiedy nie ma następnej iteracji (nie ma już nic, czyli się skończyły) - zwraca fałsz i tym samym uruchamia rekurencje
    # zatrzymuje rekurencyjność kiedy jesteśmy na indeksie n-1 czyli ostatnim i wybraliśmy już dla niego pozycje
    # wtedy appenduje liste permutation tą liczbą i zwraca fałsz cofając do poprzedniego aż wykorzystane zostaną wszystkie opcje
    if index == n:
        # print(curr_permutation, 'HERE')
        permutations.append(curr_permutation.copy())
        # print(permutations)
        # The issue you're encountering stems from the fact that in Python, lists are mutable objects, and when you append a list to another list, it appends the reference to the list, not a copy of it. So, when you modify curr_permutation, it affects all previously appended instances of it in permutations, because they all point to the same list in memory.curr_permutation[index] = 0
        
    
    for item in numbers:
        if item not in curr_permutation:
            # print(f'index {index}, curr_permutation {curr_permutation}')
            curr_permutation[index] = item
            if permute(index+1, curr_permutation):
                curr_permutation[index] = 0

    return True

print("Zestaw 1, zadanie 15")
print("Napisz program, który dla zadanej liczby naturalnej n wypisze wszystkie permutacje zbioru {1, . . . , n}, to znaczy wszystkie sposoby uporządkowania elementów tego zbioru.")

permute(0, curr_permutation)
print(f'these are all {len(permutations)} permutations: {permutations}')
input()
            
