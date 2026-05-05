Brukerveiledning

Dette er en enkel nettbutikk som du kan installere selv og style. Jeg har laget ferdig database som kan endres på, database inneholder navn, pris, beskrivelse og mengde.

Hvordan sette opp?:

Først klon prosjektet fra github via lenke til din server host.

Sjekk at du har disse pakkene installert:

pip install mariadb
pip install flask
pip install python-dotenv

------------

Lag en .env fil i flask mappen med følgende informasjon for tilgang til database, disse kan endres på.

DB_USER=kioskbruker
DB_PASSWORD=123123
DB_NAME=kiosk

---------

Lag en environment:

1. python3 -m venv .venv
2. source .venv/bin/activate

Så er alt klart, serveren hostes på hosten sin IP-addresse
