# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Archivist! Remain Vigilant Of Your Surroundings At All Times When Accessing The Archives!'

if __name__=='__main__': 
   app.run(debug=True) 