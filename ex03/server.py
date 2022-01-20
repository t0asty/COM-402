from flask import Flask, request, make_response
from hashlib import sha256
import hmac
from base64 import b64encode, b64decode

app = Flask(__name__)

cookie_name = "LoginCookie"

@app.route("/login",methods=['POST'])
def login():
    secret_key = 'very_very_secret'
    args = request.form
    user = args['username']
    password = args['password']
    
    if user == 'admin' and password == '42':
        cookie_txt = "{},{},com402,hw2,ex2,admin,".format(user, password)
    else:
        cookie_txt = "{},{},com402,hw2,ex2,user,".format(user, password)
    h = hmac.new(secret_key.encode(), cookie_txt.encode(), sha256)
    cookie_txt += str(h.hexdigest())

    resp = make_response()
    resp.set_cookie('LoginCookie',b64encode(cookie_txt.encode()))
    return resp

@app.route("/auth",methods=['GET'])
def auth():
    secret_key = 'very_very_secret'
    if 'LoginCookie' not in request.cookies:
        return "Fail", 403
    else:
        cookie_val = b64decode(request.cookies.get('LoginCookie')).decode()
        if len(cookie_val.split(',')) != 7:
            return "Bruh, gib dir Mühe", 403
        cookie_hmac = cookie_val.split(',')[-1]
        cookie_txt = ','.join(cookie_val.split(',')[:-1]) + ','
        h = hmac.new(secret_key.encode(), cookie_txt.encode(), sha256)
        if str(h.hexdigest()) != cookie_hmac:
            return "Du Wicht!", 403
        else:
            if cookie_val.split(',')[5] == 'admin':
                return "Mylord", 200
            else:
                return "Hallo, du Knecht", 201


if __name__ == '__main__':
    app.run()