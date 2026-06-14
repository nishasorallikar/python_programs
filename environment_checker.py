"""
=====================================
 Question 4: Environment Checker
=====================================

Business Context:
Pipelines can run in development or production.

Task:
Input environment.

If:
dev
→ Development Environment

If:
prod
→ Production Environment

Otherwise:
Unknown Environment
"""
environment = input("Enter Environment:")
if environment == "dev":
    print("Development Environment")
elif environment == "prod":
    print("Production Environment")
else:
    print("Unknown Environment")
