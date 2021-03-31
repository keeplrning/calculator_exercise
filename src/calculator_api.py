import flask
from flask import request
from src.calculator import calculate_pre, calculate_infix

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return '<h1>Hello from Calc Server!</h1>'


@app.route('/api/v1/calculate_prefix', methods=['GET'])
def calculate_p():
    if 'expression' in request.args:
        exp = request.args['expression']
        return '<h1>Calculation Results - {}'.format(calculate_pre(exp))
    else:
        return 'Invalid Request!'


@app.route('/api/v1/calculate_infix', methods=['GET'])
def calculate_i():
    if 'expression' in request.args:
        exp = request.args['expression']
        return '<h1>Calculation Results - {}'.format(calculate_infix(exp))
    else:
        return 'Invalid Request!'


app.run()