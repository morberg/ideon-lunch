# Warning, this project is not yet fit for public consumption
It works for me, but it is a mess.

Todo: create a scrapy pipelines that creates the .ics files.

# Hämta veckans meny, skapa en .ics-fil och öppna i kalendern

Ta bort förra veckans meny:

`rm lunch.json`

Skapa en ny json-fil för varje restaurang (just nu enbart `edison`) med `scrapy`:

`scrapy crawl edison -o lunch.json`

Kör skript för att skapa filen `Ideon Edison.ics`:

`./create-calendar-file.py`

Och öppna i kalendern:

`open Ideon Edison.ics`

Smaklig spis.