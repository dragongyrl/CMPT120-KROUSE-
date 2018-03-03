#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/26/18

def main():
    answer = 'axolotl'
    boo = False
    while boo==False:
        print('I\'m thinking of an animal...')
        inny=input('Enter an animal:')
        inny=inny.lower()
        if inny==answer:
            print('That\'s the one!')
            boo=True
        elif inny == 'quit':
            exit()
        else:
            print('That\'s not it! Try again!')

main()
    
