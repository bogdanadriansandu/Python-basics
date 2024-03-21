import calendar
import math


# 1. Definiti o funcție fara parametri si fara return care să calculeze și să returneze suma a două numere.

def suma_numere():
    a, b = 7, 19
    suma = a + b
    print(suma)


suma_numere()


# 2. Definiti o funcție care să returneze TRUE dacă un număr este par sau FALSE daca numarul este impar

def numar_par_impar():
    numar = input('Introduceti numarul: ')
    if int(numar) % 2 == 0:
        return True
    else:
        return False


print(numar_par_impar())


# 3. Definiti o funcție o care returnează numărul total de caractere din numele tău complet (nume, prenume, nume_mijlociu)

def numar_caractere():
    nume = input('Introduceti numele: ')
    prenume = input('Introduceti prenumele: ')
    nume_mijlociu = input('Introduceti numele mijlociu: ')
    return len(nume + prenume + nume_mijlociu)


print(numar_caractere())


# 4. Definiti o funcție care returnează aria unui dreptunghi cu laturile primite prin parametru


def arie_dreptunghi(lungime, latime):
    return lungime * latime


print(arie_dreptunghi(8, 14))
print(arie_dreptunghi(12, 7))


# 5. Definiti o funcție care returnează aria unui cerc si o returneaza. Raza va fi primita prin parametru.


def arie_cerc(raza):
    return math.pi * raza ** 2


print(arie_cerc(5))

# 6. Funcție care returnează TRUE dacă un caracter x se găsește într-un string dat și FALSE in caz contrar.

sir = 'fasgad ;lgadfj;l etwq;ml'


def gasire_caracter():
    caracter = input('Introduceti caracterul: ')
    if caracter in sir:
        return True
    else:
        return False


print(gasire_caracter())

"""
7. Definiti o funcție fără return care primește un string și printează pe ecran:
 - Numărul de caractere lower case este x
 - Numărul de caractere upper case exte y
"""


def numarare_caractere_mici_mari(sir):
    x, y = 0, 0
    for litera in sir:
        if litera.islower():
            x += 1
        elif litera.isupper():
            y += 1
    print(f"Numarul de caractere lower case este {x} \nNumarul de caractere upper este {y}")


numarare_caractere_mici_mari(input('Introduceti sirul: '))

""" 8. Definiti o funcție care primește ca parametru o LISTĂ de numere și returnează o alta LISTĂ doar cu numerele 
pozitive """

lista_pozitiva = []


def numere_pozitive(lista):
    for numar in lista:
        if numar >= 0:
            lista_pozitiva.append(numar)
    return lista_pozitiva


print(numere_pozitive([-8, 12, -23, 8, 17, -63.2, 69.6]))

""" 
9. Definiti o funcție care nu returneaza nimic dar care primește două numere și PRINTEAZĂ
 - Primul număr x este mai mare decat al doilea număr y
 - Al doilea număr y este mai mare decat primul număr x
 - Numerele sunt egale.
"""


def comparare_numere(x, y):
    if x > y:
        print(f"Primul număr {x} este mai mare decat al doilea număr {y}")
    elif y > x:
        print(f"Al doilea număr {y} este mai mare decat primul număr {x}")
    else:
        print("Numerele sunt egale")


comparare_numere(9, 5.8)
comparare_numere(7.3, 58)
comparare_numere(14, 14)

""" 
10. Definiti o funcție care primește un număr și un set de numere. Functia va face urmatoarele:
va printa ‘am adaugat numărul nou în set’ si va returna TRUE daca numarul nu exista deja in set
va ‘nu am adaugat numărul în set. Acesta există deja’ si va returna FALSE daca numarul exista deja in set
"""


def apartenenta_la_set(numar, set_numere):
    if numar in set_numere:
        print("Nu am adaugat numărul în set. Acesta există deja")
        return False
    else:
        set_numere.add(numar)
        # print(set_numere)
        print("Am adaugat numărul nou în set")
        return True


print(apartenenta_la_set(8, {9, 17, 3, 5}))
print(apartenenta_la_set(5, {19, 17, 23, 5}))


# 11. Definiti o funcție care primește o lună din an și returnează câte zile are acea lună.


def numarare_zile_luna(luna):
    numar_zile = calendar.monthrange(2023, luna)[1]
    return numar_zile


print(numarare_zile_luna(8))
print(numarare_zile_luna(2))


# 12. Definiti o funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea si împărțirea a două numere.


def calculator():
    a = float(input("Introduceti primul numar: "))
    b = float(input("Introduceti al doilea numar: "))
    suma = a + b
    diferenta = a - b
    inmultire = a * b
    try:
        impartire = a / b
    except ZeroDivisionError:
        impartire = 'Eroare impartire la 0'
    return suma, diferenta, inmultire, impartire


print(calculator())

""" 
13. Definiti o funcție care primește o listă de cifre (adică doar 0-9) si care returnează un dictionar care va contine 
cifra ca si cheie si numarul de aparitii ale acelei cifre ca valoare
"""

dictionar = {}


def lista_dictionar(lista):
    for cifra in lista:
        dictionar.update({cifra: lista.count(cifra)})
    return dictionar


print(lista_dictionar([1, 2, 1, 3, 5, 6, 2, 3, 8, 6, 1, 6]))


# 14. Definiti o funcție care primește 3 numere si returnează valoarea maximă dintre ele.


def maxim_numere(a, b, c):
    return max(a, b, c)


print(maxim_numere(8, 12, 6))
print(maxim_numere(18, -12, 16))
print(maxim_numere(11, 4, 16))


# 15. Definiti o funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.


def suma_n_numere(numar):
    suma = 0
    for i in range(numar):
        suma += i
    return suma


print(suma_n_numere(10))


# 16. Definiti o funcție care sa primească 2 liste de numere (numerele pot fi dublate) si sa returneze numerele comune.


def numere_comune(lista_1, lista_2):
    return list(set(lista_1).intersection(lista_2))


print(numere_comune([5, 2, 2, 9, 8, 5, 3], [2, 7, 9, 5, 4]))

""" 
17. Definiti o funcție care să aplice o reducere de preț. Dacă produsul costă 100 lei și aplicăm reducere de 10%. 
Pretul va fi 90 de lei. Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""


def aplicare_reducere_pret(pret_initial, reducere):
    # Verific daca reducerea este in intervalul [0%, 100%]
    if 0 <= reducere <= 100:
        # Calculez noul pret dupa ce aplic reducerea
        pret_final = pret_initial * (1 - reducere / 100)
        return pret_final
    else:
        # Reducerea este invalida si ridic o exceptie
        raise ValueError("Reducerea trebuie sa fie in intervalul [0%, 100%]")


try:
    pret_final = aplicare_reducere_pret(100, 10)
    print(f"Pretul dupa reducere: {pret_final:.2f} lei")
except ValueError as e:
    print(f"Eroare: {e}")
