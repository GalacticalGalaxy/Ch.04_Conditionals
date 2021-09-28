'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

Semgrade= int(input("What was your Semgrade? "))
Finalexam = int(input("What was your Final Exam grade? "))
Semgradeworth = int(input("What was your Exam Worth? "))
ga = (Semgrade*(100-Semgradeworth)+Finalexam*Semgradeworth)/100

if ga >= 90:
    print("You got an A")
elif ga >= 80:
    print("You got a B")
elif ga >= 70:
    print("You got a C")
elif ga >= 60:
    print("You got a D")
else:
    print("Transfer to Johnston!")