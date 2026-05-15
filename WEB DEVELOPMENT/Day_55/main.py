from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello():
#     return "<h1 style='text-align: center'> Hello </h1>" \
#         "<p>'This para is just for testing'</p>'" \
#         "<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1tYtejtOJ1Y0Z_7mqaN062K1UEMlPiy3vCw&s'>"


# @app.route('/username/<username>')
# def greeting(name):
#     return f"{hello()} {name}"

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def make_emphasis(func):
    def wrapper(*args, **kwargs):
        result = f"<em>{func(*args, **kwargs)}</em>"
        return result
    return wrapper


def make_underlined(func):
    def wrapper(*args, **kwargs):
        result = f"<u>{func(*args, **kwargs)}</u>"
        return result
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def task():
    return "This is a task realated to the decarotar"


if __name__ == '__main__':
    app.run(debug=True)
