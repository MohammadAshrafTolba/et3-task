from app.models import db
from app.handlers.user_handler import UserHandler
from app.handlers.employee_handler import EmployeeHandler
from app.handlers.leave_request_handler import LeaveRequestHandler

db.drop_all()
db.create_all()

u_handler = UserHandler()
e_handler = EmployeeHandler()
lr_handler = LeaveRequestHandler()

u_handler.add_user('employee1@example.com', 'Ahmed', 'pass123')
u_handler.add_user('employee2@example.com', 'Aly', '123pass')
u_handler.add_user('employee3@example.com', 'Mohammad', 'pass123')
u_handler.add_user('employee4@example.com', 'Ashraf', '123pass')
u_handler.add_user('employee5@example.com', 'Ibrahim', '123pass')

e_handler.assign_manager_to_employee(2, 1)
e_handler.assign_manager_to_employee(1, 3)
e_handler.assign_manager_to_employee(4, 1)
e_handler.assign_manager_to_employee(5, 3)

lr_handler.add_request(2, 1, 'Got Dr appointment')
lr_handler.add_request(2, 1, 'Family member in hospital')
lr_handler.add_request(1, 3, "Really sick")
lr_handler.add_request(5, 3, "Urgent stuff")