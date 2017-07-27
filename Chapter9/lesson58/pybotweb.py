from bottle import route, run, template
from datetime import datetime


@route('/hello')
def hello():
    now = datetime.now()
    return template('pybot_template', now=now)


run(host='localhost', port=8080, debug=True)
