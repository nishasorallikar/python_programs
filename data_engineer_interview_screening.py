"""
=====================================
 Question 10: Data Engineer Interview Screening
=====================================

Business Context:
A company shortlists candidates based on:
- Python Score
- SQL Score

Rules:

If:
Both scores >= 80
→ Selected

If:
One score >= 80
and the other >= 60
→ Waitlist

Otherwise:
Rejected
"""
p_score = int(input("Enter Python Score: "))
S_score = int(input("Enter SQL Score: "))
if p_score >= 80 and S_score >= 80:
    print("Selected!!")
elif (p_score >= 80 and S_score >= 60) or (p_score >=60 and S_score >= 80):
    print("Waitlist!!")
else:
    print("Rejected!!")