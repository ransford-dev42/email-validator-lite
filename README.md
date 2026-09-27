# Email Validator Lite

Email Validator Lite is a simple Python library for checking whether an email address follows a valid basic format.

## Features

* Checks for a valid email username.
* Checks for the `@` symbol.
* Checks for a valid domain name.
* Checks for a domain extension such as `.com`, `.org`, or `.edu`.
* Returns `True` for valid email formats and `False` for invalid formats.

## Installation

Download or clone this repository from GitHub and place the `email_validator` folder in your Python project.

## Usage

Import the `is_valid_email` function from the library:

```python
from email_validator import is_valid_email

print(is_valid_email("student@gmail.com"))
```

Output:

```text
True
```

An invalid email:

```python
print(is_valid_email("student@gmail"))
```

Output:

```text
False
```

## Examples

| Email Address                                 | Result |
| --------------------------------------------- | ------ |
| [student@gmail.com](mailto:student@gmail.com) | True   |
| [hello@yahoo.com](mailto:hello@yahoo.com)     | True   |
| student@gmail                                 | False  |
| @gmail.com                                    | False  |

## Purpose

This library was developed as a simple reusable tool for validating the basic format of email addresses in Python applications.

## Author

[Boateng Ransford]

## License

This project is available for educational and personal use.
