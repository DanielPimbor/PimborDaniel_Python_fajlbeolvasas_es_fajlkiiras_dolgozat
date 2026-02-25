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
legkevesebb_oldalszam_konyv = ''

for konyv in konyvek:
    if legkevesebb_konyv_oldalszam == 0:
        legkevesebb_konyv_oldalszam = konyv['Oldalszám']
        legkevesebb_oldalszam_konyv = konyv['Cím']

    elif konyv['Oldalszám'] < legkevesebb_konyv_oldalszam:
        legkevesebb_konyv_oldalszam = konyv['Oldalszám']
        legkevesebb_oldalszam_konyv = konyv['Cím']

#4. feladat

legtobb_konyv=0
legtobb_konyv_iroi = []

konyvek_iroi=[]

for konyv in konyvek:
    konyvek_iroi.append(konyv['Szerző'])

for iro in konyvek_iroi:
    if konyvek_iroi.count(iro) > legtobb_konyv:
        legtobb_konyv = konyvek_iroi.count(iro)
        legtobb_konyv_iroi.append(iro)
    elif konyvek_iroi.count(iro) == legtobb_konyv:
        legtobb_konyv_iroi.append(iro)

legtobb_konyv_iroi = set(legtobb_konyv_iroi)

#5. feladat

osszes_oldal = 0

for konyv in konyvek:
    osszes_oldal += konyv['Oldalszám']

atlag = osszes_oldal / len(konyvek)


#6. feladat

legtobb_konyv_kiadonkent=0
legtobb_konyv_kiadoja = []

konyvek_kiadoi=[]

for konyv in konyvek:
    konyvek_kiadoi.append(konyv['Kiadó'])

for kiado in konyvek_kiadoi:
    if konyvek_kiadoi.count(kiado) > legtobb_konyv_kiadonkent:
        legtobb_konyv_kiadonkent = konyvek_iroi.count(kiado)
        legtobb_konyv_kiadoja.append(kiado)

    elif konyvek_iroi.count(kiado) == legtobb_konyv_kiadonkent:
        legtobb_konyv_kiadoja.append(kiado)

legtobb_konyv_kiadoja = set(legtobb_konyv_kiadoja)


print(f"1. A beolvasott fájlban összesen {konyek_szama} könyv szerepel.")
print(f"2. A legtöbb oldalas könyv: {legtobb_konyv_oldalszam_konyv }")
print(f"3. A legkevesebb oldalas könyv: {legkevesebb_oldalszam_konyv} ")
print(f"4. A legtöbb könyvet író szerző: {legtobb_konyv_iroi}")
print(f"5. Az átlagos oldalszám: {atlag:.2f}")
print(f"***A legtöbb könyvet kiadó kiadó: {legtobb_konyv_kiadoja}")