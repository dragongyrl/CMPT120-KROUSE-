#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/26/18

def main():
    answer = 'axolotl'
    boo = False
    while boo==False:
        print('I\'m thinking of an animal...')
        if input('Enter an animal:')==answer:
            print('That\'s the one!')
            boo=True
        else:
            print('That\'s not it! Try again!')

main()
    
