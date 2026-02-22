class Account:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.history = [f"Počáteční stav: {initial_balance} Kč"]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Vklad: +{amount} Kč")
            print(f"Vloženo {amount} Kč.")
        else:
            print("Částka musí být kladná.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Částka musí být kladná.")
        elif amount > self.balance:
            print("Transakce zamítnuta: Nedostatečný zůstatek!")
        else:
            self.balance -= amount
            self.history.append(f"Výběr: -{amount} Kč")
            print(f"Vybráno {amount} Kč.")

    def show_history(self):
        print("\n--- Historie transakcí ---")
        for record in self.history:
            print(record)
        print(f"Aktuální zůstatek: {self.balance} Kč")

def main():
    try:
        start_money = float(input("Zadejte počáteční vklad pro otevření účtu: "))
        my_account = Account(start_money)
    except ValueError:
        print("Neplatný vstup, začínáme s 0 Kč.")
        my_account = Account(0)

    while True:
        print("\n--- Bankovní systém ---")
        print("1. Zobrazit zůstatek a historii")
        print("2. Vložit peníze")
        print("3. Vybrat peníze")
        print("4. Konec")
        
        volba = input("Vyberte akci: ")

        if volba == "1":
            my_account.show_history()
        elif volba == "2":
            try:
                castka = float(input("Částka k vložení: "))
                my_account.deposit(castka)
            except ValueError:
                print("Chyba: Zadejte číslo.")
        elif volba == "3":
            try:
                castka = float(input("Částka k výběru: "))
                my_account.withdraw(castka)
            except ValueError:
                print("Chyba: Zadejte číslo.")
        elif volba == "4":
            print("Děkujeme, že využíváte naše služby. Nashledanou!")
            break
        else:
            print("Neplatná volba.")

if __name__ == "__main__":
    main()