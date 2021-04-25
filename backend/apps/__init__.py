from flask import Flask
from backend.config import settings
from backend.ext import db, api, cors


def create_app():

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)



    db.init_app(app)
    api.init_app(app)
    cors.init_app(app)

    # print(app.config)

    # app.register_blueprint(switch_bp)


    return app