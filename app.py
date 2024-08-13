#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
from module import check
#from module import imageQuality
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
file_arr = []
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file1' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file1 = request.files['file1']
    file2 = request.files['file2']
    if file1.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file1 and allowed_file(file1.filename):
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

        # print('upload_image filename: ' + filename)
        flash('Images successfully uploaded and displayed below')
        # flash('\n FileName = '+filename)
        f1 = UPLOAD_FOLDER+filename1
        f2 = UPLOAD_FOLDER+filename2
        '''bscore = imageQuality(f1)
        if(bscore>30):
            flash(filename1+' Quality is low please reupload it')
        bscore = imageQuality(f2)
        if (bscore > 30):
            flash(filename2 + ' Quality is low please reupload it')'''

        print('FileName1 = '+filename1)
        #Processing the images
        a, b = check((f1), (f2))
        #check((f1),(f2))
        if(b=='photos'):
            flash('Upload only one Photograph')
        elif(b=='signatures'):
            flash('Upload only one Signature')
        else:
            s = 'static/uploads/'
            if s in a:
                a = a.replace(s,'')
                print('a = '+a)
            if s in b:
                b = b.replace(s,'')
            #file_arr.clear()
            file_arr.append(a)
            file_arr.append(b)

        print(file1, file2)
        #print(file_arr)
        #print(a, b)
        return render_template('index.html', filename1=filename1, filename2 = filename2)

    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)
@app.route('/first')
def first():
    print('array = '+file_arr[0]+' '+file_arr[1])
    flash("Final Photo and Signature")
    return render_template("first.html",filename1=file_arr[0], filename2 = file_arr[1])
@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)




if __name__ == "__main__":
    app.debug = True
    app.run()