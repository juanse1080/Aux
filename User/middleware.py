def admin(user):
    return True if user.role == 'A' else False