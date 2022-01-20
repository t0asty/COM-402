#!/usr/bin/env python3
import populate
from flask import Flask
from flask import request, jsonify
import pymysql


app = Flask(__name__)
username = "root"
password = "root"
database = "hw5_ex2"

# This method returns a list of messages in a json format such as
# [
# { "name": <name>, "message": <message> },
# { "name": <name>, "message": <message> },
# ...
# ]
# If this is a POST request and there is a parameter "name" given, then only
# messages of the given name should be returned.
# If the POST parameter is invalid, then the response code must be 500.


@app.route("/messages", methods=["GET", "POST"])
def messages():
    with db.cursor() as cursor:
        if request.method == 'POST':
            name = request.form.get('name')
            if name is not None:
                name = name.replace('"','')
                name = name.replace("'",'')
                prep_statement = 'SELECT name, message FROM messages WHERE name = "{}";'.format(name)
                cursor.execute(prep_statement)
                entries = cursor.fetchall()
                json = [{'name': entry[0], 'message': entry[1]} for entry in entries]
            else:
                return "param name missing", 500
        else:
            # method == 'GET'
            cursor.execute('SELECT name, message FROM messages;')
            entries = cursor.fetchall()
            json = [{'name': entry[0], 'message': entry[1]} for entry in entries]
        return jsonify(json), 200


# This method returns the list of users in a json format such as
# { "users": [ <user1>, <user2>, ... ] }
# This methods should limit the number of users if a GET URL parameter is given
# named limit. For example, /users?limit=4 should only return the first four
# users.
# If the paramer given is invalid, then the response code must be 500.
@app.route("/users", methods=["GET"])
def contact():
    with db.cursor() as cursor:
        # your code here
        lim = request.args.get('limit')
        if lim is not None:
            try:
                lim = int(lim)
                if lim < 1:
                    raise ValueError
                lim = str(lim)
            except:
                return 'Invalid limit', 500
            prep_statement = 'SELECT name FROM users LIMIT {};'.format(lim)
            print(prep_statement)
            cursor.execute(prep_statement)
            users = cursor.fetchall()
            json = {'users': users}
        else:
            cursor.execute('SELECT name FROM users;')
            users = cursor.fetchall()
            json = {'users': users}
        return jsonify(json), 200


if __name__ == "__main__":
    db = pymysql.connect("localhost",
                         username,
                         password,
                         database)
    with db.cursor() as cursor:
        populate.populate_db(cursor)
        db.commit()
    print("[+] database populated")

    app.run(host='0.0.0.0', port=80)
