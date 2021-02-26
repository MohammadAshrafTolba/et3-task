from app.models import db, Employee
from app.handlers.user_handler import UserHandler


class EmployeeHandler:
    """
    brief   :   Handler for handling CRUD operations in the Employee table
    """

    def get_all(self):
        """
        brief        : gets all employees in the system 
        param        : none 
        constraint   : none
        throws       : none
        return       : List of all employees in the system
        """

        users = db.session.query(Employee).all() or None
        return users

    def get_all_managers(self):
        """
        brief        : gets all managers in the system 
        param        : none 
        constraint   : none
        throws       : none
        return       : List of IDs all managers
        """

        res = db.session.query(Employee.manager_id).all() or None
        
        if res is None:
            return None
        
        managers_ids = []
        for res_tuple in res:
            managers_ids.append(res_tuple[0])
        
        return managers_ids

    def is_manager(self, id):
        """
        brief        : gets all managers in the system 
        param        : id -- int -- employee's unique id
        constraint   : none
        throws       : none
        return       : True -- if manager
                       False -- otherwise
        """

        return id in self.get_all_managers()

    def get_employee_manager(self, id):
        """
        brief        : gets specific employee's managers
        param        : id -- int -- employee's unique id
        constraint   : none
        throws       : none
        return       : list of IDs of managers of a specific employee
        """

        manager_id = db.session.query(Employee.manager_id).filter(Employee.id==id).first() or None

        if manager_id is None:
            return None
        
        return manager_id[0]

    def get_manager_employees(self, id):
        """
        brief        : gets specific manager's employees
        param        : id -- int -- employee's unique id
        constraint   : none
        throws       : none
        return       : list of IDs of employess of a specific manager
        """

        res = db.session.query(Employee.id).filter(Employee.manager_id==id).all() or None

        if res is None:
            return None
        
        managers_ids = []
        for res_tuple in res:
            managers_ids.append(res_tuple[0])
        
        return managers_ids

    def assign_manager_to_employee(self, id, manager_id):
        """
        brief        : adds a specific manager to a specific employee
        param        : id -- int -- employee's unique id
                       manager_id -- int -- manager's unique id
        constraint   : none
        throws       : none
        return       : True -- added successfully
                       False -- otherwise
        """

        u_handler = UserHandler()
        employee = u_handler.get_user_by_id(id)
        if not employee or not u_handler.user_exists(manager_id):
            return False

        employee = Employee(id=id, manager_id=manager_id, email=employee.email)
        db.session.add(employee)
        db.session.commit()
        return True
