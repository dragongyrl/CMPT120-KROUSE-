#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/5

def main():
    num = int(input("Please enter an integer."))
    x = 1
    prev = 0
    twoprev = 0
    for i in range(num -1):
        result = x + prev
        twoprev = prev
        prev = x
        x = result
    print(result)
    

main()
