'''
II.
Olvassunk be billentyűzetről tizedes törteket (float), és tároljuk őket egy listában!
A bevitel végét a 0.0 jelzi.
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5.5-nél nagyobb szám a listában?
2. Írjuk ki az első olyan szám indexét, ami(pl.: - negatív és egész 2.0, -5.0)!
3. Hány darab 1 és 2 közé eső szám szerepel a listában?
4. Melyik volt a legnagyobb értékű negatív szám, és hányadik helyen állt?
5. Mennyi a pozitív számok összege?
'''
szamok = []
run = True
while run:
    useri = float(input('Adj meg számokat, a 0 érték a számok megadásának végét jelentik\n'))
    szamok.append(useri)
    if useri == 0:
        run = False

print('1. feladat')
legnagyobbszam = 0
for i in szamok:
    if i > legnagyobbszam:
        legnagyobbszam = i

print(f'{legnagyobbszam}')

if legnagyobbszam > 5.5:
    print('Van 5.5-nél nagyobb szám')
else:
    print('Nincsen 5.5-nél nagyobb szám')


print('2. feladat:')
negativegesz = 0
inegativegesz = 0
for i in szamok:
    if i < 0 and i % 1 == 0:
        negativegesz = i
        inegativegesz = szamok.index(i)
        exit

print(f'Az első negatív egész szám a: {negativegesz}, indexe: {inegativegesz}')

print('3.feladat')
begyketto = []
for i in szamok:
    if 1 < i < 2:
        begyketto.append(i)
b_o_a_t = len(begyketto)
print(f'A listában {b_o_a_t} szám van 1 és kettő között')

print('4. feladat:')
try:
    negativszamok = []
    for i in szamok:
        if i < 0:
            negativszamok.append(i)

    print(max(negativszamok))

except ValueError as e:
    print(f'{e}: nem szerepel negativ szam a listában')

print('5.feladat')
pozitivszamok = []
for i in szamok:
    if i > 0:
        pozitivszamok.append(i)
pozitivosszegek = sum(pozitivszamok)
print(pozitivosszegek)