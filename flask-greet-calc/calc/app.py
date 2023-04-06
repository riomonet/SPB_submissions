from flask import Flask, request
import operations

app = Flask(__name__)

@app.route("/add")
def add():
    a = int(request.args['a'])
    b = int (request.args['b'])
    sum = operations.add(a,b)
    return str(sum)


@app.route("/sub")
def sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    difference = operations.sub(a,b)
    return str(difference)


@app.route("/mult")
def mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    product = operations.mult(a,b)
    return str(product)


@app.route("/div")
def div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    quotient = operations.div(a,b)
    return str(quotient)

@app.route("/math/<operation>")
def math(operation):

    a = int(request.args['a'])
    b = int(request.args['b'])
    ans =  op[operation](a,b)
    return str(ans)

op = {'add': operations.add, 'sub': operations.sub, 'mult' :  operations.mult, 'div': operations.div}






