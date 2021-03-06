from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .schema import configure as config_ma

def create_app():
    app = Flask(__name__);
   
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/smartnx';
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
    
    config_db(app);
    config_ma(app);
    
    Migrate(app, app.db);
    
    from .client import bp_clients
    app.register_blueprint(bp_clients)
    return app;
