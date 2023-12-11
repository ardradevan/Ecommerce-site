def validate_name(name):
    """
    Simple validation for a name:
    - Should not be empty
    - Should contain only letters
    """
    if not name:
        return 'Name is required.'
    
    if not name.isalpha():
        return 'Invalid name. Use only letters.'

    return None