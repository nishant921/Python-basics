# Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

num1 = int(input("Enter numerator of first fraction: "))
den1 = int(input("Enter denominator of first fraction: "))
print("first fraction: ", num1, '/', den1)

num2 = int(input("Enter numerator of second fraction: "))
den2 = int(input("Enter denominator of second fraction: "))
print("second fraction: ", num2, '/', den2)
print()

if den1==den2:
    numerator=num1+num2
    denominator=den1
    print("Sum of fractions =", numerator, "/", denominator)
else:
    numerator = (num1 * den2) + (num2 * den1)
    denominator = den1 * den2
    print("Sum of fractions =", numerator, "/", denominator)