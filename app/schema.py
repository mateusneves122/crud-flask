from flask_marshmallow import Marshmallow
from .model import Client


ma = Marshmallow()

def configure(app):
    ma.init_app(app)
    
class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client