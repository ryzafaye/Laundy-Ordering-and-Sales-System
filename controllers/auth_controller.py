from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.db import connect_db

auth_controller = Blueprint('auth', __name__)

@auth_controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emp_id = request.form.get('emp_id') 
        password = request.form.get('password') 

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM "EMPLOYEES" WHERE "EmpID" = ? AND "Password" = ?', (emp_id, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['emp_id'] = user['EmpID']
            session['full_name'] = f"{user['FirstName']} {user['LastName']}"
            session['position'] = user['Position']
            
            return redirect(url_for('dashboard')) 
        else:
            flash('Invalid Employee ID or Password!', 'error')
            
    return render_template('login.html')

@auth_controller.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('auth.login'))