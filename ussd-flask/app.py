"""
USSD Flask app using Africas Talking API
"""

from flask import Flask, request
import africastalking

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)