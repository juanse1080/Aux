def admin(user):
    """
        This method performs the verification of the user charge that initiates session, it is a function of denial of access
        Attributes:
            user {User}
                This attribute is the user to validation
        Returns:
            {boolean}
                This is the state of the operation
    """
    return True if user.role == 'A' else False # A is the character that identifies the administrator