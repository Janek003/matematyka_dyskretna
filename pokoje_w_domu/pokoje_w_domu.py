def pokojePoRuchu(dokad_pokoj_drzwi, wybrane_drzwi, pokoje_og):

    nowe_pokoje = [0 for _ in range(len(pokoje_og))]
    
    for pokoj, gracze_w_pokoju in enumerate(pokoje_og):

        ida_do = dokad_pokoj_drzwi[pokoj][wybrane_drzwi]
        nowe_pokoje[ida_do] += gracze_w_pokoju
    
    return nowe_pokoje

def czyKoniec(pokoje, zbior_docelowy, il_graczy):

    razem = 0
    for item in zbior_docelowy:
        razem += pokoje[item]
        
    if razem == il_graczy: return True
    return False

def wynik(file_name):
    
    with open(file_name, 'r') as file: 
        lines = file.read().split("\n")
    
    ilosc_pokojow = int(lines[0])
    ilosc_graczy = int(lines[1])

    poczatkowe_pokoje = [int(pokoj) - 1 for pokoj in lines[2].split(" ")]
    zbior_koncowy = [int(element) - 1 for element in lines[3].split(" ")]

    schemat_w_cyfrach = lines[4].replace('A', '0').replace('B', '1').replace('C', '2').replace('D', '3')
    schemat = [int(cyfra) for cyfra in schemat_w_cyfrach]
    
    pokoje = [0 for _ in range(ilosc_pokojow)]

    for poczatkowy_pokoj in poczatkowe_pokoje: pokoje[poczatkowy_pokoj] += 1

    dokad_pokoj_drzwi = [ [ int(item) - 1 for item in lines[5 + i].split(" ") ] for i in range(ilosc_pokojow) ]
    
    tried_moves = []

    etapy = 0
    while not czyKoniec(pokoje, zbior_koncowy, ilosc_graczy):

        i = etapy % len(schemat)
        wybrane_drzwi = schemat[i]

        curr_move = [i, pokoje]
        
        if curr_move in tried_moves: return "NIE"

        tried_moves.append(curr_move)
        pokoje = pokojePoRuchu(dokad_pokoj_drzwi, wybrane_drzwi, pokoje)

        etapy += 1
        # print(f"{etapy}: {pokoje}")

    return etapy

pliki = ["example.txt", "example2.txt"]
# pliki = ["input1.txt", "input2.txt", "input3.txt"]

for plik in pliki:
    print( f"wynik dla {plik}: { wynik(plik) }" )