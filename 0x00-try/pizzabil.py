size_pizza = input("what size of pizza do want(S for Small/M for Medium/L for Large)?: ")
price = 0
if( size_pizza == 's' or size_pizza == 'S'):
    price += 100
    print(f"price for small size pizza is {price} Rs")
    pepper = input("Do you want pepperoni for small Pizza(y/n)?: ")
    if(pepper == 'y' or pepper == 'Y'):
        price += 30
    elif(pepper == 'n' or pepper == 'N'):
        price = price
    else:
        print("wrong input")
        exit()
elif ( size_pizza == 'm' or size_pizza == 'M'):
    price += 200
    print(f"price for medium size pizza is {price} Rs")
    pepper = input("Do you want pepperoni for medium Pizza(y/n)?: ")
    if(pepper == 'y' or pepper == 'Y'):
        price += 50
    elif(pepper == 'n' or pepper == 'N'):
        price = price
    else:
        print("wrong input")
        exit()
elif( size_pizza == 'l' or size_pizza == 'L'):
    price += 300
    print(f"price for large size pizza is {price} Rs")
    pepper = input("Do you want pepperoni for large Pizza(y/n)?: ")
    if(pepper == 'y' or pepper == 'Y'):
        price += 50
    elif(pepper == 'n' or pepper == 'N'):
        price = price
    else:
        print("wrong input")
        exit()
else:
    print("wrong input")
    exit()
cheese = input("Do want extra cheese(y/n)?: ")
if(cheese == 'y' or cheese == 'Y'):
    price += 20
    print(f"Total order amount for pizza is {price} Rs")
elif(cheese == 'n' or cheese == 'N'):
    price = price
    print(f"Total order amount for pizza is {price} Rs")
else:
    print("wrong input")
    exit()

