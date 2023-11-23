'''
Flask is a web framework, it's a I - Python module that lets you develop web
applications easily. It has a small and easy-to-extend core: it's a
microframework that doesn't include ORM (Object Relational Manager)
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world() -> object:
    return "Hello World!\nThis is a Flask website"


if __name__ == '__main__':
    app.run()
