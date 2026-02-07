# Určení atributů + normalizace (1. a 2. NF)

### Atributy entit:

    1. **servers**
        - ID (PK)
        - name
        - CPU
        - GPU
        - RAM
        - Disk
        - Motherboard

    2. **services**
        - ID (PK)
        - services

    3. **deployment**
        - ID (PK)
        - servers ID (FK)
        - services ID (FK)
        - date
        - status

### Normalizační formy:

    1. NF
        - Podle 1. NF by v entitě **services** mělo být místo atributu _services_ (který zahrnuje všechny služby, např.: firewall, DNS, webserver, ...) atribut pro každou službu zvlášť. 

    2. NF
        - Podle 2. NF musí všechny atributy v entitě souviset s PK entity. 
        - Kdyby entita **deployment** neměla vlastní ID(PK), ale měla by složený PK z atributů _servers ID(FK)_ a _services ID(FK)_ tak by to nebylo zprávně protože atributy _date_ a _status_ se vztahují na PK(v tomto případě ID) a nemohou se vztahovat na složený PK(v případě kdy by entita neměla vlastní PK ale jen složený ze dvou FK). 

### Otázky k zamyšlení:

    1. **Jaký význam mají v relačním modelu atributy?**
        - Atributy jsou **vlastnosti**(nebo také sloupce v tabulce) dané entity. 
        - Mohou to být jen informace o dané entitě definující data a nebo také specialní atributy jako **PK** nebo vazbové atributy **FK**. 

    2. **Proč provádíme normalizaci databáze?**
        - Normalizaci databáse děláme pro to aby byla databáze bezpečná a efektivní a abychom se vyhli třem hlavním problémům (anomáliím). 