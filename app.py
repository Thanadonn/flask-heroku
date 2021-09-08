from flask import Flask, jsonify
from flask import Flask, render_template

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "สวัสดี ธณดล ขันติรมย์ เลขที่1 ม.4/6 "

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/hi')
@app.route('/hello')
def hi ():
    return"สวัสดี|"
