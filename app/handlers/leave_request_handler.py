from sqlalchemy.sql.expression import false
from app.models import db, LeaveRequest
from app.handlers.user_handler import UserHandler
from datetime import datetime
from sqlalchemy.sql import extract


class LeaveRequestHandler:
    """
    brief   :   Handler for handling CRUD operations in the LeaveRequest table table
    """

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
                       action -- int -- 0 -> decline, 1 --> accepts
        constraint   : action -- {0, 1}
        throws       : none
        return       : True -- if action was successfull
                       False -- otherwise
        """
        
        if action not in [0, 1]:
            return False

        request = db.session.query(LeaveRequest).filter(LeaveRequest.id == id).first() or None
        if request is None:
            return False
        
        request.status = action
        db.session.commit()
        return True




    
