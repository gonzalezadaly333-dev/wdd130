import math
# Write a program to compute the areas of three different shapes: a 
# square, a rectangle, and a circle. Prompt for the necessary 
# information, then compute and display the area, as follows:
# 1. Initialize
squareSize = 0
areaOfsquare = 0
rectanglewidth = 0
rectanglelength = 0
areaOfRectangle =0
areaOfCircle = 0
circleRadius = 0
# 2. Get values
squareSize = int(input("What is the length of a side of the square? "))
#3. Calculate
areaOfsquare = squareSize * squareSize
#4. Output
print("The area of the square is: " + str (areaOfsquare))
rectanglelength = int(input("What is the length of rectangle?"))
rectanglewidth = int(input("What is the width of rectangle?"))
#3. Calculate
areaOfsquare = squareSize * squareSize
#4. Output
print("The area of the square is: " + str (areaOfsquare))
print(f"The area fo the square is: {areaOfsquare}")
areaOfRectangle = rectanglelength * rectanglewidth
print("The area of the rectangle is: "+ str(areaOfRectangle))
circleRadius = int(input("What is the radius of the circle?"))
areaOfCircle = math.pi * pow(circleRadius, 2)
# print("The area of the circle is: " + str (areaOfCircle))
print(f"The area of the circle is: {areaOfCircle:.2f}")


