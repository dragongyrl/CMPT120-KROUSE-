#Amelia Krouse
#4/16


class Product:

    def __init__(name,title, price, quantity):
        name.title=title
        name.price = price
        name.quantity = quantity

    def inventory(name, integer):
        if integer > name.quantity:
            return False
        else:
            return True

    def cost(name, integer):
        return integer*name.price

    def stock(name, integer):
        name.quantity = name.quantity-integer
            

def printStock(productNames):
     print()
     print("Available Products")
     print("------------------")
     for i in range(0,len(productNames)):
         if productNames[i].quantity>0:
             print(str(i)+")",productNames[i].title, "$", productNames[i].price)
     print()
     
def main():
    productNames = [ Product("Ultrasonic range finder",2.50,4)
                 , Product("Servo motor",14.99,10)
                 , Product("Servo controller",44.95, 5)
                 , Product("Microcontroller Board",34.95,7)
                 , Product("Laser range finder",149.99,2)
                 , Product("Lithium polymer battery",8.99,8)
                 ]
    cash = float(input("How much money do you have? $"))

    while cash > 0:
        printStock(productNames)
             
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit":
            break

        prodId = int(vals[0])
        count = int(vals[1])
             
        if productNames[prodId].quantity >= count:
            if cash >= Product.cost(productNames[prodId],count):
                Product.stock(productNames[prodId],count)
                cash -= Product.cost(productNames[prodId],count)
                print("You purchased", count, productNames[prodId].title +".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", productNames[prodId].title)
         
main()
