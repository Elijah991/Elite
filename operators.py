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
# print("Sum:", sum_result)
# print("Difference:", difference_result)
# print("Product:", product_result)
# print("Quotient:", quotient_result)

# Example code with operators and if statement

# Define two variables
a = 10
b = 5

# Perform arithmetic operations
sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b

# Check conditions using if statement
if sum_result > 15:
    print("The sum is greater than 15.")
elif difference_result < 0:
    print("The difference is negative.")
elif product_result % 2 == 0:
    print("The product is an even number.")
else:
    print("None of the conditions are met.")

# Output the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)