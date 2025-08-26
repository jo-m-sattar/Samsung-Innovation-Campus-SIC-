class SIC_clothes_store:
    def __init__(self, clothes_type, model_year, brand, price):
        self.clothes_type = clothes_type.lower()
        self.model_year = model_year
        self.brand = brand
        self.price = price
        
    def price_after_discount(self):
        global total_amount
        if self.clothes_type == 'shirts':
           return total_amount + 0.6 * self.price
        if self.clothes_type == 'pants':
           return total_amount + 0.7 * self.price
        if self.clothes_type == 'shoes':
           return total_amount + 0.5 * self.price

bought_items = []
total_amount = 0.0

no_of_items = int(input('enter the number of bought items: '))
for i in range(no_of_items):
    print('pls enter the item details')
    item_type = input('Item type (pants, shoes, shirts): ')
    item_model_year = input('Model Year: ')
    item_brand = input('Brand: ')
    item_price = float(input('Price: '))
    
    item = SIC_clothes_store(item_type, item_model_year , item_brand, item_price)
    bought_items.append(item)
print("---------------Bill details----------------")
for item in bought_items:
    price_after_disc = item.price_after_discount()
    print(f"Buyed item: {item.clothes_type}, Brand: {item.brand}, Model year: {item.model_year}, and Price after discount is {price_after_disc}")
    total_amount += price_after_disc
print(f"the total bill amount is {total_amount}")
