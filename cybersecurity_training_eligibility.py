"""
=====================================
 Question 9: Cybersecurity Training Eligibility
=====================================

Business Context:
A fresher can join an advanced cybersecurity batch only if:
- Age >= 18
- Python score >= 70

Task:
Take age and Python score as input.

Print:
Eligible

or

Not Eligible
"""
age = int(input("Enter age: "))
score = int(input("Enter Python score: "))
if age >= 18 and score >= 70:
    print("Eligible")
else:
    print("Not Eligible")