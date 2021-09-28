'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with
two of your student colleagues before you run it by your instructor.
'''
S = int
S = 0
# Question 1------------------------------------------------
QA = int(input("Whats 9+10? "))
if QA == 21 or QA == 19:
    print("Your Right!")
    S += 1
else:
    print("Wrong (Faceplam)")
# Question 2------------------------------------------------
print("You have a D in CSP. Will you either,")
print("A. try to catch up and pass the class.")
print("B. Give up.")
print("C. Code.")

QB = str(input("Ans- "))
if QB == "A" or QA == "C" or QB == "a" or QB == "c":
    print("Your Right!")
    S += 1
else:
    print("Wrong, Bruh, the door is to the right.")
#Question 3------------------------------------------------
print("Which is better?")
print("A. Mac Computers.")
print("B. Windows Computers.")
print("C. Chromebooks.")
QC = str(input("Ans-"))
if QC == "A" or QC == "a" or QC == "B" or QC == "b":
    print("Good Job!")
    S += 1
else:
    print("NUU, WHy. Never.")
#Question 4------------------------------------------------
print("What is 2(3)*3")
print("A. 16")
print("B. something")
print("C. 18")
QD = str(input("Ans- "))
if QD == "C" or QD == "c":
    print("Your Right!")
    S += 1
else:
    print("Your Wrong")
#Question 5------------------------------------------------
print("What is an awesome class in school?")
QE = str(input("Ans- "))
if QE == "CSP" or QE == "csp":
    print("Awesome, Same!")
    S += 1
else:
    print("oh ok.")
    S += 0.5
#Question 6------------------------------------------------
print("If you roll two six sided dice,")
print("What is the chance of rolling a six on each dice.")
print("A. 1/6")
print("B. 1/36")
print("C. 1/12")
QH = str(input("Ans- "))
if QH == "B" or QH == "b":
    print("Your Right!")
    S += 1
else:
    print("Your Wrong!")

#Question 7------------------------------------------------
print("What is the most efficient method to code a")
print(" frequently used procedure in python?")
print("A. Function.")
print("B. Libraries.")
print("C. A and B.")
print("D. None of the above.")
QF = str(input("Ans- "))
if QF == "C" or QF == "c":
    print("Good Job, Your a great coder.")
    S += 1
else:
    print("Wrong!")
#Question 8------------------------------------------------
print("True or False.")
print("-4 squared equals 16.")
QG = bool(input("Ans- "))
if QG == True:
    print("Your Right!")
    S += 1
else:
    print("You need to take more math classes")
Total = (S/8)*100
print("Your Scored, an",Total ,"%")
if Total >= 90:
    print("You got an A, YOU WIINNNNN!")
elif Total >= 80:
    print("You got a B")
elif Total >= 70:
    print("You got a C")
elif Total >= 60:
    print("You got a D")
else:
    print("OOOOOFFF")