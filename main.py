
#     instrukcjeTablica = [x[:-1] for x in dane.readlines()]        //czyści tablicę
#     dopisaneLitery = [c[1] for c in [n.split(" ") for n in instrukcjeTablica] if c[0] == "DOPISZ"]
#     print(dopisaneLitery)

instrukcje = []
tablica = []
ciagi = []
literyDop = []
wyraz = ""
licznik = 0
litera = ""

with open("instrukcje.txt") as dane:

    for wiersz in dane:

        wiersz = wiersz.strip()
        # print(wiersz)
        instrukcje.append(wiersz[:-2])
        tablica.append(wiersz)

        if wiersz.count("DOPISZ") > 0:
            wyraz = wyraz + wiersz[-1]
            # print(wyraz)
        if wiersz.count("USUN"):
            wyraz = wyraz[:-1]
        if wiersz.count("ZMIEN"):
            wyraz = wyraz[:-1] + wiersz[-1:]
        if wiersz.count("PRZESUN"):
            for i in range(0, len(wyraz)):
                if wyraz[i] == wiersz[-1:]:
                    przesuniecie = chr(ord(wyraz[i])+1)
                    tablicaNowyPrzesuniety = list(wyraz)
                    # print(tablicaNowyPrzesuniety)
                    tablicaNowyPrzesuniety[i] = przesuniecie
                    wyraz = ''.join(tablicaNowyPrzesuniety)
                    # print(wyraz)
                    if wiersz[-1:] == "Z":
                        tablicaNowyPrzesuniety = list(wyraz)
                        tablicaNowyPrzesuniety[i] = "A"
                        wyraz = ''.join(tablicaNowyPrzesuniety)
                    break

for i in range(0, len(instrukcje)):
    if instrukcje[i-1] == instrukcje[i]:
        ciagi.append(ciagi[-1]+1)
    else:
        ciagi.append(1)

for i in range(0, len(tablica)):
    if tablica[i][:-2] == "DOPISZ":
        literyDop.append(tablica[i][-1])

for i in range(0, len(literyDop)):
    if literyDop.count(literyDop[i]) > licznik:
        litera = literyDop[i]
        licznik = literyDop.count(litera)


print("Wyraz:", wyraz)
print("Dlugosc:", len(wyraz), "znakow")
print(instrukcje[ciagi.index(max(ciagi))], ", wykorzystana", max(ciagi), "razy")
print("Litera dopisywana: ", litera," --> ", licznik,"razy")

# print(instrukcje)