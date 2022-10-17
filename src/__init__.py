import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

from src import routes, models

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.Config)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.Config.SQLALCHEMY_DATABASE_URI
app.debug = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# def create_app():
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_object(config.Config)
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.debug = True
#     db = SQLAlchemy(app)
#     db.init_app(app)
#     migrate = Migrate()
#     migrate.init_app(app, db)
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass
#
#     return app

# from src.routes import contacts

# export FLASK_APP=src / export FLASK_APP=routes.py
# export FLASK_DEBUG=true
# flask run
