from bottle import route, run, template, request


@route('/hello')
def hello():
    return template('pybot_template04', text='')


@route('/hello', method='POST')
def do_hello():
    input_text = request.forms.input_text
    return template('pybot_template04', text=input_text)


run(host='localhost', port=8080, debug=True)
