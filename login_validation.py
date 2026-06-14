"""
=====================================
 Question 3: Login Validation
=====================================

Business Context:
A data engineer can access the pipeline dashboard only with the correct username.

Task:
Input username.

If username is:
admin

Print:
Access Granted

Otherwise:
Access Denied
"""
username = input("Enter Username: ")

if username == "admin":
    print("Access Granted")
else:
    print("Access Denied")