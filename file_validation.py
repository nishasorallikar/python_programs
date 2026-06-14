"""
=====================================
 Question 1: ETL File Validation
=====================================

Business Context:
A data pipeline should not process an empty file.

Task:
Ask the user for the number of records.

If records are:
- 0 → Print "File is empty"
- Greater than 0 → Print "File is valid"
"""
record = int(input("Enter record count:"))
if record == 0:
    print("File is empty")
else:
    print("file is Valid")