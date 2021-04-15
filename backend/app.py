from flask import Flask, render_template, request, send_from_directory, make_response, json, jsonify
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from libs.pymndb import MongoDBClient
from datetime import datetime,timedelta
from flask_cors import CORS
import zipfile


app = Flask(__name__)

bootstrap = Bootstrap(app)
ckeditor = CKEditor(app)
cors = CORS(app)
# csrf = CSRFProtect(app)

@app.route('/')
def index():

    mg = MongoDBClient()
    all_data = mg.all_data()
    print(all_data[0])

    return render_template("index.html",all_data=all_data)

import os
@app.route('/download1', methods=['GET'])
def download1():
    dirpath = os.path.join(app.root_path, 'files')
    print(dirpath)
    file_path = os.path.join(dirpath, "华为万兆堆叠.txt")
    print(file_path)
    mg = MongoDBClient()
    all_data = mg.all_data()
    mydata = all_data[0]["pile"]
    # print(mydata)
    # with open(file_path,"w+",encoding="gbk") as f:
    #     f.write(mydata)
    # for i in all_data:
    #     with open("")
    res = make_response(send_from_directory(dirpath, filename="华为万兆堆叠.txt", as_attachment=True))
    res.headers["Cache-Control"] = "no_cache"
    res.headers["max-age"] = 1
    return res

@app.route("/download", methods=["GET"])
def download():
    dirpath = os.path.join(app.root_path, 'files')


@app.route("/modify", methods=['POST'])
def modify_data():
    if request.method == 'POST':
        mg = MongoDBClient()
        tree_data = mg.tree_data()

        return jsonify(tree_data)





if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    #缓存问题
    # app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    # 解决前端传给后端的中文出现乱码

    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
