def main():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 140.00,
        "MSFT": 400.00
    }

    portfolio = []
    total_value = 0

    print("--- Simple Stock Tracker ---")
    print(f"Available stocks: {', '.join(stock_prices.keys())}\n")

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"How many shares of {symbol} do you own? "))
                investment = quantity * stock_prices[symbol]
                total_value += investment
                portfolio.append(f"{symbol}: {quantity} shares (${investment:,.2f})")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Stock not found in price list. Try AAPL, TSLA, GOOGL, or MSFT.")

    # Display Results
    print("\n--- Portfolio Summary ---")
    for item in portfolio:
        print(item)
    print(f"Total Investment Value: ${total_value:,.2f}")

    # File Handling (Optional)
    save = input("\nSave results to file? (y/n): ").lower()
    if save == 'y':
        with open("portfolio_summary.txt", "w") as f:
            f.write("Portfolio Summary\n" + "="*20 + "\n")
            for item in portfolio:
                f.write(item + "\n")
            f.write(f"Total Value: ${total_value:,.2f}")
        print("Saved to portfolio_summary.txt")

if __name__ == "__main__":
    main()