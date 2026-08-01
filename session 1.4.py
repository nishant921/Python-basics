#  Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
A1=int(input("Enter first AP Number a1: "))
A2=int(input("Enter second AP Number a2: "))
n=int(input("Enter the nth term of AP: "))

d=A2-A1
Nth_term = A1 + (n-1) * d
print("The Last NTH TERM Of AP will be A",n," : ", Nth_term,sep="")