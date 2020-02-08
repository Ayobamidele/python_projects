print("How much did You pay:")
price = input()

price = int(price)
tax = 0 
print("where is your state in Nigeria :")
state = input()
state = str(state)
if price >= 100.00 and state.lower() in ("lagos","calabar", "kano", "ogun", "benin" ):
    tax = 01.50
elif state.lower() in ( "imo" , "kano", "calabar"):
    tax = 00.20
else:
    tax = 0.00    
total_price = tax + price
total_price = float(total_price)
print(f"You live in {state.capitalize()}.\nSo your tax is {tax}. \nThe total price is {total_price} ")