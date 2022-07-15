from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from pytz import timezone
from sqlalchemy import func

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db
    
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    corporate_name = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), default=func.now())