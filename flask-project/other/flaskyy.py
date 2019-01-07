
from flask import make_response
from flask import Flask
from flask import request
from flask import redirect
from flask import abort
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://www.baidu.com')
    #response = make_response('<h1>This document carries a cookie!</h1>')
    #response.set_cookie('answer','42')
    #return response
    #return '<h1>Bad Request</h1>',400
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s </p>' % user_agent
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' % name
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello,%s</h1>' % user.name


if __name__ == '__main__':
    app.run(debug=True)
