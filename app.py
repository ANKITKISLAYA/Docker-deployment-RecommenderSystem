# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:03:17 2020

@author: Ankit
"""

import flask
from flask import request, jsonify, url_for


from RecSys import RecSys
from RecSys1 import RecSys1
from RecSys2 import RecSys2


import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


app = flask.Flask(__name__)
app.debug = False


sentry_sdk.init(
    dsn="https://d4f55392a9aa4f78a816e498c88fb5c3@sentry.io/1873356",
    integrations=[FlaskIntegration()]
)



@app.route('/recsysitem')
def recsysitem():
    
    itemid = request.args['itemid']
    number = request.args['number']
    
    jso=RecSys().rec(itemid,number)
    return jsonify(jso)
	


@app.route('/recsysitem1')
def recsysitem1():
    
    itemid = request.args['itemid']
    number = request.args['number']
    wid = request.args['warehouseid']
    jso=RecSys1().rec(itemid,number,wid)
    return jsonify(jso)

@app.route('/recsysitem2')
def recsysitem2():
    
    itemid = request.args['itemid']
    number = request.args['number']
    wid = request.args['warehouseid']
    jso=RecSys2().rec(itemid,number,wid)
    return jsonify(jso)



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)











