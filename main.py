from flask import Flask, render_template, Response,redirect,url_for,jsonify,request
import os
import cv2;
import Scanner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/image_gatway',methods=['POST'])
def image_gatway():
        f=request.files['file']
        UPLOAD_FOLDER = '.'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],"sample.jpg"))
        s=Scanner.AdharExtract()
        d=s.getData("sample.jpg")
        
        return jsonify(d)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)