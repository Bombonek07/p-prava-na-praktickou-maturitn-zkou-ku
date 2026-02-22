try:
    zustatek = float(input("Zadejte počáteční zůstatek: "))
    
    print("1. Vklad")
    print("2. Výběr")
    volba = input("Vyberte operaci (1/2): ")
    castka = float(input("Zadejte částku: "))

    if volba == "1":
        # Vklad
        zustatek += castka
        print(f"Úspěšně vloženo. Nový zůstatek: {zustatek} Kč")
    elif volba == "2":
        if castka > zustatek:
            print("Chyba: Nedostatek finančních prostředků na účtu!")
        else:
            zustatek -= castka
            print(f"Výběr proveden. Nový zůstatek: {zustatek} Kč")
    else:
        print("Neplatná volba.")

except ValueError:
    print("Chyba: Zadejte prosím platné číslo.")