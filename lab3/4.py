def calculate_price(original_price, discount_percentage=10):
    discount_amount = (discount_percentage / 100) * original_price
    final_price = original_price - discount_amount
    return final_price


original_price = float(input("Enter the original price of the item: "))


use_custom_discount = input("Do you want to provide a custom discount percentage? (yes/no): ").strip().lower()

if use_custom_discount == 'yes':
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_price(original_price, discount_percentage)
else:
   
    final_price = calculate_price(original_price)

print(f"The final price after discount is: {final_price:.2f}")
