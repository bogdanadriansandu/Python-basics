# Variabile si tipuri de date

# Ex_1 - În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

# O variabila este o adresa de memorie ce stocheaza valori.

# Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:int, string, float, boolean

varsta = 32
nume = 'Popescu'
pret = 34.85
disponibil = True

# Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.

print(type(varsta))
print(type(nume))
print(type(pret))
print(type(disponibil))

""" 
Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă
(suprascriere), apoi verifică din nou tipul de date al acesteia.
"""

pret = round(pret)
print(pret, type(pret))

# Ex_5 - Incearca sa convertesti variabila string la int folosind type casting si observa rezultatele

# print(int(nume))

# Ex_6 - Incearca sa convertesti variabila boolean la int folosind type casting si observa rezultatele

print(int(disponibil))

# Ex_7 - Schimba valoarea variabilei boolean (din true in false sau din false in true) si repeta exercitiul anterior

disponibil = False
print(int(disponibil))

# Print

"""
Ex_1 -  Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip pe rand prin toate modalitatile cunoscute
"""

varsta = 32
nume = 'Popescu'
pret = 34.85
disponibil = True

print("Prima variabila are valoarea: " + str(varsta))
print('Numele lui este: ' + nume)
print("Pretul produsului este: ", str(pret))
print(f'Produsul este disponibil la raft? Raspuns: {disponibil}')

"""
Ex_2 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.
"""

nume = input('Introduceti numele: ')
prenume = input('Introduceti prenumele: ')
nume_complet = nume + prenume
nr_caractere = len(nume_complet)
print(f"Numele complet are {nr_caractere} caractere")

"""
Ex_3 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila.
Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.
"""

lungime = input('Introduceti lungimea: ')
latime = input('Introduceti latimea: ')
print('Aria dreptunghiului este ', float(lungime) * float(latime))

"""
Ex_4 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare
cuvântul 'the' în acest string
"""

sir = 'Coral is either the stupidest animal or the smartest rock'
nr_aparitii = sir.count('the')
print(nr_aparitii)

"""
Ex_5 Folosindu-te de string-ul de la exercițiul 4, inlocuieste “the” cu “THE” peste tot
(inclusiv in cuvantul “either”) si afișează pe ecran rezultatul
"""

sir = sir.replace('the', 'THE')
print(sir)

"""
Ex_6 Folosindu-te de string-ul de la exercițiul 4 foloseste un assert ca să verifici dacă acest string conține
doar numere.
"""

continut_sir = sir.isnumeric()
print(continut_sir)
assert continut_sir == False, 'sirul contine doar litere si spatii'

# Exercitii de dificultate medie

# Ex_1 Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.

sir_impar = input('Introduceti un sir de caractere de dimensiune impara (minim 3 caractere): ')
lungime_sir = len(sir_impar)
pozitie = int(lungime_sir/2) # pozitie = lungime_sir // 2
caracter = sir_impar[pozitie]
print(caracter)

# Ex_2 Folosind assert, verifică dacă un string este palindrom.

sir_1 = 'alabala'
sir_2 = sir_1[::-1]
assert sir_2 == sir_1, 'Sirul ar trebui sa fie un palindrom'

# Ex_3 - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:

sir_tastatura = input('Introduceti un text: ')

# salvează fiecare cuvânt într-o variabilă;

pozitie_spatiu = sir_tastatura.index(' ')  # pozSp = sir_tastatura.find(' ')
cuvant_1 = sir_tastatura[:pozitie_spatiu:]
cuvant_2 = sir_tastatura[pozitie_spatiu + 1::]

# printează ambele variabile pentru verificare.

print(cuvant_1, cuvant_2, sep='\n')

# Ex_4 - Citește un string de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:

sir_tastatura = input('Introduceti un text: ')

# salvează primul caracter într-o variabilă

primul_caracter = sir_tastatura[0]

# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

# Varianta 1 - am considerat ultimul caracter identic cu primul

# capitalizare primul caracter
caracter_mare = primul_caracter.upper()
# verificare numar de aparitii ale primului caracter in text
numar_aparitii = sir_tastatura.count(primul_caracter)
# extragere text fara primul caracter din sirul initial
sir_nou = sir_tastatura[1::]
# inlocuire primul caracter cu caracterul capitalizat in sirul nou mai putin de doua ori
sir_nou = sir_nou.replace(primul_caracter, caracter_mare, numar_aparitii-2)
# concatenare primul caracter cu sirul modificat si afisare in consola sir final
sir_final = primul_caracter + sir_nou
print(sir_final)

# Varianta 2 - am considerat ultimul caracter ca si pozitie in sir

ultimul_caracter = sir_tastatura[-1]

sir_modificat = primul_caracter + sir_tastatura[1:len(sir_tastatura)-1].replace(primul_caracter, primul_caracter.upper()) + ultimul_caracter
print(sir_modificat)

