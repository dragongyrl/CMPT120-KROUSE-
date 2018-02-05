#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/5

import math

def main():
    num = int(input("Please enter an integer."))
    sign = 0
    result = 0
    for i in range(1, num, +2):
        if(sign == 0):
            result = result + 4/i
            sign = 1
        elif(sign == 1):
            result = result - 4/i
            sign = 0
    print(result)
    print(result - math.pi)


main()
