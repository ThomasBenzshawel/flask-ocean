from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello MSOE, my name is Thomas Benzshawel! Don not click this link: https://www.youtube.com/watch?v=dQw4w9WgXcQ'


if __name__ == '__main__':
    app.run(debug=True)
