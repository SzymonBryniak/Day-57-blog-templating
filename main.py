from flask import Flask, render_template
import requests


app = Flask(__name__)


posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()


@app.route('/full_read/<idu>')
def full_read(idu):
    
    return render_template("post.html", id=int(idu), posts=posts)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)

