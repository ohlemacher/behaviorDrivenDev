#!/usr/bin/env python

from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {
    'jack01': {'name': 'Jack'},
    'zero00': {'name': 'Zero'},
    'seth02': {'name': 'Seth'},
}

GET = 'GET'

@app.route("/user/<username>", methods=[GET])
def access_users(username):
    if request.method == GET:
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)
    else:
        print 'Error: methon %s not support' % \
            request.method

@app.route("/users", methods=[GET])
def users():
    return jsonify(USERS)

@app.route("/")
def welcom():
    return "Welcome to my Behavior Driven Development REST server"


if __name__ == '__main__':
    app.run()
