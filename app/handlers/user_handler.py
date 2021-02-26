from app.models import db, User

class UserHandler:
    """
    brief   :   Handler for handling CRUD operations in the User table
    """

    def get_all(self):
        """
        brief        : gets all users in the system 
        param        : none 
        constraint   : none
        throws       : none
        return       : List of all users in the system
        """

        users = db.session.query(User).all() or None
        return users

    def get_user_id_by_email(self, email):
        """
        brief        : gets specific user id by email 
        param        : email -- string -- unique user email
        constraint   : none
        throws       : none
        return       : user_id -- int
                       None -- if no user found
        """

        user_id = db.session.query(User).filter(User.email==email).first() or None
        return user_id

    def check_credentials(self, email, password):
        """
        brief        : checks user's credentials to log in 
        param        : email -- string -- unique user email
                       password -- string -- user's password
        constraint   : none
        throws       : none
        return       : True, user -- if credentials are correct
                       False, None -- otherwise
        """

        user = db.session.query(User).filter(User.email==email).first() or None
        if user is not None and user.check_password(password):
            return True, user
        return False, None

    def get_user_by_id(self, id):
        """
        brief        : gets specific user by id
        param        : id -- int -- unique user id
        constraint   : none
        throws       : none
        return       : List of all users in the system
        """

        user = db.session.query(User).filter(User.id==id).first() or None
        return user

    def user_exists(self, id):
        """
        brief        : checks if a user is in the system
        param        : id -- int -- unique user id
        constraint   : none
        throws       : none
        return       : True -- if user exists
                       False -- otherwise
        """

        return self.get_user_by_id(id) is not None

    def email_exists(self, email):
        """
        brief        : checks if the email is associated with a user in the system
        param        : id -- email -- string
        constraint   : none
        throws       : none
        return       : True -- if email exists
                       False -- otherwise
        """

        res = db.session.query(User).filter(User.email==email).all() or None
        return res is not None

    def add_user(self, email, name, password):
        """
        brief        : checks if the email is associated with a user in the system
        param        : id -- int
                       email, name -- string
        constraint   : id, email -- unique
        throws       : none
        return       : True -- if user was added successfully
                       False -- otherwise
        """
        """
        if self.user_exists(id):
            return False, 'user with this id exists'
        """
        if self.email_exists(email):
            return False, 'user with this email exists'

        user = User(email=email, name=name, type=0)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return True, 'user was added successfully'

    def delete_user(self, id):
        """
        brief        : checks if the email is associated with a user in the system
        param        : id -- int
        constraint   : none
        throws       : none
        return       : True -- if user was deleted successfully
                       False -- otherwise
        """
        
        user = self.get_user_by_id(id)
        if user is None:
            return False, "user doesn't exist"
        db.session.delete(user)
        db.session.commit()
        return True, 'user was deleted successfully'