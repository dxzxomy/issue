import pymongo
import configparser
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, "config/config.ini"))


# print(config.sections())

class MongoDBClient:

    def __init__(self):
        self.host = config.get('MongoDB', 'host')
        self.port = config.get('MongoDB', 'port')


    #连接mongo数据库
    def connect(self):
        conn = pymongo.MongoClient(f"mongodb://{self.host}:{self.port}/")
        # print("----------conn----", conn)
        return conn

    #增
    def add_data(self):
        conn = self.connect()

    #删
    def del_data(self):
        conn = self.connect()

    # 修改某一条数据
    def patch_data(self, id, text):
        import json
        code = ""
        conn = self.connect()
        db = conn.omy
        coll = db.omy
        try:
            if coll.update_one({"_id": id}, {"$set": {"data": text}}):
                code = 1
                conn.close()
                return code

        except:
            code = 2
            conn.close()
            return code

    #查
    def all_data(self):
        conn = self.connect()
        db = conn.omy
        col = db.omy
        all_data = col.find()

        return all_data

    #查询某一条数据
    def one_data(self):
        conn = self.connect()


    def data_init(self):
        print("---------------------------------------")
        all_data = self.all_data()
        tree_data = self.tree_data()

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

        for i in all_data:
            data = i.get("data")
            label = i.get("label")
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

        return all_data



    def tree_data(self):
        conn = self.connect()
        db = conn.omy
        coll = db.omy
        all_data = coll.find()
        data = []
        c_data = []
        for i in all_data:
            i["children"] = []
            if i["level"] == 1:
                data.append(i)
            else:
                c_data.append(i)


        for n in data:
            for m in c_data:
                if m["parent_id"] == n["_id"]:
                    n["children"].append(m)

        conn.close()
        return data

    def tree_init(self):
        conn = self.connect()
        tree_data = self.tree_data()

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
                    j["data"] = data.replace("rj_acl", rj_acl)

                elif label == "hw_acl":
                    j["data"] = data.replace("hw_acl", hw_acl)

                elif "h3c_acl" == "h3c_acl":
                    j["data"] = data.replace("h3c_acl", h3c_acl)

                elif label == "rj_ipv6_acl":
                    j["data"] = data.replace("rj_ipv6_acl", rj_ipv6_acl)

                elif label == "hw_ipv6_acl":
                    j["data"] = data.replace("hw_ipv6_acl", hw_ipv6_acl)

                elif label == "h3c_ipv6_acl":
                    j["data"] = data.replace("h3c_ipv6_acl", h3c_ipv6_acl)

                elif label == "lunar":
                    j["data"] = data.replace("lunar", lunar)

                elif label == "h3c_margin_acl":
                    j["data"] = data.replace("h3c_margin_acl", h3c_margin_acl)

                elif label == "hw_margin_acl":
                    j["data"] = data.replace("hw_margin_acl", hw_margin_acl)

                elif label == "rj_margin_acl":
                    j["data"] = data.replace("rj_margin_acl", rj_margin_acl)

                else:
                    continue

        conn.close()

        return tree_data

