# Vytvoření databáze

![Diagram vytvořené databáze](image_uloha7.png "Diagram vytvořené databáze")

## Otazky k zamyšlení

1. Jaký SW resp. služby jsou potřeba k vytvoření relační databáze?
    - Jsou tři hlavní SW které potřebujeme pro vytvoření relační databáze.
        1. **SŘBD** (Systém řízení báze dat) - Ukládá data, hlída vztahy mezi entitami a vykonává příkazi.
        2. **Jazyk SQL** - I když ho nemusíme psat ručně tak je to jediná řeč které SŘBD rozumí tudíž je potřeba
        3. **Server** - Databázový engine musí někda běžet ať už na cloudovém serveru nebo fyzickém
2. Které z nich jsou nezbytné a které pomocné?
    - Pomocné:
        1. Administrační nástroje (phpMyAdmin, ...)
        2. Modelovací nástroje (draw.io, ...)
        3. Ovladače (**PDO** pro PHP, **JDBC** pro Javu, ...)