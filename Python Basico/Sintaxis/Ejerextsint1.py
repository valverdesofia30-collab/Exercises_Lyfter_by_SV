price = float(input("Enter the price of the product:"))
if price >= 100:
    discount = price * 0.10
    final_price = price - discount
elif price <100:
    discount = price * 0.02
    final_price = price - discount
print(f"The final price after discount is: {final_price}")
