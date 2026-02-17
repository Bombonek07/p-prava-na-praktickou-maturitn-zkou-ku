book = input("Zadej název knihy: ")
pages = int(input("Zadej počet stran: "))

if pages < 100:
    print(f"Kniha '{book}' je krátká.")
elif 100 <= pages <= 300:
    print(f"Kniha '{book}' je středně dlouhá.")
else:
    print(f"Kniha '{book}' je dlouhá.")
