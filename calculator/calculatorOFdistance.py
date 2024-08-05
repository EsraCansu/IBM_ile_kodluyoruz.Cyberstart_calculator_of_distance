
import math

# Got input from the user and create tuples for the points
x1 = int(input("Please enter the first value of x point:\n"))
y1 = int(input("Please enter the first value of y point:\n"))
point1 = (x1, y1)

x2 = int(input("Please enter the second value of x point:\n"))
y2 = int(input("Please enter the second value of y point:\n"))
point2 = (x2, y2)

# Calculated the distance between the points
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Printed the result
print("The distance between the points " + str(point1) + " and " + str(point2) + " is: " + str(distance))