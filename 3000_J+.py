class Tanulo:
    csoportok = ['alfa', 'beta', 'gamma']
    def __init__(self, tanulokod:int, nev:str, matinfcsop:str, angolcsop:str, masodiknyelv:str, nem:str, csalad:int, testverek:int):
        self.tanulokod = tanulokod
        self.nev = nev
        self.matinfcsop = matinfcsop
        self.angolcsop = angolcsop
        self.masodiknyelv = masodiknyelv
        self.nem = nem
        self.csalad = csalad
        self.testverek = testverek

    def __repr__(self) -> str:
        return self.nev


def beolvas():
    lista = []
    with open("input.txt", encoding="utf8") as f:
        for sor in f:
            sortomb = sor.strip().split(';')
            lista.append(Tanulo(int(sortomb[0]), sortomb[1], sortomb[2], sortomb[3], sortomb[4], sortomb[5], int(sortomb[6]), int(sortomb[7])))
    return lista

tanulok = beolvas()

# 1. feladat
def hanydiak():
    print(f'Összesen {len(tanulok)} diák tanul az osztályban.')
#hanydiak()

# 2-3. feladat
def hanyfiulany(neme):
    db = 0
    for tanulo in tanulok:
        if tanulo.nem == neme:
            db += 1
    if neme == 'F':
        print(f'Az osztályba {db} fiú jár.')
    else:
        print(f'Az osztályba {db} lány jár.')
#hanyfiulany('F')

# 4, 6. feladat
def tobb_mint_x_testver(testverszam):
    db = 0
    for tanulo in tanulok:
        if tanulo.testverek > testverszam:
            db += 1
    print(f'Az osztályba {db} olyan diák jár, akinek több testvére is van.')
#tobb_mint_x_testver(1)

# 5, 7. feladat
def tobb_mint_x_testver_nev(testverszam):
    for tanulo in tanulok:
        if tanulo.testverek > testverszam:
            print(str(tanulo))
#tobb_mint_x_testver_nev(1)

#8. feladat
def hany_nemetet_tanul():
    db = 0
    for tanulo in tanulok:
        if tanulo.masodiknyelv == 'német':
            db += 1
    print(f'Második nyelvnek {db} diák tanul németet.')
#hany_nemetet_tanul()

# 9. feladat
def hany_nemetet_tanul_nev():
    for tanulo in tanulok:
        if tanulo.masodiknyelv == 'német':
            print(str(tanulo))
#hany_nemetet_tanul_nev()

# 10-11. feladat
def hanyan_angol_csoport(csoport):
    db = 0
    for tanulo in tanulok:
        if csoport in tanulo.angolcsop:
            db += 1
    print(f'{db} diák jár a(z) "{csoport}." angol csoportba.')
#hanyan_angol_csoport('2')

# 12-17. feladat
def hanyan_matek_ab(neme, csoport):
    db = 0
    if neme == 'FL':
        for tanulo in tanulok:
            if tanulo.matinfcsop == csoport:
                db += 1
        return print(f'Összesen {db} diák jár a(z) {csoport} matek/informatika csoportba.')
    elif neme == 'F':
        for tanulo in tanulok:
            if tanulo.matinfcsop == csoport:
                if tanulo.nem == neme:
                    db += 1
        return print(f'Összesen {db} fiú jár a(z) {csoport} matek/informatika csoportba.')
    else:
        for tanulo in tanulok:
            if tanulo.matinfcsop == csoport:
                if tanulo.nem == neme:
                    db += 1
        return print(f'Összesen {db} lány jár a(z) {csoport} matek/informatika csoportba.')
#hanyan_matek_ab('FL', 'alfa')

# 18-20. feladat
def tanul_e_nyelvet(nyelv):
    van = False
    for tanulo in tanulok:
        if tanulo.masodiknyelv == nyelv:
            van = True
    if van:
        print(f'Van olyan diák, aki {nyelv} nyelvet tanul.')
    else:
        print(f'Nincs olyan diák, aki {nyelv} nyelvet tanul.')
#tanul_e_nyelvet('spanyol')

# 21. feladat
def legnagyobb_csalad():
    db = 0
    for tanulo in tanulok:
        if tanulo.csalad > db:
            db = tanulo.csalad
    return db
#print(f'Az osztályban a legnagyobb család {legnagyobb_csalad()} főből áll.')

# 22. feladat
def valaki_akinek_legtobb_testver():
    for tanulo in tanulok:
        if tanulo.csalad == legnagyobb_csalad():
            return print(f'{tanulo.nev} diáknak van a legnagyobb családja.')
#valaki_akinek_legtobb_testver()

# 23. feladat
def lany_angolcsoport():
    for tanulo in tanulok:
        if tanulo.nem == 'L':
            if '1' in tanulo.angolcsop or '2' in tanulo.angolcsop:
                print(str(tanulo))
#lany_angolcsoport()

# 24. feladat
def fiu_angolcsoport_testverek():
    for tanulo in tanulok:
        if tanulo.nem == 'F':
            if '3' in tanulo.angolcsop or '4' in tanulo.angolcsop:
                if tanulo.testverek == 0 or tanulo.testverek == 2:
                    print(str(tanulo))
