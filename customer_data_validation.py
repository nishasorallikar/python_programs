"""
Question 12: Customer Data Load Approval

Inputs:
- customer_count
- error_count

Rules:
- customer_count >= 1000 and error_count == 0
  → Load Approved
- Otherwise
  → Load Rejected
"""
count = int(input("Enter Customer Count: "))
error = int(input("Enter Error Count: "))
if count >= 1000 and error == 0:
    print("Load Approved!!")
else:
    print("Load Rejected!!")