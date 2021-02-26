from flask.globals import request
from app.models import LeaveRequestSchema as lr_schema
from app.handlers.user_handler import UserHandler
from datetime import datetime
from flask import jsonify
from sqlalchemy import extract
import json


def leave_requests_jsonify(leave_requests):
    if leave_requests is None or not leave_requests:
        return jsonify({'data': 'None'})

    leave_requests_schema = lr_schema(many=True)
    json_response = leave_requests_schema.dump(leave_requests)
    u_handler = UserHandler()
    user = None
    for (lr_json, lr_query) in zip(json_response, leave_requests):
        lr_json['employeed_id'] = lr_query.employee_id
        user = u_handler.get_user_by_id(lr_query.employee_id)
        lr_json['employee_name'] = user.name
        lr_json['employee_email'] = user.email

    return {'data': json_response}

def past_leave_requests_jsonify(leave_requests):
    if leave_requests is None or not leave_requests:
        return jsonify({'data': 'None'})

    leave_requests_schema = lr_schema(many=True)
    json_response = leave_requests_schema.dump(leave_requests)
    
    request_date = None
    status = None
    
    for lr_json in json_response:
        status = int(lr_json['status'])
        if status == 0:
            lr_json['status'] = 'unanswered'
        elif status == 1:
            lr_json['status'] = 'request declined'
        elif status == 2:
            lr_json['status'] = 'request approved'

    return {'data': json_response}