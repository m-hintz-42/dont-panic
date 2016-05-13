from datetime import datetime
from flask import abort, request, jsonify, json
from sandbox_42.module_1.models import Data, Logs
from sandbox_42 import db, app

__author__ = 'mhintz'


@app.route('/api/andy/<int:uuid>', methods=['POST'])
def andy_request(uuid):
    if not request.json:
        abort(400)
    else:
        response = request.json
        response = json.dumps(response)
        data = Data(uuid=uuid, response=response, datetime=datetime.now())
        db.session.add(data)
        db.session.commit()
        return jsonify({'Success': 'Yo ' + str(uuid) + ' worked!'}), 201


@app.route('/api/matt/<int:uuid>', methods=['POST'])
def matt_request(uuid):
    if not request.json:
        abort(400)
    else:
        payload = request.json
        payload = json.dumps(payload)
        record = Logs(uuid=uuid, payload=payload, datetime=datetime.now())
        response = Data.query.filter_by(uuid=uuid).first_or_404()
        db.session.add(record)
        db.session.delete(response)
        db.session.commit()
        return response.response, 200


@app.route('/api/michael/<int:uuid>', methods=['GET'])
def get_payload(uuid):
    payload = Logs.query.filter_by(uuid=uuid).first_or_404()
    db.session.delete(payload)
    db.session.commit()
    return payload.payload, 200

