from bottle import template

response = template('こんにちは {{name}} さん', name='たかのり')
print(response)
response = template('こんにちは {{name}} さん', name='みつき')
print(response)
