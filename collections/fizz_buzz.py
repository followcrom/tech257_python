"""Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'

Make a new 'fizzbuzz.py' file

For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz" instead of the number
For numbers which are multiples of both three and five print "FizzBuzz".

Acceptance Criteria
All core task are done
Core works with no error"""


print("\n-------------------------------------------")
# Write a program that prints the numbers from 1 to 100.
x = 1

while x <= 100:
    if (x % 3 == 0) and (x % 5 == 0):
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Buzz")
    elif x % 5 == 0:
        print("FizzBuzz")
    else:
        print(x)
    x += 1



print("\n-------------------------------------------")
# Improve the script so we can decide which numbers to substitute for "Fizz" and "Buzz"

x = 1
fizz_num = int(input("Fizz number: "))
buzz_num = int(input("Buzz number: "))

while x <= 100:
    if (x % fizz_num == 0) and (x % buzz_num == 0):
        print("FizzBuzz")
    elif x % fizz_num == 0:
        print("Buzz")
    elif x % buzz_num == 0:
        print("FizzBuzz")
    else:
        print(x)
    x += 1




print("\n-------------------------------------------")
x = 1
fizz_num = int(input("Fizz number 2: "))
buzz_num = int(input("Buzz number 2: "))

def check_fizzbuzz(num, fizz_num, buzz_num):
    if (x % fizz_num == 0) and (x % buzz_num == 0):
        print("FizzBuzz")
    elif x % fizz_num == 0:
        print("Buzz")
    elif x % buzz_num == 0:
        print("FizzBuzz")
    else:
        print(num)

while x <= 100:
    check_fizzbuzz(x, fizz_num, buzz_num)
    x += 1
