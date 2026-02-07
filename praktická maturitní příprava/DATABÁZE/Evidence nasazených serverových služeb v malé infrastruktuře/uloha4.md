# Datové typy a integritní omezení

## Tabulkový přehled atributů

### Servers

| Atribut     | Datový typ  | Integritní omezení          | Význam                              | 
| :---------- | :---------: | :-------------------------: | :---------------------------------- | 
| ID          | INT         | PRIMARY KEY, AUTO_INCREMENT | Unikátní identifikační klíč serveru | 
| name        | VARCHAR(45) | NOT NULL, UNIQUE            | Unikátní název serveru              | 
| Motherboard | VARCHAR(45) | NOT NULL                    | Model základní desky                | 
| RAM         | VARCHAR(45) | NOT NULL                    | Kapacita ram                        | 
| CPU         | VARCHAR(45) | NOT NULL                    | Model procesoru                     | 
| GPU         | VARCHAR(45) | NULL                        | Model grafiky                       | 
| Disk        | VARCHAR(45) | NOT NULL                    | Kapacita a typ disku                | 

### Services

| Atribut  | Datový typ  | Integritní omezení          | Význam                             | 
| :------- | :---------: | :-------------------------: | :--------------------------------- | 
| ID       | INT         | PRIMARY KEY, AUTO_INCREMENT | Unikátní identifikační klíč služby | 
| services | VARCHAR(45) | NOT NULL, UNIQUE            | Název služby                       | 

### Deployment

| Atribut    | Datový typ                        | Integritní omezení          | Význam                   | 
| :--------- | :-------------------------------: | :-------------------------: | :----------------------- | 
| ID         | INT                               | PRIMARY KEY, AUTO_INCREMENT | ID záznamu o nasazení    | 
| server ID  | INT                               | NOT NULL, FOREIGN KEY       | Odkaz do entity servers  | 
| service ID | INT                               | NOT NULL, FOREIGN KEY       | Odkaz do entity services | 
| date       | DATE                              | NOT NULL                    | Datum nasazení serveru   | 
| status     | ENUM('production', 'development') | NOT NULL, CHECK             | Stav serveru             | 