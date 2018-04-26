# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename

from sim import solve
from tfidf import fenci, getFilelist, Tfidf
from sjet import get_rank

reload(sys)
sys.setdefaultencoding('utf8')

#仅支持上传txt格式的文档
UPLOAD_FOLDER = 'data/uploads'
ALLOWED_EXTENSIONS = set(['txt'])
app = Flask(__name__)

#设置初始登录界面的url，并使用init.html渲染
@app.route('/')
def hello_world():
    return render_template('init2.html')

#判断文件名是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#计算tfidf的初始登录界面
@app.route('/tfidf', methods=['GET', 'POST'])
def tfidfview():
    return render_template('tfidf2.html')

#上传文件的函数
@app.route('/tfidf/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        (allfiles,path) = getFilelist('data/uploads')
        #判断现有文件的数量，按文件号编号
        len = allfiles.__len__()
        upfile = request.files['myfile']
        #如果文件名合法，存储文件并重命名
        if upfile and allowed_file(upfile.filename):
            fname = str(len+1)+'.txt'
            upfile.save(os.path.join('data/uploads', fname))
            return upfile.filename
    return render_template('tfidf2.html')

#计算tfidf的函数
@app.route('/tfidf/caltfidf', methods=['GET', 'POST'])
def caltfidf():
    (allfile, path) = getFilelist('data/uploads/')
    #将文件中所有词语分词
    for ff in allfile:
        fenci(ff, path)

    Tfidf(allfile)
    return render_template('tfidf2.html')

#显示上传文档的tfidf值
@app.route('/tfidf/showtfidf', methods=['GET', 'POST'])
def show():
    files = os.listdir('data/tfidffile')
    len1 = len(files)

    file = str(len1) + '.html'
    return render_template(file)

#显示句子相似度的页面
@app.route('/sim', methods=['GET', 'POST'])
def simview():
    #
    if request.method == 'GET':
        return render_template('sim2.html')
    else:
        str1 = request.form.get('first')
        str2 = request.form.get('second')
        print str1
        print str2
        if str1 == '' or str2 == '':
            return '["?","?","?"]'
        ans1, ans2, ans3 = solve(str1, str2)
        return '[' + str(ans1) + ',' + str(ans2) + ',' + str(ans3) + ']'

#显示搜索引擎的页面
@app.route('/search', methods=['GET', 'POST'])
def searchview():
    if request.method == 'GET':
        return render_template('search2.html')
    else:
        str1 = request.form.get('input')
        print 12313
        print str1
        print 234324
        #读入输入的字符串，根据文档中词语和输入的相似性来确定排名
        get_rank(str1)
        return render_template("result.html")



if __name__ == '__main__':
    app.run()
