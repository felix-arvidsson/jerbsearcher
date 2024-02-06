# jerb searcher

Script som kan schemaläggas för att övervaka nya jobbannonser på Platsbanken.
När en ny annons läggs till som inte finns i databasen, skickas ett mail till de mailadresser som har ställts in i konfigurationsfilen.
De nya annonserna sparas sedan också i databasen för framtida referens.

## förberedelse

1. Kopiera example-config.py till en ny fil med namnet config.py.
2. Skapa ett app-lösenord för Gmail och lägg in värdet i konfigurationsfilen. [Läs mer](https://support.google.com/mail/answer/185833?hl=sv)
3. Gå in på Platsbanken.se, under filter, välj kommun och yrke. I dagsläget funkar bara en kommun och yrkeskategori (Enskild kategori eller 'Välj alla yrken').
4. Kopiera URL:en, och kör skriptet `python url-disector.py '<kopierad url>'`.
5. Spara värden i config.py för occupation_field och kommun.

## Installation

```bash
git clone https://github.com/felix-arvidsson/jerbsearcher.git
cd jerbsearcher
docker-compose up --build
```

## Kontakt

felix.arvidsson [a] gmail.com
http://felix.arvidson.io/
