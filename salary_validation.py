"""
=====================================
 Question 5: Salary Validation
=====================================

Business Context:
A Data Engineer job requires a minimum expected salary range.

Task:
Input expected salary.

If:
- Less than 300000 → "Too Low"
- Between 300000 and 800000 → "Acceptable"
- Greater than 800000 → "High Expectation"
"""
expected_salery = int(input("Enter your salery expectation:"))
if expected_salery < 300000:
    print("Too Low ")
elif expected_salery <= 800000:
    print("Acceptable")
else:
    print("High Expectation")