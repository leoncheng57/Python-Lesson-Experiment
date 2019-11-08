from flask import Flask, render_template

app = Flask(__name__)

# Index Page
@app.route('/')
def index():
    return "this is the index page"

if __name__ == '__main__':
    app.run(debug=True)
