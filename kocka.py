'''
I.
Szimuláljuk egy 6 oldalú kocka 20 dobását! A dobásokat egy listában tároljuk!
Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 5-ös dobás a listában?
2. Hanyadik dobás lett először 1-es?
3. Hány darab páros számot dobtunk?
4. Melyik volt a legkisebb dobás a 4-nél nagyobbak közül, és hányadik dobás volt?
5. Mennyi a 3-as dobások összege?
'''

import random

dobasszam = 0
dobott_ertekek = []
paros = 0

while dobasszam < 20:
    gennum = random.randrange(1, 7)
    dobott_ertekek.append(gennum)
    dobasszam += 1

print (f'{dobott_ertekek}')

print('1. feladat')
otos = dobott_ertekek.count(5)
if otos >= 1:
    print('Van 5-ös a listában')
else:
    print('Nincsen 5-ös a listában')

try:
    elsoegyes = dobott_ertekek.index(1)
    print(f'2. feladat:\naz {elsoegyes + 1}. dobás lett először 1-es szám')

except ValueError as e:
    print(f'{e}, nem fordul elő 1-es szám')

for i in dobott_ertekek:
    if i % 2 == 0:
        paros += 1

print(f'3. feladat:\n{paros} alkalommal fordult elő páros szám')

def elsonegyplus():
    if dobott_ertekek.count(5) != 0:
        elf = dobott_ertekek.index(5)
        print(f'az 5-ös szám {elf}. indexen fordult elő először')
    elif dobott_ertekek.count(6) != 0:
        elf = dobott_ertekek.index(6)
        print(f'a 6-os szám {elf}. indexen fordult elő először')
    else:
        print('nem fordult elő 4-nél nagyobb szám')

print('4. feladat:')
elsonegyplus()

harmasokosszege = 0

for i in dobott_ertekek:
    harmaselof = dobott_ertekek.count(3)
    harmasokosszege = harmaselof*+3

print(f'5. feladat:\n a 3-sok összege: {harmasokosszege}')
