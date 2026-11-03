name = input("what is your name?    ")

product = input("which product have you chosen to buy?:   ")
price = int(input("what is the price of your selected product?:  "))
quantity = int(input(f"what will be the quantity of your {product}?:  "))

bill_amount = price * quantity
discount = 1
if bill_amount < 1000:
    discount = 1
elif bill_amount > 1000 and bill_amount < 2000:
    discount = bill_amount * (5/100)
elif bill_amount > 2000 and bill_amount < 3001:
    discount = bill_amount * (10/100)
elif bill_amount > 3000:
    discount = bill_amount * (20/100)

final_bill = bill_amount - discount

print(f'''
================================
          SHOPPING BILL         
================================
                                
Customer Name: {name}          
product: {product}     
price = ${price}              
quantity = {quantity}          
--------------------------------
original amount = ${bill_amount}
discount = ${discount}            
Final bill = $ {final_bill}     
--------------------------------

Thank you for shopping!
================================''')
