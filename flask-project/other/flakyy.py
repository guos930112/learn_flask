
from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from flask.ext.script import Manager
app = Flask(__name__)
@app.route('/')
def index():
    response = make_response('<h1>This Document carries a cookie!</h1>')
    response.set_cookie('gs','25')
    return response
    #return redirect('http://www.atguigu.com')
    #user_agent=request.headers.get('User-Agent')
    #return '<h1>Your Browser is %s</h1>'%user_agent

    #return '<h1>Hello New World!</h1>'

@app.route('/user/<name>')
def user(name):
    if not name:
        return 404
    return '<p>Hello,%s</p>'% name
@app.route('/pid/<int:pid>')
def pid(pid):
    if not int(pid):
        return '<p>Bad Request!</p>',400
    return '<h1>Welcom %s</h1>'%pid

if __name__ == '__main__':
    app.run(debug=True)
