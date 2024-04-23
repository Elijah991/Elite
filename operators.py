# Example code using operators and if statement

# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if num1 is greater than num2
if num1 > num2:
    print("The first number is greater than the second number.")
elif num1 < num2:
    print("The first number is smaller than the second number.")
else:
    print("Both numbers are equal.")

# Perform arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

# Display the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)