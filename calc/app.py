from flask import Flask, request
from operations import add
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
