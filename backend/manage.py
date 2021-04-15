from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from apps import create_app
from ext import db
from apps.user.models import User


#创建app核心对象

app = create_app()
manager = Manager(app)


#创建db管理工具
migrate = Migrate(app,db)
# 添加db迁移命令到manage中
manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()