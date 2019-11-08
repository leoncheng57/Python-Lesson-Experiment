from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Index Page
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/savePythonContent', methods=['POST'])
def savePythonContent():
    if request.method == 'POST':
        print(request.data)
        text_file = open("test.py", "w")
        text_file.write(request.data)
        text_file.close()
        # # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        # file = request.files['file']
        # # if user does not select file, browser also
        # # submit an empty part without filename
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return redirect(url_for('uploaded_file',
        #                             filename=filename))
    return "Done"

if __name__ == '__main__':
    app.run(debug=True)
