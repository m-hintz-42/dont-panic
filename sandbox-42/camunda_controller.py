from datetime import datetime
from flask import abort, request, jsonify, json
from api_data_app.REST_service.models import Data, Logs
from api_data_app import db, app

__author__ = 'mhintz'


@app.route('/api/data/<int:uuid>', methods=['POST'])
def data_inbound(uuid):
    if not request.json:
        abort(400)
    else:
        response = request.json
        response = json.dumps(response)
        data = Data(uuid=uuid, response=response, datetime=datetime.now())
        db.session.add(data)
        db.session.commit()
        return jsonify({'Success': 'uuid ' + str(uuid) + ' was successfully added to the database.'}), 201


@app.route('/api/camunda', methods=['POST'])
def camunda_request():
    if not request.json:
        abort(400)
    else:
        uuid = request.json['ServiceRequestID']['ID']
        payload = request.json
        payload = json.dumps(payload)
        record = Logs(uuid=uuid, payload=payload, datetime=datetime.now())
        response = Data.query.filter_by(uuid=uuid).first_or_404()
        db.session.add(record)
        db.session.delete(response)
        db.session.commit()
        return response.response, 200


@app.route('/api/payload/<int:uuid>', methods=['GET'])
def camunda_payload(uuid):
    payload = Logs.query.filter_by(uuid=uuid).first_or_404()
    db.session.delete(payload)
    db.session.commit()
    return payload.payload, 200

