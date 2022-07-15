from asyncio import exceptions
import json
from warnings import catch_warnings
from flask import Blueprint, current_app, request, jsonify
from .model import Client
from .schema import ClientSchema

bp_clients = Blueprint('client', __name__)

@bp_clients.route('/client', methods=['GET'])
def findAll():
    result = Client.query.all()
    return ClientSchema(many=True).jsonify(result), 200


@bp_clients.route('/client/<identificador>', methods=['GET'])
def findOne(identificador):
    
    client = Client.query.filter(Client.id == identificador).first()

    if(client == None):
        return jsonify ({
                    "status": 400,
                    "message": 'ID not found',
                    "error": 'ID INVALID'
        }) 
    else:
        return ClientSchema(many=False).jsonify(client)


@bp_clients.route('/client', methods=['POST'])
def create():
    cs = ClientSchema()

    client = cs.load(request.json)

    try:
        current_app.db.session.add(client)
        current_app.db.session.commit()
        return jsonify ({
                    "status": 200,
                    "message": 'registered successfully',
                    "error": 'null'
                })
    except Exception as e:
                return jsonify ({
                    "status": 400,
                    "message": 'error in registration',
                    "error": 'Error request'
                })
    return {}, 200

@bp_clients.route('/client/<identificador>', methods=['PUT'])
def upgrade(identificador):
    cs = ClientSchema()
    query = Client.query.filter(Client.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return cs.jsonify(query.first())


@bp_clients.route('/client/<identificador>', methods=['DELETE'])
def delete(identificador):
    client = Client.query.filter(Client.id == identificador).first()
    
    print(client)
    
    if(client == None):
        return jsonify ({
                    "status": 400,
                    "message": 'ID not found',
                    "error": 'ID INVALID'
        }) 
    else:
        client = Client.query.filter(Client.id == identificador).delete()
        current_app.db.session.commit()
        return jsonify({                 
                    "status": 200,
                    "message": 'successfully deleted',
                    "error": 'null'})