# CodeAlpha Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}


def display_stocks():
    print("\nAvailable Stocks:")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")


def calculate_portfolio():
    portfolio = []
    total_investment = 0

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not available. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            price = stock_prices[stock]
            investment = price * quantity

            portfolio.append((stock, quantity, price, investment))
            total_investment += investment

            print(f"{stock}: {quantity} shares × ${price} = ${investment}")

        except ValueError:
            print("Please enter a valid number.")

    print("\n" + "=" * 50)
    print("           STOCK PORTFOLIO SUMMARY")
    print("=" * 50)

    if not portfolio:
        print("No stocks were added.")
        return

    for stock, quantity, price, investment in portfolio:
        print(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Investment: ${investment}"
        )

    print("-" * 50)
    print(f"Total Investment: ${total_investment}")
    print("=" * 50)

    save_result = input("\nDo you want to save the result? (yes/no): ").lower()

    if save_result == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 40 + "\n")

            for stock, quantity, price, investment in portfolio:
                file.write(
                    f"{stock} | Quantity: {quantity} | "
                    f"Price: ${price} | Investment: ${investment}\n"
                )

            file.write("=" * 40 + "\n")
            file.write(f"Total Investment: ${total_investment}\n")

        print("Portfolio saved to portfolio.txt")


print("=" * 40)
print("     CODEALPHA STOCK PORTFOLIO TRACKER")
print("=" * 40)

display_stocks()
calculate_portfolio()
