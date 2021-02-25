from app.models import Employee, db, User
from app.handlers.user_handler import UserHandler
from app.handlers.employee_handler import EmployeeHandler
from app.handlers.leave_request_handler import LeaveRequestHandler

db.drop_all()
db.create_all()

user = User(id=1, name="a", email='email1@domain.com')
user.set_password('112')
db.session.add(user)
db.session.commit()

user = User(id=2, name="b", email='email2@domain.com')
user.set_password('112')
db.session.add(user)
db.session.commit()

user = User(id=3, name="c", email='email3@domain.com')
user.set_password('112')
db.session.add(user)
db.session.commit()

user = User(id=4, name="d", email='email4@domain.com')
user.set_password('112')
db.session.add(user)
db.session.commit()

employee = Employee(id=2, manager_id=1, email='email2@domain.com')
db.session.add(employee)
db.session.add(employee)
db.session.commit()

u_handler = UserHandler()
u_handler.add_user('emaillll@domain.com', 'e', 'kbjkjb')
print(u_handler.get_all())
e_handler = EmployeeHandler()
print(e_handler.get_all_managers())
print(u_handler.get_user_by_id(4))
print(e_handler.get_manager_employees(1))
x, y = u_handler.delete_user(2)
print(x)
print(u_handler.get_all())
print(e_handler.assign_manager_to_employee(5, 3))
le_handler = LeaveRequestHandler()
print(le_handler.get_requests_by_specific_employee(1))