"""
=====================================
 Question 7: Email Domain Validator
=====================================

Business Context:
Company employees must use company email.

Task:
Input email.

If email equals:
employee@company.com

Print:
Valid Employee

Otherwise:
Invalid Employee
"""
email = input("Enter your email: ")
if email == "employee@company.com":
    print ("Valid Employee")
else:
    print ("Invalid Employee")