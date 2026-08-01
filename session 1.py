# QUes 1
var="ddd"
var2="dedq"
print(var,var2,sep="-")
print("Data","Science","Mentorship","Program","By","CampusX",sep="-", end=None)



# swapping without special syntax
temp=None
num1=int(input("Enter first no. :"))
num2=int(input("Enter Second no. :"))
print(f"Before swapping num1: {num1} and num2: {num2}")
temp=num1
num1=num2
num2=temp
print(f"After swapping num1: {num1} and num2: {num2}")



# conversion of celsius to fahreheit F = 9/5 * C + 32
celsius=float(input("Enter temperature in celsius: "))
fahrenheit  = 9/5 * celsius + 32
print("Temperature in celsius: ",celsius )
print("Using F = 9/5 * celsius + 32")
print("Temperature in fahrenheit: ",fahrenheit )




# find the euclidean distance between two coordinates
# import math then math.sqrt(25) or from math import sqrt then sqrt() directly
import math
x1=float(input("Enter the point X1: "))
y1=float(input("Enter the point Y1: "))
x2=float(input("Enter the point X2: "))
y2=float(input("Enter the point Y2: "))
Euclidean_distance= math.sqrt((pow(x2-x1,2) + pow(y2-y1,2)))
print("Coordinate of x1,y1: ", x1,y1)
print("Coordinate of x2,y2: ", x2,y2)
print("The Euclidean Distance Between two coordinates: ",Euclidean_distance)