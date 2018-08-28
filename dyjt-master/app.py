import os
import time

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app,db')
db = SQLAlchemy(app)

UPLOAD_FOLDER = '/static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from PicModel import Picture


@app.route('/')
def hello_world():
    return 'Hello orld!'


@app.route('/dyjtpic/api/v1.0/pic', methods=['get'])
def get_picture():
    pic = [i.serialize for i in Picture.query.order_by(Picture.id)]
    return jsonify(pic)


@app.route('/dyjtpic/api/v1.0/pic_upload', methods=['post'])
def pic_upload():
    if request.method == 'POST':
        f = request.files['picfile']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static\\uploads',
                                   str(round(time.time())) + secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return 'saved'


@app.route('/dyjtpic/api/v1.0/PicUpload')
def upload_page():
    return render_template('PicUpload.html')


if __name__ == '__main__':
    app.run(debug=True)
