from flask import Flask, render_template
import requests
from post import Post

blog_post = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
blog_object = []
for each in blog_post:
    post = Post(each['id'], each['title'], each['subtitle'], each['body'])
    blog_object.append(post)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_object)


@app.route('/post/<number>')
def post_blog(number):

    for each in blog_object:
        if int(number) == each.id:
            return render_template('post.html', blog=each)


if __name__ == "__main__":
    app.run(debug=True)
