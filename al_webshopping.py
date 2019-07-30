#Anna Lieb
#CSP 2018
#5/25/18
#al_webshopping.py

PRODUCT = ["Dark Chocolate Bar","Milk Chocolate Bar", "Caramel Chocolate Drops", "Chocolate Peanut Butter Bites","Chocolate Wafers"]

def welcomeMessage():
    print('''Welcome to the Princeton Chocolate Company!
Here is a list of our products:
Product #1 Dark Chocolate Bar: $2.50
Product #2 Milk Chocolate Bar: $1.75
Product #3 Caramel Chocolate Drops: $2.00
Product #4 Chocolate Peanut Butter Bites: $2.75
Product #5 Chocolate Wafers: $3.15''')

def getProductNo():
    productNo = int(input("Product number?: "))-1
    while productNo < 0 or productNo > 4:
        print("Invalid input, please try again. ")
        productNo = int(input("Product number?: "))-1
    return productNo

def getQuantity():
    quantity = int(input("Quantity?: "))
    return quantity

def getProductPrice(productNo):
    if productNo == 0:
        price = float(2.50)
    elif productNo == 1:
        price = float(1.75)
    elif productNo == 2:
        price = float(2.00)
    elif productNo == 3:
        price = float(2.75)
    elif productNo == 4:
        price = float(3.15)
    return price
    
def main():
    total = 0
    welcomeMessage()
    cont = True
    while cont == True:
        productNo = getProductNo()
        quantity = getQuantity()
        price = getProductPrice(productNo)
        print(quantity,"unit(s) of", PRODUCT[productNo], "have been added to your shopping cart. ")
        total += price*quantity
        repeat = input("Do you want to continue? (y/n): ")
        if repeat == 'n':
            cont = False
    print("Total: $"+str(total))

main()
    
