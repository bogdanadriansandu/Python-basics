# Liste

"""
Definiti o lista care sa stocheze numele tuturor celor prezenti la studiul individual.
Parcurgeti lista si printati toate elementele din aceasta folosind pe rand for, while si foreach
"""

lista_prezenta = ["Bogdan", "Codruta", "Denisa", "Razvan", "Simona", "Daniel"]

# for
for i in range(len(lista_prezenta)):
    print(lista_prezenta[i])

i = 0

# while
while i < len(lista_prezenta):
    print(lista_prezenta[i])
    i += 1

# foreach
for cursant in lista_prezenta:
    print(cursant)

''' Exercitii bonus - ATENTIE!!! Pentru aceste exercitii va trebui sa va puneti in aplicare abilitatile de “detectivi”
 si sa cautati pe google '''


# Bonus 1: Sortati o lista folosind algoritmul de sortare prin metoda bulelor (bubble sort)

def bubble_sort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = [-2, 45, 0, 11, -9]

bubble_sort(data)

print('Sorted Array in Ascending Order:')
print(data)


# Optimized Bubble sort

def optimized_bubble_sort(array):
    # loop through each element of array
    for i in range(len(array)):

        # keep track of swapping
        swapped = False

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping occurs if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break


optimized_bubble_sort(lista_prezenta)

print('Sorted Array in Ascending Order:')
print(lista_prezenta)

"""
Bonus 2: Incercati sa printati pe ecran pe cei 101 dalmatieni salvati intr-o lista. La fiecare dalmatian veti printa
pe ecran urmatorul text: “Dalmatianul curent se afla in pozitia “i””. Atentie, ghilimelele vor trebui tratate
folosind caracterul escape
"""

dalmatieni = ["Dalmatianul " + str(i) for i in range(1, 102)]

for i in range(1, len(dalmatieni) + 1):
    print(f"Dalmatianul curent se afla in pozitia \"{i}\"")

# Dictionare

# Aveti urmatorul dictionar (dictionar imbricat / nested dictionary / embedded dictionary):

fotbalisti_pe_echipe = {
    "Barcelona":
        {
            "Dica":
                {
                    "Nume complet": "Nicolae Dica",
                    "Varsta": 45,
                    "Numar Tricou": 10
                },
            "Banel":
                {
                    "Nume complet": "Banel Nicolita",
                    "Varsta": 47,
                    "Numar Tricou": 3
                },
            "Dukadam":
                {
                    "Nume complet": "Helmut Dukadam",
                    "Varsta": 65,
                    "Numar Tricou": 7
                }
        }
}

# Pe baza acestui dictionar faceti urmatoarele exerciti:

# - Printati pe ecran numarul de pe tricou al oricarui jucator doriti

numar_tricou = fotbalisti_pe_echipe["Barcelona"]["Dukadam"]["Numar Tricou"]

print(f"Numarul de pe tricou al lui Dukadam este: {numar_tricou}")

# - Folositi functia pop pentru a scoate orice jucator din dictionar

jucator_sters = fotbalisti_pe_echipe["Barcelona"].pop("Banel")

print(f"Jucatorul scos este: {jucator_sters}")
print(fotbalisti_pe_echipe)

"""
- Printati pe ecran detaliile despre fiecare jucator astfel incat sa obtineti urmatorul rezultat:
La echipa Barcelona joaca jucatorul:
Detalii jucator - Nume complet:Nicolae Dica, Detalii jucator - Varsta:45, Detalii jucator - Numar Tricou:10,
...
"""

for echipa, jucatori in fotbalisti_pe_echipe.items():
    for nume_jucator, detalii_jucator in jucatori.items():
        print(f"\nLa echipa {echipa} joaca jucatorul:")
        for cheie, valoare in detalii_jucator.items():
            print(f"Detalii jucator - {cheie}: {valoare}")

# Alte Exercitii

# 1. Ascunde vocalele! Să se scrie un "translator" care să modifice vocalele în "*" utilizând ciclul while / if / for.

# cu while

vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

text_initial = input('Introduceti textul: ')
text_final = ''

i = 0

while i < len(text_initial):
    if text_initial[i] in vocale:
        text_final += "*"
    else:
        text_final += text_initial[i]
    i += 1

print(text_final)

# cu for

vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

text_initial = input('Introduceti textul: ')
text_final = ''

for caracter in text_initial:
    if caracter in vocale:
        text_final += "*"
    else:
        text_final += caracter

print(text_final)

# 2. Tipăriţi toate numerele prime aflate între două numere naturale citite de la tastatura

# Rezolvare cu functie

"""
def este_prim(num):
    # Verifică dacă un număr este prim.
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Validăm și citim cele două numere de la tastatură
while True:
    try:
        a = int(input("Introduceți primul număr natural: "))
        b = int(input("Introduceți al doilea număr natural (mai mare sau egal cu primul): "))

        if a <= 0 or b <= 0 or b < a:
            raise ValueError("Numerele trebuie să fie naturale, iar al doilea număr trebuie să fie mai mare sau egal cu primul.")

        break
    except ValueError as ve:
        print(ve)
        continue

print(f"Numere prime între {a} și {b}:")

# Tipărim toate numerele prime din intervalul [a, b]
for num in range(a, b + 1):
    if este_prim(num):
        print(num)
"""

# Rezolvare fara functie

