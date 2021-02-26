from os import read
from sqlalchemy.sql.expression import false, true
from app.models import db, LeaveRequest
from app.handlers.user_handler import UserHandler
from datetime import datetime
from sqlalchemy.sql import extract


class LeaveRequestHandler:
    """
    brief   :   Handler for handling CRUD operations in the LeaveRequest table table
    """

    def __init__(self):
        self.u_handler = UserHandler()

    def get_all(self):
        """
        brief        : gets all leave requests in the system 
        param        : none 
        constraint   : none
        throws       : none
        return       : List of all requests in the system
        """

        requests = db.session.query(LeaveRequest).all() or None
        return requests

    def get_requests_by_specific_employee(self, id):
        """
        brief        : gets all leave requests made by a specific employee 
        param        : id -- int -- unique employee id
        constraint   : none
        throws       : none
        return       : List of all requests made by a specific employee
        """

        requests = db.session.query(LeaveRequest).filter(LeaveRequest.employee_id == id).all() or None
        return requests

    def get_requests_to_specific_manager(self, id):
        """
        brief        : gets all leave requests directed to a specific manager
        param        : id -- int -- unique manager id
        constraint   : none
        throws       : none
        return       : List of all requests directed to a specific manager
        """

        now = datetime.now()
        res = db.session.query(LeaveRequest).filter(LeaveRequest.manager_id == id,\
                                                    LeaveRequest.status == 0,\
                                                    extract('year', LeaveRequest.request_date) == now.year,\
                                                    extract('month', LeaveRequest.request_date) == now.month,\
                                                    extract('day', LeaveRequest.request_date) == now.day)\
                                            .all() or None
        return res

    def take_action_on_request(self, id, action):
        """
        brief        : accepts/declines request
        param        : id -- int -- unique request id
                       action -- int -- 1 -> declined, 2 --> approved
        constraint   : action -- {0, 1, 2}
        throws       : none
        return       : True -- if action was successfull
                       False -- otherwise
        """
        
        if action not in [1, 2]:
            return False

        request = db.session.query(LeaveRequest).filter(LeaveRequest.id == id).first() or None
        if request is None:
            return False
        
        request.status = action
        db.session.commit()
        return True

    def add_request(self, employee_id, manager_id, leave_reason):
        """
        brief        : adds a leave request to the LeaveRequest table
        param        : employee_id -- int
                       manager_id -- int
                       reason -- string -- reason for leaving
        constraint   : none
        throws       : none
        return       : True -- if action was successfull
                       False -- otherwise
        """

        employee = self.u_handler.get_user_by_id(employee_id)
        manager = self.u_handler.get_user_by_id(manager_id)
        if employee is None or manager is None:
            return False
            
        now = datetime.now()
        new_request = LeaveRequest(employee_id=employee_id, manager_id=manager_id, reason=leave_reason, request_date=now, status=0)
        db.session.add(new_request)
        db.session.commit()
        return True

    




    