# Ex_5 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere'

user = input('Introduceti userul: ')
parola = input('Introduceti parola: ')
lungime_parola = len(parola)
print(f'Parola pt user {user} este {parola} si are {lungime_parola} caractere')

# Exercitii Structura Alternativa If

# Ex_1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

# if conditie: daca este adevarata se executa bucata de cod de sub if, altfel se executa codul de sub else

''' Ex_2 Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai
 mare ca 0) '''

x = 12

if type(x) is int and x > 0:
    print('x este numar natural')
else:
    print('x nu este numar natural')

# Ex_3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = -93.8

if x > 0:
    print('x este numar pozitiv')
elif x < 0:
    print('x este numar negativ')
else:
    print('x este numar neutru')

# Ex_4 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x = 11.9

if -2 <= x <= 13:
    print('x este in intervalul [-2, 13]')
else:
    print('x nu apartine intervalului [-2, 13]')

# Ex_5 Verifica daca x NU este intre 5 si 27, excluzand capetele de interval. (a se folosi ‘not’)

x = 5

# varianta 1
if 5 < x < 27:
    print('x este in intervalul deschis (5, 27)')
else:
    print('x nu este in intervalul deschis (5, 27)')

# varianta 2
if not 5 < x < 27:
    print('x nu este in intervalul deschis (5, 27)')
else:
    print('x este in intervalul deschis (5, 27)')

''' Ex_6 Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza
care din ele este mai mare '''

x, y = 7, 5

if x == y:
    print('x si y sunt egale')
elif x > y:
    print('x este mai mare decat y')
else:
    print('y este mai mare decat x')

''' Ex_7 Presupunand ca x, y, z (toate de tip int) reprezinta laturile unui triunghi, afiseaza daca triunghiul este
isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala). '''

x, y, z = 11, 12, 12

if x == y == z:
    print('Triunghiul este echilateral')
elif x == y or x == z or y == z:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul este oarecare')

''' Ex_8 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie! Trebuie sa
evaluati si cazurile uppercase si cazurile lowercase. '''

litera = input("Introduceti o litera: ")

if litera.lower() not in 'aeiou':
    print('Litera introdusa nu este o vocala')
else:
    print('Litera introdusa este o vocala')

# Exerciții Structura Alternativa If - Dificultate Medie

# Calculare pret discount

""" 
Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea
o reducere de 10%
Atat pentru seniori cat si pentru non- seniori se va aplica o reducere suplimentara de 10% daca vor calatori
in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% dacă vor călători
în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.
"""

pret_calatorie = input('Introduceti pretul calatoriei (in lei): ')
varsta = input("Introduceti varsta in ani: ")
insotitor = input('Calatoriti insotit de cel putin un copil? DA/NU ')
sezon_calatorie = input('In ce sezon doriti sa calatoriti (iarna/primavara/vara/toamna)? ')
clasa_calatorie = input('La ce clasa doriti sa calatoriti (clasa I, alta)? ')

if int(varsta) > 65:
    reducere = 0.15
else:
    if insotitor.lower() == 'da':
        reducere = 0.1
    else:
        reducere = 0
if sezon_calatorie.lower() == 'iarna':
    reducere += 0.1
if clasa_calatorie.lower() == 'clasa I':
    taxa_lux = 0.03
    pret_cu_reducere = float(pret_calatorie) * (1 - reducere)
    pret_final = pret_cu_reducere * (1 + taxa_lux)
else:
    taxa_gestiune = 0.01
    pret_cu_reducere = float(pret_calatorie) * (1 - reducere)
    pret_final = pret_cu_reducere * (1 + taxa_gestiune)

print(f'Pretul calatoriei este de {pret_final} lei')

''' Introduceti un nume de film de la tastatura si evaluati daca numele acelui film este numele filmului
vostru preferat. Daca da, atunci printati pe ecran: “Acesta este filmul meu preferat”. In caz contrar printati
pe ecran: “Din pacate nu este filmul meu preferat”
'''

film = input('Introduceti un nume de film: ')
film_preferat = 'Troia'

if film == film_preferat:
    print('Acesta este filmul meu preferat')
else:
    print('Din pacate nu este filmul meu preferat')

"""
 Aveti la dispozitie urmatorul database url:
jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
Extrageti din acest text numele bazei de date: mysql.db.server
Folositi un if statement pentru a evalua daca numele bazei de date este cel corect 
(presupunand ca extrageti url-ul dintr-un sistem extern si nu stiti care este acesta) 
"""

db_url = 'jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC'
nume_bd = 'mysql.db.server'
pozitie_start = db_url.find('//') + 2
pozitie_end = db_url.find(':', pozitie_start)
nume_extras = db_url[pozitie_start:pozitie_end]

if nume_extras == nume_bd:
    print('Numele bd este cel corect')
else:
    print('Numele bd nu este corect')
