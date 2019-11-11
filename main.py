from flask import Flask, render_template, request
import python_runner
import json, platform

app = Flask(__name__)
EXECUTABLE = '_executeme.py'

# Index Page
@app.route('/')
def index():
    version = platform.python_version()
    return render_template("index.html", version = version)


# Handle receiving python from frontend
# running the python code, and returning the error messages
@app.route('/savePythonContent', methods=['POST'])
def savePythonContent():

    # Take in python text (written by user on frontend)
    # Take that data and write it to a python file called EXECUTABLE
    text_file = open(EXECUTABLE, "w")
    # print(request.data)
    text_file.write(request.data)
    text_file.close()
    
    # Call python_runner to execute file and handle error messages
    output = python_runner.run(EXECUTABLE)
    return json.dumps(output)

if __name__ == '__main__':
    app.run(debug=True)
