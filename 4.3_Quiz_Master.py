'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with
two of your student colleagues before you run it by your instructor.
'''
# Question 1
QA = int(input("Whats 9+10? "))
if QA == 21 or QA == 19:
    print("Your Right!")
else:
    print("Wrong (Faceplam)")
# Question 2
print("You have a D in CSP. Will you either,")
print("A. try to catch up and pass the class.")
print("B. Give up.")
print("C. Code.")

QB = str(input("Ans- "))
if QB == "A" or QA == "C" or QB == "a" or QB == "c":
    print("Your Right!")
else:
    print("Wrong, Bruh, the door is to the right.")
#Question 3
print("Which is better?")
print("A. Mac Computers.")
print("B. Windows Computers.")
print("C. Chromebooks.")
QC = str(input("Ans-"))
if QC == "A" or QC == "a" or QC == "B" or QC == "b":
    print("Good Job!")
else:
    print("NUU, WHy. Never.")
#Question 4
print("What is 2(3)*3")
print("A. 16")
print("B. something")
print("C. 18")
QD = str(input("Ans- "))
if QD == "C" or QD == "c":
    print("Your Right!")
else:
    print("Your Wrong")
#Question 5
print("What is an awesome subject in school?")
QE = str(input("Ans- "))
if QE == "Science" or QE == "science":
    print("Awesome, Same!")
else:
    print("oh ok.")
#Question 6
print("If you roll two six sided dice,")
print("What is the chance of rolling a six on each dice.")
QH = int(input("Ans- "))
if QH == 36 or QH == 0.36:
    print("Your Right!")
else:
    print("Your Wrong!")

#Question 7
print("What is the most efficient method to code a")
print("A. frequently used procedure in python?")
print("A. Function.")
print("B. Libraries.")
print("C. A and B.")
print("D. None of the above.")
QF = int(input("Ans- "))
if QF == "C" or QF == "c":
    print("Good Job, Your a great coder.")
else:
    print("Wrong!")
#Question 8
print("True or False.")
print("-4 squared equals 16.")
QG = bool(input("Ans- "))
if QG == True:
    print("Your Right!")
else:
    print("You need to take more math classes")