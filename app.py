import datetime, random
from flask import Flask, render_template

app = Flask(__name__)

def quotes():
 sampleList = ["a", "b", "c"]
 x = random.choice(sampleList)
 print(x)

@app.route('/')
def hello():
    return render_template('index.html', quote=quotes())