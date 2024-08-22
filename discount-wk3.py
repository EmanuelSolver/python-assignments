def calculate_discount(price, discount_percent):
    price = int(input("Enter the price of the item: "))
    discount_percent = int(input("Enter the discount percentage: "))
    
    if discount_percent >= 20:
        price = price - (price * discount_percent / 100)
        
    print('The price of the item: ', price)
    return price

calculate_discount(0, 0)
    