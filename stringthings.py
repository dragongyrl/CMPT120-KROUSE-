#Author: Amelia Krouse
#Instructor: Juan Arias

def main():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    uname = first + '.' + last
    passwd = input("Create a new password: ")
    boo=False
    
    while boo == False:
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        else:
              boo=True
    print("The force is strong in this one…")
    print("Account configured. Your new email address is",
    uname + "@marist.edu")

main()
