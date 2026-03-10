#Stock Portfolio Tracker
stock = {
    "AAPL" : 180,
    "TSLA" : 250,
    "AMZN" : 130,
    "GOOG" : 140
}
total =0
n= int(input("enter number of stock you have :"))
for i in range(n):
    name = input("Enter stock name:").upper()
    qty = int(input("Enter quantity:"))
    if name in stock:
        value = stock[name]*qty
        total += value
print("Total Investment Value: " ,total)        
        