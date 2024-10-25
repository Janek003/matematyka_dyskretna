import itertools
ilosc_zmiennych = int(input("wprowadz ilosc zdan logicznych w rownaniu: "))

print("\n----- JAK WPROWADZAC ZMIENNE -----\n1)'^' = 'i'\n2)'V' = 'lub'\n3)'-' = 'zaprzeczenie'\n4)uzywaj nawiasow\n5)zmienne wprowadzaj od A-E wlacznie, duze litery\n6)uzywaj spacji pomiedzy wszystkimi znakami")

lewa_storna = input("\nlewa strona rownania: ").replace('^','and').replace('V','or').replace('-','not').replace('A','n[0]').replace('B','n[1]').replace('C','n[2]').replace('D','n[3]').replace('E','n[4]')

prawa_storna = input("prawa strona rownania: ").replace('^','and').replace('V','or').replace('-','not').replace('A','n[0]').replace('B','n[1]').replace('C','n[2]').replace('D','n[3]').replace('E','n[4]')

print(f"analizowane rownanie:\n{lewa_storna} = {prawa_storna}")

# m element list of (n element lists) each containing a differnet combination of True and False

cartesian_product = list(itertools.product([True, False], repeat=ilosc_zmiennych))

n = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0} # variable dictionary

ls = ["A", "B", "C", "D", "E"]

for i in range(ilosc_zmiennych):
    print(ls[i].ljust(5), end=" | ")



print("Lewa  | Prawa")

for i in range(ilosc_zmiennych):    
    print('_________', end="")

print("___________")

is_correct = "tozsamosc"

for item in cartesian_product:
    
    for i, element in enumerate(item):
        n[i] = element
        print(str(element).ljust(5), end = " | ")

    print(f"{str(eval(lewa_storna)).ljust(5)} | {str(eval(prawa_storna)).ljust(5)}")

    if eval(lewa_storna) != eval(prawa_storna):
        is_correct = "sprzecznosc"

print(f"\n{is_correct}")