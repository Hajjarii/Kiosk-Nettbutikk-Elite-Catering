from flask import Flask, render_template
import mariadb
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route('/')
def hjem():
    with mariadb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host="localhost",
            port=3306,
            database=os.getenv("DB_NAME") ) as conn:

            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM produkter")
            produkter = mycursor.fetchall()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
