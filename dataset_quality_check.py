"""
Question 14: Dataset Quality Check

Inputs:
- record_count
- null_percentage

Rules:
- record_count > 1000 and null_percentage < 5
  → Quality Passed
- Otherwise
  → Quality Failed
"""
record_count = int(input("Enter record count: "))
null_percentage = int (input("Enter null percentage: "))
if record_count > 1000 and null_percentage < 5:
    print("Quality Passed!!")
else:
    print("Quality Failed!!")