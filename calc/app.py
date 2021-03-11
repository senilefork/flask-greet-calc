from operations import add, sub, mult, div
from flask import Flask, request


app = Flask(__name__)

@app.route('/add')
def add_1():
    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = add(a,b)
    return f"<h1>{answer}</h1>"

@app.route('/sub')
def sub_1():
    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = sub(a,b)
    return f"<h1>{answer}</h1>"

@app.route('/mult')
def mult_1():
    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = mult(a,b)
    return f"<h1>{answer}</h1>"

@app.route('/div')
def div_1():
    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = div(a,b)
    return f"<h1>{answer}</h1>"

operationsDict = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def math_op(operation):
     a = int(request.args["a"])
     b = int(request.args["b"])
     answer = operationsDict[operation](a,b)
     return f"<h1>{answer}</h1>"





