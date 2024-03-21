import datetime

# Definiti o adresa de memorie care sa salveze data curenta. Va fi o variabila sau o constanta?

# Va fi o variabila pentru ca valoarea ei se schimba

# declarare si initializare variabila de tip date
data_curenta = datetime.date.today()

# afisare valoare variabila in consola
print(data_curenta)

# Identificati tipul de data pe care il are variabila pe care ati definit-o folosind una din functiile invatate la curs

# afisare tip de data
print(type(data_curenta))

# Definiti alte cateva variabile care sa stocheze cursul la care sunteti, ce zi este si la ce sesiune de curs sunteti.

# declarare si initializare variabile
curs = 'Testare Manuala si Testare Automata'
zi_curs = 'marti'
sesiune_curs = 1

# afisare variabile in consola
print(curs, zi_curs, sesiune_curs, sep='\n')

# Salvati fiecare cuvant din propozitia: “Ana s-a nascut in anul 1990 si acum are 33 de ani” in cate o adresa de memorie.

# declarare si initializare variabile pentru fiecare cuvant din propozitia de mai sus
cuvant_1 = 'Ana'
cuvant_2 = 's-a'
cuvant_3 = 'nascut'
cuvant_4 = 'in'
cuvant_5 = 'anul'
cuvant_6 = 1990
cuvant_7 = 'si'
cuvant_8 = 'acum'
cuvant_9 = 'are'
cuvant_10 = 33
cuvant_11 = 'de'
cuvant_12 = 'ani'

# Printati propozitia de mai sus folosind trei tipuri diferite de printuri.

# 1. Printare cu concatenare si type casting
print(cuvant_1 + ' ' + cuvant_2 + ' ' + cuvant_3 + ' ' + cuvant_4 + ' ' + cuvant_5 + ' ' + str(cuvant_6) + ' ' + cuvant_7 + ' ' + cuvant_8 + ' ' + cuvant_9 + ' ' + str(cuvant_10) + ' ' + cuvant_11 + ' ' + cuvant_12)

# 2. Printare cu formatare
print(f'{cuvant_1} {cuvant_2} {cuvant_3} {cuvant_4} {cuvant_5} {cuvant_6} {cuvant_7} {cuvant_8} {cuvant_9} {cuvant_10} {cuvant_11} {cuvant_12}')

# 3. Printare cu separator ' '
print(cuvant_1, cuvant_2, cuvant_3, cuvant_4, cuvant_5, cuvant_6, cuvant_7, cuvant_8, cuvant_9, cuvant_10, cuvant_11, cuvant_12, sep=' ')

# Declarati cateva alte adrese de memorie la alegere si initializati-le folosind functia input.

# declarare si initializare variabile/constante cu input
varsta = input('Introduceti varsta: ')
NUME = input('Introduceti numele: ')
MASTER = input('Absolvent Master (True/False): ')
inaltime = input('Introduceti inaltimea: ')

# afisare variabile/constante in consola
print(int(varsta), NUME, bool(MASTER), float(inaltime), sep='\n')

# Adaugati comentarii la fiecare linie de cod cu explicatii cu privire la ce ati facut la fiecare
