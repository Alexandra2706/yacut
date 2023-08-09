from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# подключаемые в самом конце модули опираются в своей работе на те экземпляры
# классов, которые созданы выше. Если подключить эти модули до создания
# экземпляров классов, то ничего работать не будет. 
from . import api_views, error_handlers, views
