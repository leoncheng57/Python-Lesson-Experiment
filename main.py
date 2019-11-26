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
            'url': "./std_a.html",
            'display': 'Click here to Continue (A)'
        },
        {
            'url': "./un_a.html",
            'display': 'Click here to Continue (B)'
        },
        {
            'url': "./an_a.html",
            'display': 'Click here to Continue (C)'
        }
    ]
    return render_template("index.html", version = version, links=links)

@app.route('/std_a.html')
def std_a():
    return render_template("un_a.html", version = version, 
    errorType = 'standard', 
    basepage = "regular_instructions.html", 
    buttonsData = [{'url': './std_b.html', 'display': 'Next Lesson'}],
    customerrorTitle = "")

@app.route('/std_b.html')
def std_b():
    return render_template("un_b.html", version = version, 
    errorType = 'standard', 
    basepage = "regular_instructions.html",
    buttonsData = [{'url': './std_a.html', 'display': 'Previous Lesson'}, {'url': 'https://forms.gle/SEfEYWP7eYtZhYNBA', 'display': "Take Survey!"}],
    customerrorTitle = "")


@app.route('/un_a.html')
def un_a():
    return render_template("un_a.html", version = version, 
    errorType = 'helpful', 
    basepage = "regular_instructions.html", 
    buttonsData = [{'url': './un_b.html', 'display': 'Next Lesson'}],
    customerrorTitle = "Advice")

@app.route('/un_b.html')
def un_b():
    return render_template("un_b.html", version = version, 
    errorType = 'helpful', 
    basepage = "regular_instructions.html",
    buttonsData = [{'url': './un_a.html', 'display': 'Previous Lesson'}, {'url': 'https://forms.gle/SEfEYWP7eYtZhYNBA', 'display': "Take Survey!"}],
    customerrorTitle = 'Advice')


@app.route('/an_a.html')
def an_a():
    return render_template("an_a.html", version = version, 
    errorType = 'anthro', 
    basepage = "anthro_instructions.html",
    buttonsData = [{'url': './an_b.html', 'display': 'Next Lesson'}],
    customerrorTitle = "Rachel's Advice")

@app.route('/an_b.html')
def an_b():
    return render_template("an_b.html", version = version, 
    errorType = 'anthro', 
    basepage = "anthro_instructions.html",
    buttonsData = [{'url': './an_a.html', 'display': 'Previous Lesson'}, {'url': 'https://forms.gle/SEfEYWP7eYtZhYNBA', 'display': "Take Survey!"}],
    customerrorTitle = "Rachel's Advice")

    


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
