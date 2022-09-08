from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
<<<<<<< HEAD
    return "Web App with Python Flask! and stuff"
=======
    return "Halló heimur(Nú í íslenskum texta)"
>>>>>>> Texti-change

app.run(host='0.0.0.0', port=81)