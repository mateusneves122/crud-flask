import imp
from flask import Blueprint, current_app, request, jsonify
from .model import Client
from .schema import ClientSchema

bp_clients = Blueprint('client', __name__)


@bp_clients.route('/findAll', methods=['GET'])
def findAll():
    ...


@bp_clients.route('/findOne', methods=['GET'])
def findOne():
    ...

@bp_clients.route('/create', methods=['POST'])
def create():
    cs = ClientSchema()
    client, error = cs.load(request.json)
    current_app.db.session.add(client)
    current_app.db.session.commit()
    

@bp_clients.route('/upgrade/<identificador>', methods=['PUT'])
def upgrade(identificador):
    cs = ClientSchema()
    query = Client.query.filter(Client.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return cs.jsonify(query.first())


@bp_clients.route('/delete/<identificador>', methods=['DELETE'])
def delete(identificador):
    Client.query.filter(Client.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('deletado')