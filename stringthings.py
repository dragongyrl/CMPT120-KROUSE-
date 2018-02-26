#Author: Amelia Krouse
#Instructor: Juan Arias

def getName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first, last]

def getUser(first, last):
    uname = first + '.' + last
    uname = uname.lower()
    return uname

def getPassword():
    passwd = input("Create a new password: ")
    while passCheck(passwd)==True:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one…")    
    return passwd

def passCheck(passwd):
        valid = len(passwd)<8
        valid = valid or (passwd.lower()==passwd)
        valid = valid or (passwd.upper()==passwd)        
        return valid

def main():
    name = getName()
    uname = getUser(name[0],name[1])
    passwd = getPassword()
    print("Account configured. Your new email address is",
    uname + "@marist.edu")

main()
