cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")
milk_position = cart.index("milk")
print(f"position of milk: {milk_position}")

cart.remove("apple")

print(f"Removed item using pop: {cart.pop()}")
print("Is banana in the cart ?", "banana" in cart)
print(f"Final cart: {cart}")