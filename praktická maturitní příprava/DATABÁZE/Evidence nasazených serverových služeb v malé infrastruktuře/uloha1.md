# Určení entitních a vztahových typů

### Entitní typy:

    1. **servers** (fyzické/vyrtuální stroje)
    2. **services** (software/služby)
    3. **deployment** (nasazení služeb na servery)

### Vztahové typy:

    1. **servers** -> **deployment**
    2. **services** -> **deployment**

### Vysvětlení:

    Tyto entytní a vztahové typy jsem zvolil právě pro to, aby každý server mohl mít více služeb a zároveň každá služba mohla být na více serverech přičemž v entitě **deployment** se eviduje jaký server má učité služby a na jakých serverech je určitá služba. Tím že na toto je zvlášť entita **deployment** tak se v ní také může určit v jamém režimu služba na daném serveru běží a kdy byla na serveru spuštěna do provozu.

### Odpověď na otázku k zamyšlení (Jaký význam mají v návrhu DB entitní a vztahový typ?):

    **Entitní typ** je takový _základní kámen_ DB a každý entitní typ představuje **střed zájmu** o kterém chceme **uchovávat informace**. 

    **Vztahový typ** nám určuje jak mezi sebou dané entity(tabulky) **souvisí**. Bez toho by jsme měli jen hromadu nesouvisejících tabulek. 
