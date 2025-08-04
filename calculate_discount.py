def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount  
    else:
        return price

try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

    if discount >= 20:
        final_price = calculate_discount(original_price, discount)
        print(f"discount applied. Final price: {final_price}")
    else:
        final_price = original_price
        print(f"No discount applicable. Final price: {final_price}")
except ValueError:
    print("Please enter valid value for price.")