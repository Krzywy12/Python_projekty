from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Witaj,swiecie!Ahoj"

app.run(port='8000')

