#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

# append to app/app.py

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:student>')
def print_string(student):
    print(student)
    return student

@app.route('/count/<int:param>')
def count(param):
    numbers=""
    for num in range(0,param):
        numbers = numbers+str(num)+'\n' 
    print(numbers) 
    return numbers

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    result=0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    else:
        result = num1 % num2
    
    return str(result)