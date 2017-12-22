from flask import render_template , jsonify
from . import home
from ..model import Employee

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    employee = Employee.query.get(1)
    return jsonify(status="200", message=employee.email)