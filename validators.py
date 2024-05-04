from email_validator import validate_email, EmailNotValidError


def is_valid_email(email: str):
    """Verifies if email address is valid or not"""
    try:
        validate_email(email, check_deliverability=True)
        return True
    except EmailNotValidError:
        return False