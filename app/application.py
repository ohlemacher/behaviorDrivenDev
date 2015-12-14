#!/usr/bin/env python

#curl -i -H "Accept: application/json" http://127.0.0.1:5000/users
#curl -i -H "Accept: application/json" http://127.0.0.1:5000/users/zero01
#curl -i -H "Accept: application/json" -X POST -d "firstName=james" http://localhost:5000/persons/person
#curl -i -H "Accept: application/json" -X DELETE http://localhost:5000/users/users/zero01

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

USERS = {
    'jack01': {'name': 'Jack'},
    'zero00': {'name': 'Zero'},
    'seth02': {'name': 'Seth'},
}

GET = 'GET'
DELETE = 'DELETE'

@app.route("/users/<username>", methods=[GET, DELETE])
def access_users(username):
    # GET
    if request.method == GET:
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            response = make_response(
                'User %s not found' % username,
                404)
            return response
    # DELETE
    elif request.method == DELETE:
        try:
            #global USERS
            user_details = USERS.get(username)
            del USERS[username]
            #return jsonify({'deleted': username})
            response = make_response(
                'User %s deleted' % username,
                200)
            return response
        except KeyError:
            #print 'KeyError'
            response = make_response(
                'User %s not found to delete' % username,
                404)
            return response
        except Exception as e:
            #print 'Unknown', e
            response = make_response(
                'Unknown error',
                500
            )
            return response
    # No support
    else:
        return Response(status=404)

@app.route("/users", methods=[GET])
def users():
    return jsonify(USERS)

@app.route("/")
def welcome():
    return "Welcome to my Behavior Driven Development REST server"


if __name__ == '__main__':
    app.debug = True
    app.run()

