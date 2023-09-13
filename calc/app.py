from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)
# Put your app in here.

@app.route("/add")
def add_nums():
    """Adds two numbers, a&b in query str"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    # return f"a={a} b={b}"
    result = add(a,b)
    return str(result)

@app.route("/sub")
def sub_nums():
    """Subtract two numbers, a&b in query str"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    # return f"a={a} b={b}"
    result = sub(a,b)
    return str(result)

@app.route("/mult")
def mult_nums():
    """Multiply two numbers, a&b in query str"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a,b)
    return str(result)

@app.route("/div")
def div_nums():
    """Subtract two numbers, a&b in query str"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    # return f"a={a} b={b}"
    result = div(a,b)
    return str(result)

@app.route("/math/<operation>")
def all_ops(operation):
    """Function where user chooses math operation to run.  Returns result"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    math_dict={"add":add, "sub":sub, "mult":mult, "div":div,}
    result=math_dict[operation](a,b)
    return str(result)
        
    