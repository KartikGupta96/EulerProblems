#Prints numbers from 1 to 100. For numbers that are multiples of 3 print Fizz
#For numbers that are multiples of 5 print Bizz
#For numebers that are multiples of both 3 and 5 prints FizzBizz
import sys

def main():
    fizzBizz()

def fizzBizz():
    for x in range(1,101):
        isTrue = False
        if (x % 3 == 0 and x % 5 == 0):
            print "FizzBizz"
            isTrue = True
        elif (x % 3 == 0):
            print "Fizz"
            isTrue = True
        elif (x % 5 == 0):
            print "Bizz"
            isTrue = True

        if (isTrue is False):
            print x

if __name__ == "__main__":
    main()