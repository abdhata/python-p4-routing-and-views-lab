#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

# append to app/app.py

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<studentname>')
def student(studentname):
    print(f'This is the student details for {studentname}')
    return f'<h1>Student details for {studentname}</h1>'