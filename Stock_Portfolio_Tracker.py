Dict = {
    "tsla": 210, "aapl": 180, "msft": 320, "googl": 140, 
    "amzn": 155, "meta": 350, "nflx": 480, "nvda": 620, 
    "intc": 45, "ibm": 165
}

Stock_name=str(input("Enter stock name:")).strip().lower()
Stock_quantity=int(input("Enter stock quantity:"))

while Stock_name not in Dict :
  print("Please enter right stock")
  Stock_name=str(input("Enter stock name:")).strip().lower()
while Stock_quantity<=0:
  print("please give valid value")
  Stock_qunatity=int(input("Enter stock quantity:"))

if(Stock_name in Dict):
   price=Dict[Stock_name]
   Total_price=price*Stock_quantity
   print("Stock Name is",Stock_name)
   print("Stock Shares is",Stock_quantity)
   print((f"The price of {Stock_name} is ${price}"))
   print("Total value of Shares is",Total_price)
user_input=str(input("Do you want to save the result  in file? (yes/no): ").strip().lower())   
if user_input != "no":
      with open("transactions.txt", "a") as f:  # append mode
       f.write(f"Stock: {Stock_name.upper()}, Quantity: {Stock_quantity}, Price: {price}, Total: {Total_price}\n")
       print("result saved in transactions.txt file")
else:
  print("As you wish")
  
