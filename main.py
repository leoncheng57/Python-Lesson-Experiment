from flask import Flask, render_template, request
import python_runner
import json, platform, random

app = Flask(__name__)
EXECUTABLE = '_executeme.py'
version = platform.python_version()

# Index Page
@app.route('/')
def index():
    links = [
        {
            'url': "./un_a.html",
            'display': 'Click here to Continue (A)'
        },
        {
            'url': "./an_a.html",
            'display': 'Click here to Continue (B)'
        }
    ]
    return render_template("index.html", version = version, links=links)

@app.route('/un_a.html')
def un_a():
    return render_template("un_a.html", version = version, 
    is_anthro = False, 
    basepage = "regular_instructions.html", 
    buttonsData = [{'url': './un_b.html', 'display': 'Next Lesson'}])

@app.route('/un_b.html')
def un_b():
    return render_template("un_b.html", version = version, 
    is_anthro = False, 
    basepage = "regular_instrutions.html",
    buttonsData = [{'url': './un_a.html', 'display': 'Previous Lesson'}, {'url': '#', 'display': "Take Survey!"}])


@app.route('/an_a.html')
def an_a():
    return render_template("an_a.html", version = version, 
    is_anthro = True, 
    basepage = "anthro_instrutions.html",
    buttonsData = [{'url': './an_b.html', 'display': 'Next Lesson'}])

@app.route('/an_b.html')
def an_b():
    return render_template("an_b.html", version = version, 
    is_anthro = True, 
    basepage = "anthro_instrutions.html",
    buttonsData = [{'url': './an_a.html', 'display': 'Previous Lesson'}, {'url': '#', 'display': "Take Survey!"}])

    


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