# Citim cele două numere de la tastatură și verificăm validitatea lor
while True:
    a = int(input("Introduceți primul număr: "))
    b = int(input("Introduceți al doilea număr: "))

    if a <= 0 or b <= 0:
        print("Ambele numere trebuie să fie naturale. Vă rugăm să reintroduceți.")
    elif b < a:
        print("Al doilea număr trebuie să fie mai mare sau egal cu primul. Vă rugăm să reintroduceți.")
    else:
        break

print(f"Numere prime între {a} și {b}:")

# Verificăm și tipărim toate numerele prime din intervalul [a, b]
for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
"""
3. Se citește un număr natural n. Să se scrie programul care determină și afișează câte cifre impare are numărul citit.
"""

cifre_impare = 0

n = int(input("Introduceti numarul natural: "))

if n > 0:
    for cifra in str(n):
        if int(cifra) % 2 != 0:
            cifre_impare += 1

    print(f"Numarul introdus {n} are {cifre_impare} cifra(e) impara(e)")

else:
    print(f"Numarul introdus nu este un numar natural")

# Alta solutie

# Citim numărul natural de la tastatură
n = int(input("Introduceți un număr natural: "))

# Inițializăm un contor pentru cifrele impare
cifre_impare = 0

# Iterăm prin cifrele numărului și numărăm cifrele impare
while n > 0:
    cifra = n % 10  # obținem ultima cifră a numărului
    if cifra % 2 != 0:  # verificăm dacă cifra este impară
        cifre_impare += 1  # creștem contorul cifrelor impare
    n //= 10  # eliminăm ultima cifră a numărului

# Afișăm rezultatul
print(f"Numărul are {cifre_impare} cifre impare.")

# 4. Se citește un număr natural n. Să se scrie programul care determină și afișează numărul de cifre ale lui n

n = input("Introduceti numarul natural: ")

if int(n) < 1:
    print(f"Numarul introdus nu este un numar natural")
else:
    print(f"Numarul introdus {n} are {len(n)} cifre")

# 5. Se citește un număr natural n. Să se scrie programul care verifică dacă numărul citește palindrom

n = input("Introduceti numarul natural: ")
numar_inversat = n[::-1]

if int(n) < 1:
    print(f"Numarul introdus nu este un numar natural")
elif n == numar_inversat:
    print(f"Numarul introdus {n} este un palindrom")
else:
    print(f"Numarul introdus {n} nu este un palindrom")

"""
6. Se citește un număr natural n. Să se scrie programul care determină și afișează cea mai mare și cea mai mică cifră
a numărului n
"""

n = input("Introduceți un număr natural: ")

# Verificăm dacă numărul este un număr natural
if n.isdigit() and int(n) > 0:
    # Convertim șirul într-o listă de cifre
    lista_cifre = [int(c) for c in n]

    # Determinăm cea mai mare și cea mai mică cifră
    cifra_maxima = max(lista_cifre)
    cifra_minima = min(lista_cifre)

    # Afișăm rezultatele
    print(f"Cea mai mare cifră a numărului {n} este: {cifra_maxima}")
    print(f"Cea mai mică cifră a numărului {n} este: {cifra_minima}")
else:
    print("Numărul introdus nu este un număr natural.")

""" 
7. Se citește un număr natural n. Să se scrie programul care afișează pe ecran mesajul DA dacă toate cifrele lui n 
sunt în ordine crescătoare și mesajul NU în caz contrar 
"""

n = input("Introduceti numarul natural: ")

lista_cifre = []

if int(n) < 1:
    print(f"Numarul introdus nu este un numar natural")
else:
    for i in range(len(n)):
        lista_cifre.append(n[i])

    if lista_cifre == sorted(lista_cifre):
        print('DA')
    else:
        print('NU')

""" 
8. Se citesc n numere întregi. Se cere: suma numerelor citite, maximul, minimul, cele mai mari/mai mici două numere 
citite, câte sunt negative, câte sunt pare/impare, cel mai mare număr negativ/pozitiv 
"""

count_numere = int(input('Cate numere doriti sa introduceti? '))

lista_numere = []

for i in range(1, count_numere + 1):
    lista_numere.append(int(input(f'Introduceti numarul intreg {i}: ')))

suma_numere = 0
numere_negative = 0
numere_impare = 0

for numar in lista_numere:
    suma_numere += numar
    if numar < 0:
        numere_negative += 1
    if numar % 2 != 0:
        numere_impare += 1

print(f'Suma celor {count_numere} citite este: {suma_numere}')

numar_maxim = max(lista_numere)

print(f'Maximul celor {count_numere} citite este: {numar_maxim}')

numar_minim = min(lista_numere)

print(f'Minimul celor {count_numere} citite este: {numar_minim}')

lista_unica = list(set(lista_numere))
lista_unica.sort()

print(f'Cele mai mari două numere citite sunt: {numar_maxim}, {lista_unica[len(lista_unica) - 2]}')
print(f'Cele mai mici două numere citite sunt: {numar_minim}, {lista_unica[1]}')

print(f'Din cele {count_numere} numere citite {numere_negative} sunt negative.')
print(f'Din cele {count_numere} numere citite {count_numere - numere_impare} sunt pare.')
print(f'Din cele {count_numere} numere citite {numere_impare} sunt impare.')

if numere_negative > 0:
    lista_numere.sort()
    print(f'Din cele {count_numere} numere citite cel mai mare număr negativ este: {lista_numere[numere_negative -1]}')
else:
    print('Toate numerele introduse sunt pozitive')
if numar_maxim >= 0:
    print(f'Din cele {count_numere} numere citite cel mai mare număr pozitiv este: {numar_maxim}')
else:
    print('Toate numerele introduse sunt negative')
