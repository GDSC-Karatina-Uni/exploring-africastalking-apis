"""
USSD Flask app using Africas Talking API
We will create a simple USSD app that will enable GDSC members to register for the GDSC community
"""

from flask import Flask, request
import africastalking
# sqlite3
import sqlite3
from flask import g

database = 'ussd.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Initialize the SDK
username = "sandbox"    # use 'sandbox' for development in the test environment

# membership table

app = Flask(__name__)

response = ""

@app.route('/ussd/', methods=['POST', 'GET'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == "":
        # This is the first request. Note how we start the response with CON
        response = "CON Welcome to GDSC\n"
        response += "1. Register\n"
        response += "2. Exit"

    elif text == "1":
        # Business logic for first level response
        response = "CON Enter your name\n"

    elif text == "2":
        # Business logic for first level response
        # This is a terminal request. Note how we start the response with END
        response = "END Thank you for using GDSC services"

    else:
        # This is a second level response where the user selected 1 in the first instance
        if text.split("*")[0] == "1":
            # Business logic for second level response
            name = text.split("*")[1]
            # Save the user to the database
            c = get_db().cursor()
            c.execute("INSERT INTO membership (name, phone_number) VALUES (?, ?)", (name, phone_number))
            get_db().commit()
            response = "END You have been registered successfully"


    # Print the response onto the page so that our gateway can read it
    return response

app.teardown_appcontext(close_db)


@app.route('/registered/', methods=['GET'])
def registered():
    c = get_db().cursor()
    c.execute("SELECT * FROM membership")
    members = c.fetchall()
    return str(members)


if __name__ == '__main__':
    app.run(debug=True)


