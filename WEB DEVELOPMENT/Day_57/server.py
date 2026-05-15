from flask import Flask, render_template
import random
import requests
import datetime as dt


app = Flask(__name__)


@app.route('/')
def home():
    num = random.randint(0, 10)
    now = dt.datetime.now()
    current_year = now.year
    name = "Amardeep Verma"

    return render_template('index.html', num=num, year=current_year, name=name)


@app.route('/guess/<fname>')
def predict(fname):
    gender_response = requests.get(
        "https://api.genderize.io", params={"name": fname})
    gender_data = gender_response.json()
    predicated_gender = gender_data['gender']

    age_response = requests.get("https://api.agify.io", params={"name": fname})
    age_data = age_response.json()
    predicated_age = age_data['age']

    return render_template('predict_age_gender.html', name=fname, predicated_gender=predicated_gender, predicated_age=predicated_age)


@app.route('/blog/<number>')
def get_blog(number):
    print(number)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    blog_posts = response.json()
    return render_template('blog.html', blog_posts=blog_posts)


if __name__ == '__main__':
    app.run(debug=True)
