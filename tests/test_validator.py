import sys
sys.path.append("..")
from email_validator import validate_email, EmailNotValidError

def is_valid(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

print(is_valid("student@gmail.com"))
print(is_valid("student@gmail"))
print(is_valid("hello@yahoo.com"))
print(is_valid("@gmail.com"))