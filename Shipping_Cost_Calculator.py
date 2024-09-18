# Shipping Cost Calculator

# Input package weight and shipping rate.

weight  = float(input("Enter the package weight in kilogram: "))
rate = float(input("Enter the shipping rate per kilogram: "))

# Calculate shipping cost
shipping_cost = weight * rate

# Display the result
print(f"shipping Cost: {shipping_cost} USD")
