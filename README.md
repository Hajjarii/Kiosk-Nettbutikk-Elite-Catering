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










DOKUMENTASJON:
Eksamen dokumentasjon

  1. Jeg startet med å sette opp github repository med kanban board for å enkelt holde styr på hva jeg gjør og skal gjøre.
  2. Deretter begynnte jeg på mariadb med å sette opp database med verdier i en produkt tabell. Jeg sattet opp flask server imens så arbeidet synkroniserte seg med flask.
  3. Det var litt problemer med pushing til github så jeg brukte AI til å hjelpe.
     Det var også noen problemer med hosting av flask serveren fordi det var en feilmelding i koden, funksjonen "def hjem()" hadde ikke noe return_template, så den viste ikke hva den skulle vise. Fikset med å skrive det på slutten av funksjonen. (Brukte ai hjelp til å finne feilen)
4. Stylet nettsiden litt.
