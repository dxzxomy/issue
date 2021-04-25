# coding:utf-8
from flask import Flask, render_template, request, send_from_directory, make_response, json, jsonify, Blueprint,send_file
from flask_restful import Resource
from ext import api
from libs.pymndb import MongoDBClient
from libs.switch_text import SwitchText
from config import settings
BASE_DIR = settings.Config().BASE_DIR

import os
import zipfile


switch_bp = Blueprint('switch', __name__, url_prefix='/switch')

@switch_bp.route('/check', methods=['POST'])
def check():
    import requests
    raw_data = request.get_json()
    if raw_data:
        node = raw_data.get("node")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "Content-Type": "application/json"
    }
    url = "http://10.64.18.34:6000/node"
    data = {"node": node}
    data = json.dumps(data)
    res = requests.post(url=url, headers=headers, data=data)
    text = res.text
    text = text.replace("null", "None")
    text = text.replace("true", "True")
    text = text.replace("false", "False")
    text = eval(text)


@switch_bp.route('/download_text', methods=['POST'])
def download1():
    node = request.form.get("name")
    print("---------------------------1",request.form)
    node = node.upper()
    print("0---------------", node)
    t = SwitchText()
    node = t.main(node)
    print("--------------0---------------0", node)
    ret = {}
    if node in [1]:

        ret["status"] = 400
        ret["msg"] = "输入有误，节点不存在或者流程已结束"
        return jsonify(ret)

    else:
        dirpath = os.path.join(BASE_DIR, "files")
        res = make_response(send_from_directory(dirpath, filename=node + ".zip", as_attachment=True))
        res.headers["Cache-Control"] = "no_cache"
        res.headers["max-age"] = 1
        filename = f'{node}'
        # print("--------------filename---------------", filename)
        # res.headers["Content-Type"] = "text/plain;charset=UTF-8"
        res.headers['Content-Type'] = 'text/plain;charset=UTF-8'
        res.headers["Access-Control-Expose-Headers"] = "Content-Disposition"
        res.headers["Content-Disposition"] = "attachment;filename=" + filename + '.zip'
        # res.headers.add_header("Content-Disposition", f"attachment;filename={filename}")
        # print(res.headers)

        return res


@switch_bp.route('/download', methods=['POST'])
def download():
    import os
    import zipfile
    import shutil

    mg = MongoDBClient()
    tree_data = mg.tree_data()


    acl = tree_data[19].get("children")
    rj_acl = acl[0].get("data")
    hw_acl = acl[1].get("data")
    h3c_acl = acl[2].get("data")
    rj_ipv6_acl = acl[3].get("data")
    hw_ipv6_acl = acl[4].get("data")
    h3c_ipv6_acl = acl[5].get("data")
    lunar = acl[6].get("data")
    h3c_margin_acl = acl[7].get("data")
    hw_margin_acl = acl[8].get("data")
    rj_margin_acl = acl[9].get("data")


    path = os.path.join(BASE_DIR, "files/交换机模板")
    if not os.path.exists(path):
        os.mkdir(path)
    zip_path = os.path.join(BASE_DIR, "files/交换机模板.zip")
    zipf = zipfile.ZipFile(zip_path, 'w')
    # print(tree_data[0].get("children")[0].get("data"))
    for i in tree_data:
        # new_dir = os.path.join(path, i.get("name"))
        # os.mkdir(new_dir)
        for j in i.get("children"):
            # new_txt = os.path.join(new_dir, j.get("name") + ".txt")
            # with open(new_txt, "w+", encoding="utf-8") as f:
            #     f.write(j.get("data"))
            data = j.get("data")
            label = j.get("label")
            if label == "rj_acl":
                data = data.replace("rj_acl", rj_acl)
            if label == "hw_acl":
                data = data.replace("hw_acl", hw_acl)
            if "h3c_acl" == "h3c_acl":
                data = data.replace("h3c_acl", h3c_acl)
            if label == "rj_ipv6_acl":
                data = data.replace("rj_ipv6_acl", rj_ipv6_acl)
            if label == "hw_ipv6_acl":
                data = data.replace("hw_ipv6_acl", hw_ipv6_acl)
            if label == "h3c_ipv6_acl":
                data = data.replace("h3c_ipv6_acl", h3c_ipv6_acl)
            if label == "lunar":
                data = data.replace("lunar", lunar)
            if label == "h3c_margin_acl":
                data = data.replace("h3c_margin_acl", h3c_margin_acl)
            if label == "hw_margin_acl":
                data = data.replace("hw_margin_acl", hw_margin_acl)
            if label == "rj_margin_acl":
                data = data.replace("rj_margin_acl", rj_margin_acl)

            zipf.writestr(f"{i.get('name')}/{j.get('name')}.txt", data=data)
    zipf.close()
    if os.path.exists(path):
        shutil.rmtree(path)
    ret = {}
    ret["status"] = 1
    ret["msg"] = "成功，请求下一步操作"

    dirpath = os.path.join(BASE_DIR, "files")
    res = make_response(send_from_directory(dirpath, filename="交换机模板.zip", as_attachment=True))
    res.headers["Cache-Control"] = "no_cache"
    res.headers["max-age"] = 1

    return res

class SwitchResource(Resource):

    def get(self):
        mg = MongoDBClient()
        switch_data = mg.tree_data()

        return jsonify(switch_data)


    def post(self):
        return "post"

    def put(self):

        return 'put'

    def delete(self):
        return 'delete'

    def patch(self):
        ret = {"status": "", "msg": ""}
        data = request.get_json()
        id = data["id"]
        text = data["text"]
        # print(text)
        mg = MongoDBClient()
        code = mg.patch_data(id, text)
        print(code)
        if code == 1:
            ret["status"] = 200
            ret["msg"] = "修改成功"
            ret["data"] = text
        else:
            ret["status"] = 401
            ret["msg"] = "修改失败"
        return ret

api.add_resource(SwitchResource, '/switch')