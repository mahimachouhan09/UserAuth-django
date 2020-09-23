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
__UserAuth__ <br>
 |<br>
 +-- templates <br>
 |  |<br>
 |  +-- base.html <br>
 |  +-- index.html <br>
 |  +-- account <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      | <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- change_password.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- login.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- password_reset_complete.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- password_reset_confirm.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- password_reset_done.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- password_reset_email.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- password_reset.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- profile_update.html <br>
 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      +-- signup.html <br>
 |    
 +-- UserAuth <br>
 | &nbsp;&nbsp;&nbsp; |  <br>
 | &nbsp;&nbsp;&nbsp; +-- __pycache__ <br>
 | &nbsp;&nbsp;&nbsp; +-- __init__.py <br>
 | &nbsp;&nbsp;&nbsp; +-- settings.py <br>
 | &nbsp;&nbsp;&nbsp; +-- urls.py <br>
 | &nbsp;&nbsp;&nbsp; +-- wsgi.py <br>
 |
 +-- UserLogin <br>
 |&nbsp;&nbsp;&nbsp;  |  <br>
 |&nbsp;&nbsp;&nbsp;  +-- __pycache__ <br>
 |&nbsp;&nbsp;&nbsp;  +-- migrations <br>
 |&nbsp;&nbsp;&nbsp;  +-- __init__.py <br>
 |&nbsp;&nbsp;&nbsp;  +-- admin.py <br>
 |&nbsp;&nbsp;&nbsp;  +-- app.py <br>
 |&nbsp;&nbsp;&nbsp;  +-- forms.py <br>
 |&nbsp;&nbsp;&nbsp;  +-- models.py <br>
 |&nbsp;&nbsp;&nbsp;  +-- tests.py <br>
 |&nbsp;&nbsp;&nbsp;  +-- urls.py <br>
 |&nbsp;&nbsp;&nbsp;  +-- views.py <br>
 |
 +-- db.sqlite3 <br>
 |
 +-- manage.py
