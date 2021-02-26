"""
This file is responsible for routing requests to the appropriate handlers
"""

from app.init_app import app
from app.handlers.user_handler import UserHandler
from app.handlers.leave_request_handler import LeaveRequestHandler
from app.handlers.employee_handler import EmployeeHandler
from app.jsonify_response import leave_requests_jsonify, past_leave_requests_jsonify

from flask import render_template, request, jsonify, session, redirect
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session['logged_in']:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def route_placeholder():
    if 'logged_in' in session and session['logged_in'] == True:
        return redirect('/home')
    session['logged_in'] = False
    return redirect('/login')

@app.route('/login')
def login():
    if 'logged_in' in session and session['logged_in'] == True:
        return redirect('/home')
    session['logged_in'] = False
    return render_template('login.html')

@app.route('/check_credentials', methods=['POST'])
def check_credentials():
    if 'logged_in' in session and session['logged_in'] == True:
        return redirect('/home')

    email = request.form.get('email')
    password = request.form.get('password')
    u_handler = UserHandler()
    valid, user = u_handler.check_credentials(email, password)
    if not valid:
        return jsonify({'status': 'false'})
    else:
        session['logged_in'] = True
        session['user_id'] = user.id
        session['user_email'] = user.email
        return jsonify({'status': 'true'})

@app.route('/home')
@login_required
def display_home():
    return render_template('home.html')

@app.route('/requests')
@login_required
def see_requests():
    return render_template('requests.html')

@app.route('/get_requests')
@login_required
def get_manager_requests():
    manager_id = session['user_id']
    lr_handler = LeaveRequestHandler()
    leave_requests = lr_handler.get_requests_to_specific_manager(manager_id)
    return leave_requests_jsonify(leave_requests)

@app.route('/request_action', methods=['POST'])
@login_required
def take_action_on_request():
    request_id = request.form.get('request_id')
    action = int(request.form.get('action'))
    lr_handler = LeaveRequestHandler()
    status = lr_handler.take_action_on_request(request_id, action)
    return jsonify({'status': status})

@app.route('/view_past_requests', methods=['GET'])
@login_required
def view_past_requests():
    employee_id = session['user_id']
    lr_handler = LeaveRequestHandler()
    leave_requests = lr_handler.get_requests_by_specific_employee(employee_id)
    return past_leave_requests_jsonify(leave_requests)

@app.route('/leave_requests')
@login_required
def past_leave_requsts_page():
    return render_template('past_requests.html')

@app.route('/send_request', methods=['POST'])
@login_required
def send_request():
    print('here2')
    leave_reason = request.form.get('leave_reason')
    employee_id = session['user_id']
    print(employee_id)
    e_handler = EmployeeHandler()
    manager_id = e_handler.get_employee_manager(employee_id)
    print(manager_id)
    if manager_id is None:
        return jsonify({'status': False})
    lr_handler = LeaveRequestHandler()
    status = lr_handler.add_request(employee_id, manager_id, leave_reason)
    print('here4')
    return jsonify({'status': status})

@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect('/login')