#fiu_angolcsoport_testverek()

# 25. feladat
def egyuttlakok_testverek_kulonbseg_nemharom():
    db = 0
    for tanulo in tanulok:
        if tanulo.csalad - tanulo.testverek != 3:
            db += 1
    print(f'Azon családok száma, ahol az együttlakók és a testvérek különbsége nem 3: {db}')
#egyuttlakok_testverek_kulonbseg_nemharom()

# 26-29 feladat
def hianyzott_angolrol(neve):
    csoport = ''
    for tanulo in tanulok:
        if tanulo.nev == neve:
            csoport = tanulo.angolcsop
    for tanulo in tanulok:
        if tanulo.angolcsop == csoport and tanulo.nev != neve:
            print(str(tanulo))
#hianyzott_angolrol('Hát Izsák')

# 31. feladat
def spanyol_nemet_tobben():
    spanyol = 0
    nemet = 0
    for tanulo in tanulok:
        if tanulo.masodiknyelv == 'spanyol':
            spanyol += 1
        elif tanulo.masodiknyelv == 'német':
            nemet += 1
    if spanyol > nemet:
        print('Az osztályban többen tanulnak spanyolt mint németet.')
    elif spanyol < nemet:
        print('Az osztályban többen tanulnak németet mint spanyolt.')
    else:
        print('Az osztályban ugyan annyian tanulnak spanyolt mint németet.')
#spanyol_nemet_tobben()

# 32. feladat
def adott_nyelv_nevsor():
    nyelv = input("Adjon meg egy nyelvet: ")
    if nyelv == 'angol':
        for tanulo in tanulok:
            print(str(tanulo))
        return ''
    for tanulo in tanulok:
        if tanulo.masodiknyelv == nyelv:
            print(str(tanulo))
#adott_nyelv_nevsor()

# 33. feladat
def hany_masodik_nyelv():
    result = []
    for tanulo in tanulok:
        if tanulo.masodiknyelv not in result:
            result.append(tanulo.masodiknyelv)
    print(result)
#hany_masodik_nyelv()

# 34. feladat
def matinf_csoportok():
    result = []
    for tanulo in tanulok:
        if tanulo.matinfcsop not in result:
            result.append(tanulo.matinfcsop)
    print(result)
#matinf_csoportok()

# 35. feladat
def melyik_angol_hanyan():
    szotar = {'1. Sió':0, '2. Bán':0, '3. Joó':0, '4. Kis':0}
    for tanulo in tanulok:
        if tanulo.angolcsop in szotar.keys():
            szotar[tanulo.angolcsop] += 1
    print(szotar)    
#melyik_angol_hanyan()

# 36. feladat
def egyuttlakok_csoportositas():
    egyuttlakok = {1:0,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}
    for tanulo in tanulok:
        if tanulo.csalad in egyuttlakok.keys():
            egyuttlakok[tanulo.csalad] += 1
    print(egyuttlakok)
#egyuttlakok_csoportositas()

# 37. feladat
def leggyakoribb_testverszam():
    szotar = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
    for tanulo in tanulok:
        if tanulo.testverek in szotar.keys():
            szotar[tanulo.testverek] += 1
    leggyakoribb = max(szotar, key = szotar.get)
    print (f'A leggyakoribb testvérszám: {leggyakoribb}')
#leggyakoribb_testverszam()

# 38. feladat
def angolcsoportonkent_testverek():
    szotar = {'1. Sió':0, '2. Bán':0, '3. Joó':0, '4. Kis':0}
    for tanulo in tanulok:
        if tanulo.angolcsop in szotar.keys():
            szotar[tanulo.angolcsop] += tanulo.testverek
    print(szotar)
#angolcsoportonkent_testverek()

# 39. feladat
def masodik_nyelv_atlagos_testver():
    szotar = {'német':0, 'spanyol':0}
    nemetdb = 0
    spanyoldb = 0
    for tanulo in tanulok:
        if tanulo.masodiknyelv in szotar.keys():
            szotar[tanulo.masodiknyelv] += tanulo.testverek
            if tanulo.masodiknyelv == 'német':
                nemetdb += 1
            else:
                spanyoldb += 1    
    for key in szotar:
        if szotar[key] == 'német':
            szotar[key] = round(szotar[key] / nemetdb)
        else:
            szotar[key] = round(szotar[key] / spanyoldb)
    print(szotar)
#masodik_nyelv_atlagos_testver()

# 40. feladat
def angolcsop_elso_utolso():
    szotar = {}
    for tanulo in tanulok:
        if tanulo.angolcsop in szotar.keys():
            szotar[tanulo.angolcsop].append(tanulo)
        else:
            szotar[tanulo.angolcsop] = [tanulo]
    for key in szotar.keys():
        length = len(szotar[key])
        print(f'{key} --- Első: {szotar[key][0]}, utolsó: {szotar[key][length - 1]}')
#angolcsop_elso_utolso()