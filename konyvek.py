"""
Olvasd be a konyvek.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány könyv szerepel a fájlban?
2. Melyik könyvnek van a legtöbb oldala?
3. Melyik könyvnek van a legkevesebb oldala?
4. Melyik szerző írt a legtöbb könyvet?
5. Átlagosan hány oldalasak a könyvek?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik kiadó adott ki a legtöbb könyvet?

A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""

konyvek = []
with open('beolvasando_adatok/konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        konyv = {'Cím': adatok[0],
                'Szerző': adatok[1],
                'Oldalszám': int(adatok[2]),
                'Kiadó': adatok[3]}
        konyvek.append(konyv)

print(f'{konyvek=}')


#1. feladat

konyek_szama = len(konyvek)

#2. feladat

legtobb_konyv_oldalszam = 0
legtobb_konyv_oldalszam_konyv = ''

for konyv in konyvek:
    if konyv['Oldalszám'] > legtobb_konyv_oldalszam:
        legtobb_konyv_oldalszam = konyv['Oldalszám']
        legtobb_konyv_oldalszam_konyv = konyv['Cím']

#3. feladat

legkevesebb_konyv_oldalszam = 0
legkevesebb_konyv_oldalszam_konyv = ''

for konyv in konyvek:
    if konyv['Oldalszám'] < legkevesebb_konyv_oldalszam:
        legkevesebb_konyv_oldalszam = konyv['Oldalszám']
        legkevesebb_konyv_oldalszam_konyv = konyv['Cím']

#4. feladat

legtobb_konyv_iro = ''
legtobb_iro_konyvei = []
legtobb_konyv = 0

for konyv in konyvek:
    if konyv['Szerző'] == legtobb_konyv_iro:
        legtobb_iro_konyvei.append(konyv['Cím'])
        legtobb_konyv = len(legtobb_iro_konyvei)

    else:
        if legtobb_konyv < kony












print(f"1. A beolvasott fájlban összesen ____ könyv szerepel.")
print(f"2. A legtöbb oldalas könyv: ____")
print(f"3. A legkevesebb oldalas könyv: ____")
print(f"4. A legtöbb könyvet író szerző: ____")
print(f"5. Az átlagos oldalszám: ____")
print(f"***A legtöbb könyvet kiadó kiadó: ____")