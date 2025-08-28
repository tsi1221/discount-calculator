def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if final_price < original_price:
    print(f"Final price after discount: {final_price}")
else:
    print(f"No discount applied. Original price: {original_price}")
