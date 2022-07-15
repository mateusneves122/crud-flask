from http import client
from flask import Blueprint, current_app, request, jsonify, Response
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
    
    print(client)
    
    return ClientSchema(many=False).jsonify(client), 200


@bp_clients.route('/client', methods=['POST'])
def create():
    cs = ClientSchema()

    client = cs.load(request.json)

    current_app.db.session.add(client)
    current_app.db.session.commit()


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
    Client.query.filter(Client.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('deletado')