magazyn = {
    "jedzenie" :  {
        "japko" : 10,
        "bulka" : 12,
        "kot" : 11,
    },


    "picia" : {
        "woda" : 3,
        "woda G" : 4,
        "koka kola 1l" : 12,
    },

    "słodycze" : {
        "lukrecja" : 12,
        "japko w karmelu" : 12,
        "pjanki" : 13,
    }
}



def dodanie():
    typ = input("jaki to jest typ produktu ")
    cos = input("dodaj produkt ")
    ile = input("podaj ilość ")
    magazyn[typ][cos] = ile

def usuwanie():
    co = input("jaki typ to jest? ")
    co1 = input("co chcesz usunac ? ")
    del magazyn[co][co1]
    print(f"usunieto produkt")

def sprawdz():
    ps = input("jaki przedmiot ")
    for kategoria, produkt in magazyn.items():
        for produkt, ilosc in magazyn.items():
            if ps == produkt.lower() or ps in produkt.lower():
                print(f"'{produkt}' jest w kategorii '{kategoria}', ilosc: '{ilosc}' ")
                return
    print(f"produkt '{ps}' nie istnieje w magazynie")
    


while True:
    print("wybierz opcje")
    print("dodaj produkt : A")
    print("usun produkt : B")
    print("wyświetl wszystkie produkty : C")
    print("wyświetl dostepne produkty : D")
    opcja = input("podaj wartośc: ")
    if opcja == ("A"):
        dodanie()
    if opcja == ("B"):
        usuwanie()
    if opcja == ("C"):
        print(magazyn)
    if opcja == ("D"):
        sprawdz()

        

