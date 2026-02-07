# Diagram výskytu entit a vztahů

### Kardinalita vztahů:

1. servers **1:N** deployment
2. services **1:N** deployment

### Parcialita entit ve ztahu:

1. Vztah:
    - servers (nepoviná)
    - deployment (poviná)
2. Vztah:
    - services (nepoviná)
    - deployment (poviná)

[ SERVERS ]                 [ DEPLOYMENT ]                [ SERVICES ]
+-------------+             +----------------+             +--------------+
| ID (PK)     |             | ID (PK)        |             | ID (PK)      |
| name        |----0------<-| server_ID (FK) |             | services     |
| CPU         |             | service_ID (FK)|->------0----|              |
| GPU         |             | date           |             +--------------+
| RAM         |             | status         |
| Disk        |             +----------------+
| Motherboard |
+-------------+

### Otázka k zamyšlení(Proč určujeme kardinalitu a parcialitu vztahů?):

Kardinalita a parcialita jsou takové pravidla pro to jak se k sobě mají entity chovat. 