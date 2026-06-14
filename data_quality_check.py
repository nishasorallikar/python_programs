"""
=====================================
 Question 2: Data Quality Check
=====================================

Business Context:
A customer dataset must have at least 100 records before loading.

Task:
Take customer count as input.

If:
- Less than 100 → "Insufficient data"
- 100 or more → "Ready for loading"
"""
Data = int(input("Enter customer count:"))
if Data < 100:
    print("Insufficient data")
else:
    print("Ready for loading")
