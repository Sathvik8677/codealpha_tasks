stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2800}
total_investment = 0

print("Available stocks:", stock_prices)

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty = int(input(f"How many shares of {stock}? "))
        total_investment += stock_prices[stock] * qty
    else:
        print("Stock not found!")

print("\nTotal Investment: $", total_investment)
