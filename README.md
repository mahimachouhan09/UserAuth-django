# UserAuth-django
build a user authentication and authorization:

- User signup
- sign in
- logout
- forget password
- update password
- profile update

# Technology-Used
used python , django, database - mysql

# Project structure
UserAuth <br>
 |
 +-- templates <br>
 |  |
 |  +-- base.html
 |  +-- index.html
 |  +-- account
 | &nbsp;&nbsp;|
 | &nbsp;&nbsp;     +-- change_password.html <br>
 | &nbsp;&nbsp;     +-- login.html <br>
 | &nbsp;&nbsp;     +-- password_reset_complete.html <br>
 | &nbsp;&nbsp;     +-- password_reset_confirm.html <br>
 | &nbsp;&nbsp;     +-- password_reset_done.html <br>
 | &nbsp;&nbsp;     +-- password_reset_email.html <br>
 | &nbsp;&nbsp;     +-- password_reset.html <br>
 | &nbsp;&nbsp;     +-- profile_update.html <br>
 | &nbsp;&nbsp;     +-- signup.html <br>
 |    
 +-- UserAuth <br>
 |  |  
 | &nbsp;&nbsp; +-- __pycache__ <br>
 | &nbsp;&nbsp; +-- __init__.py <br>
 | &nbsp;&nbsp; +-- settings.py <br>
 | &nbsp;&nbsp; +-- urls.py <br>
 | &nbsp;&nbsp; +-- wsgi.py <br>
 |
 +-- UserLogin <br>
 |  |  
 |&nbsp;&nbsp;  +-- __pycache__ <br>
 |&nbsp;&nbsp;  +-- migrations <br>
 |&nbsp;&nbsp;  +-- __init__.py <br>
 |&nbsp;&nbsp;  +-- admin.py <br>
 |&nbsp;&nbsp;  +-- app.py <br>
 |&nbsp;&nbsp;  +-- forms.py <br>
 |&nbsp;&nbsp;  +-- models.py <br>
 |&nbsp;&nbsp;  +-- tests.py <br>
 |&nbsp;&nbsp;  +-- urls.py <br>
 |&nbsp;&nbsp;  +-- views.py <br>
 |
 +-- db.sqlite3
 |
 +-- manage.py
