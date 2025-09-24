def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")
