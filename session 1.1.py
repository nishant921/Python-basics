# find the simple interest when the value of principle,rate of interest and time period
principle = float(input("Enter the principle Amount: "))
Rate = float(input("Enter the Rate of Interest: "))
Time = float(input("Enter the Time Period: "))
SI = (principle*Rate*Time)/100
print("SIMPLE INTEREST : ", SI)



#  Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
heads=int(input("Enter the No. of Heads: "))
legs=int(input("Enter the No. of Legs: "))
# Dogs=(legs-2*heads)//2  #assuming all where chicken 
# Chicken=heads-Dogs  #logic = Elimination method
Chicken=(4*heads-legs)//2  #assuming all where Dogs
Dogs=heads-Chicken  #logic = Elimination method
print("Total NO. Of Dog's: ",Dogs)
print("Total NO. Of Chicken: ",Chicken)




# find the sum of squares of first n natural numbers where n will be provided by the user.
num=int(input("Enter the total no. of first n natural numbers: "))
ssum=0
i=1
while i<=num:
    print(i)
    square=pow(i,2)
    ssum=ssum+square
    i=i+1
print("Sum of squares of the first",num,"natural numbers: ",ssum)

# The formula for the sum of squares of first n natural numbers is: n(n+1)(2n+1)/6
ssum=(num*(num+1)*(2*num+1))/6
print("Sum of squares of the first",num,"natural numbers: ",ssum)
