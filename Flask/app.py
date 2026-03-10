from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database-innstillinger
DB_HOST = '10.2.0.74'
DB_USER = 'kioskbruker'
DB_PASSWORD = '123123'  # Passordet du lagde i Del 3A
DB_NAME = 'kiosk'

def koble_til_db():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/')
def hjem():
    db = koble_til_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produkter")
    produkter = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', produkter=produkter)

if __name__ == '__main__':
    app.run(debug=True)