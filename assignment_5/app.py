# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os
from flask import Flask, render_template
import psycopg2


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
assignment = "Assignment 5"

# Retrieve database connection parameters from environment variables
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PA$SWORD")
DB_HOST = os.environ.get("DB_HO$T")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")


def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return conn

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")
def webpage_display():
    try:
        conn = get_db_connection()

    except psycopg2.Error as err:
        return render_template("fail.html", words=err.pgerror, title=assignment)

    else:
        cur = conn.cursor()
        cur.execute('SELECT * FROM col;')
        words = cur.fetchall()
        return render_template("pass.html", words=words, title=assignment)


# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")
