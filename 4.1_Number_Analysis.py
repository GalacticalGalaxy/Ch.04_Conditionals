'''
NUMBER ANALYSIS PROGRAM
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''

nu = float (input("What is the number?"))
oe = nu % 2

if oe == 1:
    print("Test one odd")
else:
    print("Test one even")
if nu > 0:
    print("Your # is positive")
elif nu < 0:
    print("Your # is negitive")
else:
    print("your # is 0")
if nu >= -100 and nu <=100:
    print("Your # is inclusive")
else:
    print("Your # is exclusive")
