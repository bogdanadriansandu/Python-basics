# Liste

# 1. Declarati o lista cu elemente multitype
lista = ['Popescu', 'engleza', 42, 18.5, True]

# 2. Declarati o lista goala
lista_goala = []

# 3. Accesati orice element din lista pe baza de index
primul_element = lista[0]
print(primul_element)
ultimul_element = lista[-1]
print(ultimul_element)

# 4. Accesati pozitia unui element din lista pe baza functiei index()
second = lista.index('engleza')
print(second)

# 5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert(). Observati rezultatele
lista.append(36)
print(lista)
lista.insert(2, 'Valoare')
print(lista)

# 6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele
lista.pop()
print(lista)
lista.remove('Valoare')
print(lista)

# 7. Numarati elementele dintr-o lista folosind functia len()
nr_elemente = len(lista)
print(nr_elemente)

# 8. Numarati de cate ori apare un anumit element in lista folosind functia count()
nr_aparitii = lista.count('engleza')
print(nr_aparitii)

# 9. Uniti doua liste folosind functia extend()
lista_2 = [38, False, 'ceva', 'engleza']
lista.extend(lista_2)
print(lista)

# 10. Sortati lista folosind functia sort()
lista_3 = [ 18, 29, 7, 87, 3]
lista_3.sort()
print(lista_3)

# 11. Inversati continutul listei folosind functia reverse()
lista.reverse()
print(lista)

# 12. Stergeti toate elementele din lista folosind functia clear()
lista.clear()
print(lista)

# Tupluri

# 1. Declarati un tuplu
tuplu = ('orice', 'ceva', 'altceva', 'Ionut', 'Andrei')
print(tuplu)

# 2. Declarati un tuplu gol
tuplu_gol = ()
print(tuplu_gol)

# 3. Accesati orice element din tuplu pe baza de index
third = tuplu[2]
print(third)

# 4. Accesati pozitia unui element din lista pe baza functiei index()
position = tuplu.index('Ionut')
print(position)

# 5. Folositi functia count() pentru a numara de cate ori apare un element in tuplu
nr_aparitii_elem = tuplu.count('ceva')
print(nr_aparitii_elem)

# 6. Folositi functia index() pentru a verifica pozitia la care se afla un anumit element in tuplu
element_position = tuplu.index('Andrei')
print(element_position)

# 7. Incercati sa modificati un element din tuplu si observati rezultatele
# tuplu['Ionut'] = 'Ionel'
# nu se pot modifica elementele unui tuplu

# Seturi

# 1. Declarati un set
primul_set = {'Vlad', 'Maria', 'Gigi', 'Vlad', 'Vali'}
print(primul_set)

# 2. Declarati un set gol
set_gol = {}
print(set_gol)

# 3. Adaugati un element nou in set folosind functia add()
primul_set.add('Danut')
print(primul_set)

# 4. Stergeti un element din set folosind functia pop() si respectiv functia remove(). Observati rezultatele
# primul_set.pop()
print(primul_set)
primul_set.remove('Gigi')
print(primul_set)

# 5. Verificati daca un set este o subdiviziune a unui alt set (subset)
second_set = {'Maria', 'Vali'}
print(primul_set.issubset(second_set))
print(second_set.issubset(primul_set))

# 6. Verificati daca un set contine toate elementele dintr-un alt set + alte elemente (superset)
print(primul_set.issuperset(second_set))
print(second_set.issuperset(primul_set))

# 7. Verificati care sunt elementele comune intre doua seturi (intersection)
print(primul_set & second_set)
print(primul_set.intersection(second_set))

# 8. Verificati diferenta intre doua seturi cu functia difference()
print(primul_set.difference(second_set))
print(second_set.difference(primul_set))

# 9. Stergeti toate elementele dintr-un set folosind functia clear()
print(second_set.clear())

# Dictionare

# 1. Declarati un dictionar
primul_dictionar = {'cheia1': 'valoare1', 'cheia2': 'valoare2', "cheia3": 'valoare3'}
print(primul_dictionar)

# 2. Declarati un dictionar gol
dictionar_gol = dict()
print(dictionar_gol)

# 3. Adaugati un element nou in dictionar folosind functia update() si respectiv pe baza de cheie
primul_dictionar.update({'cheie4': 'valoare4'})
print(primul_dictionar)
primul_dictionar['cheie8'] = 'valoare8'
print(primul_dictionar)
primul_dictionar['cheie4'] = 'valoare4.1'
print(primul_dictionar)

# 4. Extrageti un element din dictionar folosind metoda get() si respectiv pe baza de cheie
print(primul_dictionar.get('cheia2'))
print(primul_dictionar['cheia3'])

# 5. Stergeti un element din dictionar folosind functia pop() si respectiv functia popitem(). Observati rezultatele
print(primul_dictionar.pop('cheie4'))
print(primul_dictionar)
print(primul_dictionar.popitem())
print(primul_dictionar)

# 6. Extrageti pe rand toate cheile, apoi toate valorile, si apoi toate item-urile din dictionar
print(primul_dictionar.keys())
print(primul_dictionar.values())
print(primul_dictionar.items())

# 7. Stergeti toate valorile din dictionar folosind metoda clear()
primul_dictionar.clear()
print(primul_dictionar)
