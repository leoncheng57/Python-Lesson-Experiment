from flask import Flask, render_template, request

app = Flask(__name__)

# Index Page
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/savePythonContent', methods=['POST'])
def savePythonContent():
    if request.method == 'POST':
        print(request.data)
        text_file = open("executable.py", "w")
        text_file.write(request.data)
        text_file.close()
    return "(More stuff todo here)"

if __name__ == '__main__':
    app.run(debug=True)
