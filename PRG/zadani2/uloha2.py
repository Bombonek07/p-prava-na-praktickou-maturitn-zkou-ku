class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def info(self):
        return f"'{self.title}' - {self.pages} stran"

def najdi_nejdelsi(seznam_knih):
    if not seznam_knih:
        return None
    
    return max(seznam_knih, key=lambda kniha: kniha.pages)

knihovna = []

while True:
    print("\n1. Přidat knihu | 2. Vypsat vše | 3. Nejdelší kniha | 4. Konec")
    volba = input("Vyber akci: ")

    if volba == "1":
        t = input("Název: ")
        p = int(input("Počet stran: "))
        knihovna.append(Book(t, p))
        print("Kniha byla uložena.")

    elif volba == "2":
        print("\n ---Seznam knih---")
        for k in knihovna:
            print(k.info())

    elif volba == "3":
        nej = najdi_nejdelsi(knihovna)
        if nej:
            print(f"\nNejdelší kniha je: {nej.info()}")
        else:
            print("Knihovna je prázdná.")

    elif volba == "4":
        break