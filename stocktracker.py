stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 130,
    "MSFT": 320
}

total_investment = 0

print("Stock Portfolio Tracker")
print("Type 'done' to finish\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        price = stock_prices[stock]
        total = price * quantity

        total_investment += total

        print(f"{stock} = {quantity} shares × ${price} = ${total}\n")
    else:
        print("Stock not found!\n")

print("\nTotal Investment Value = $", total_investment)
