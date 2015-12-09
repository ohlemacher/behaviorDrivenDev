#from application import app
#
#
#USERS = {'jack01': {'name': 'Jack'}}
#
#GET = 'GET'
#
#@app.route("/user/<username>") #, methods=[get])
#def access_users(username):
#    print('access_users()')
#    if request.method == GET:
#        user_details = USERS.get(username)
#        print 'user_details:', user_details
#        if user_details:
#            return jsonify(user_details)
#        else:
#            return Response(status=404)
