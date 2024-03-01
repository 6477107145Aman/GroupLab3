# Name : Amanjot Singh
# Date : 29 February, 2024
# Description : Creating a program for calculating area of different shapes

import math
# Establishing a class named as ShapesAreaCalculator
class ShapesAreaCalculator:
   
# Creating a definition for calculating area of circle   
    @staticmethod 
    def area_of_circle(radius):
        return math.pi * radius ** 2
    
# Creating a definition for calculating area of trapezium
    @staticmethod
    def area_of_trapezium(base1, base2, height):
        return 0.5 * (base1 + base2) * height
    
# Creating a definition for calculating area of ellipse
    @staticmethod
    def area_of_ellipse(major_axis, minor_axis):
        return math.pi * major_axis * minor_axis
    
# Creating a definition for calculating area of rhombus   
    @staticmethod
    def area_of_rhombus(diagonal1, diagonal2):
        return 0.5 * diagonal1 * diagonal2

if __name__ == "__main__":
    # Creating a prompt that will ask the user to enter the shape which they want
    shape_choice = input("Enter your shape choice (circle, trapezium, ellipse, rhombus): ").lower()

    calculator = ShapesAreaCalculator()
# If the user chooses circle, then display a prompt asking the user to enter the radius of circle
    if shape_choice == "circle":
        radius = float(input("Enter the radius of circle: "))
        result = calculator.area_of_circle(radius)
# If the user chooses trapezium, then display three prompts asking the user to enter length of the first and second base and height of the trapzeium-
        # -respectively        
    elif shape_choice == "trapezium":
        base1 = float(input("Enter the length of the base one of trapezium: "))
        base2 = float(input("Enter the length of the base two of trapezium: "))
        height = float(input("Enter the height of the trapezium: "))
        result = calculator.area_of_trapezium(base1, base2, height)
# If the user chooses ellipse, then display two prompts asking the user to enter the length of the major and minor axis        
    elif shape_choice == "ellipse":
        major_axis = float(input("Enter the length of the major axis of ellipse: "))
        minor_axis = float(input("Enter the length of the minor axis of ellipse: "))
        result = calculator.area_of_ellipse(major_axis, minor_axis)
# If the user chooses rhombus, then display two prompts asking the user to enter length of the first and second diagonal of rhombus       
    elif shape_choice == "rhombus":
        diagonal1 = float(input("Enter the length of the first diagonal of rhombus: "))
        diagonal2 = float(input("Enter the length of the second diagonal of rhombus: "))
        result = calculator.area_of_rhombus(diagonal1, diagonal2)
# If the user enters any invalid shape then display an error and ask to choose appropriate shape         
    else:
        print("Error!! Choose an appropriate shape..")
        result = None
# Displaying the result
    if result is not None:
        print(f"The area of {shape_choice} is: {result}")
