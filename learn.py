Name = input("What is your name?")
Age = int(input("How old are you:"))

print(Name, "is", Age, "years old")

# # Function to calculate the area of a rectangle
# def calculate_area(length, width):
#     area = length * width
#     return area

# User input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and display the area
area = calculate_area(length, width)
print("The area of the rectangle is:", area)

class MyClass:
    def my_method(self):
        print("Hello, World!")

# Create an instance of MyClass
my_instance = MyClass()

# Call the my_method of my_instance
my_instance.my_method()