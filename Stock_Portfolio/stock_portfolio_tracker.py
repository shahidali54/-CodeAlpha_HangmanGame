def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 150,
        "MSFT": 300,
        "AMZN": 120
    }

    portfolio = {}
    total_value = 0

    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Enter stock name and quantity (type 'done' to finish).")

    # Collect user input
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").upper().strip()
        if stock_name.lower() == 'done':
            break
        if stock_name not in stock_prices:
            print("Invalid stock name. Please choose from:", ", ".join(stock_prices.keys()))
            continue
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            portfolio[stock_name] = quantity
        except ValueError:
            print("Please enter a valid number for quantity.")

    # Calculate total value
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total_value += value
        print(f"{stock}: {quantity} shares @ ${stock_prices[stock]} = ${value}")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

    # Save to file
    save = input("Save portfolio to file? (yes/no): ").lower().strip()
    if save == 'yes':
        with open('portfolio.txt', 'w') as file:
            file.write("Stock Portfolio\n")
            file.write("---------------\n")
            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity
                file.write(f"{stock}: {quantity} shares @ ${stock_prices[stock]} = ${value}\n")
            file.write(f"\nTotal Portfolio Value: ${total_value:.2f}\n")
        print("Portfolio saved to 'portfolio.txt'.")

# Run the tracker
if __name__ == "__main__":
    stock_portfolio_tracker()