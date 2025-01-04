#lab2_item2
def calculate_discount():
    while True:
        try:
            # Input the total purchase amount
            total_purchase = float(input("Enter the total purchase amount: "))
            
            # Determine the discount
            if total_purchase > 5000:
                discount_rate = 0.10
            else:
                discount_rate = 0.05

            discount = total_purchase * discount_rate
            final_price = total_purchase - discount

            # Display the results
            print(f"Initial Purchase Amount: {total_purchase:.2f}")
            print(f"Discount: {discount:.2f}")
            print(f"Final Price: {final_price:.2f}")

            # Ask if the user wants to try again
            try_again = input("Do you want to try again? (yes/no): ").strip().lower()
            if try_again != "yes":
                print("Thank you!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function
calculate_discount()
