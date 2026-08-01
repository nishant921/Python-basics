# Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.

import math

print("------Dimensions of milk tank-------") #tank is cuboid volume= L x b x h
length=float(input("Enter the Length of the milk tank: "))
breadth=float(input("Enter the breadth of the milk tank: "))
height=float(input("Enter the height of the milk tank: "))


print("------Dimensions of Milk Glass-------") # glass is a cylinder volume= pie x r^2 x H
g_height=float(input("Enter the Height of Milk Glass: "))
g_radius=float(input("Enter the radius of glass: "))

# volume of tank
T_volume=length*breadth*height
print("Volume of the Tank ", T_volume)

# volume of glass
G_volume=  math.pi*pow(g_radius,2)*g_height
print("Volume of the Tank ", G_volume)

# Result
print("No. of glasses of milk approx: ", int(T_volume/G_volume))