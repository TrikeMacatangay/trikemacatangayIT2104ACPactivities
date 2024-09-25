def main():
    while True:
        try:
            amount = float(input("Enter the total purchase amount: "))
            discount_rate = 0.10 if amount > 5000 else 0.05
            discount = amount * discount_rate
            final_price = amount - discount

            print(f"Initial Purchase Amount: {amount:.2f}")
            print(f"Discount: {discount:.2f}")
            print(f"Final Price: {final_price:.2f}")

            if input("Do you want to try again? (yes/no): ").strip().lower() != 'yes':
                print("Thank you!")
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
