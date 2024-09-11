jmeno = "Lukáš"         # Vytvořte proměnnou, do které vložíte své jméno.
prijmeni = "Tichý"      # Vytvořte proměnnou, do které vložíte své příjmení.
vek = 16


print("Jméno:", jmeno)          # Vypište tyto dvě proměnné do konzole.
print("Příjmení:", prijmeni)


vek = int (input("Vas vek:"))   # Vytvořte vstup pro uživatele, který bude moct zadat pouze věk (nikoli své jméno nebo jinou stringovou hodnotu).
print ("Vas vek", vek)


print("Delka jmena:", len(jmeno))           #  Vypište v konzoli délku první proměnné a druhé proměnné.
print("Delka prijmeni:", len(prijmeni))


cislo = 6               # Vytvořte proměnnou, do které uložíte hodnotu 6.
print ("Cislo", cislo)


hodnota = 0             # Vytvořte cyklus, který bude mít 5 opakování a při každém opakování se přičte hodnota 3.

for i in range(5):                  
    hodnota += 3
    print(f'Opakovani {i + 1}: {hodnota}')

print(f'Konečná hodnota: {hodnota}')  #Vypište v konzoli výslednou hodnotu po 5 cyklech.


vstup = input("Zadejte svůj věk: ")

try:
    vek = int(vstup)                    # Vytvořte podmínku pro uživatele, který zadá věk - 1. Pokud zadá jen celočíselnou hodnotu program odpoví "Děkuji". 2. Pokud zadá jakoukoli jinou hodnotu program odpoví "Zadej jen celočíselnou hodnotu." 
    
    if vek < 0:
        print("Zadej jen celočíselnou hodnotu.")
    else:
        print("Děkuji")
except ValueError:
    print("Zadej jen celočíselnou hodnotu.")


import random

nahodne_cislo = random.randint(1,10)

print("Náhodne cislo", nahodne_cislo)