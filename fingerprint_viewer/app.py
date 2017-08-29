from flask import Flask
from flask import render_template
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('line_basic.html')

@app.route('/bubble')
def bubble():
    return render_template('bubble_basic.html')

@app.route('/getretina', methods=['GET', 'POST'])
def get_retina():
    print "WE ARE IN GETRETINA"
    data = [{ "x": 10, "y": 10, "z": 100 }]
    jdatas = json.dumps(data)
    print jdatas
    return jdatas

if __name__ == '__main__':
  app.run('0.0.0.0', 8080)
