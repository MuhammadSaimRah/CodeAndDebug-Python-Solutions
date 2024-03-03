# Q12. Write a Python program that takes two numbers as input and
# performs the following operations: addition, subtraction, multiplication,
# division, and modulus. Display the results.

a=int(input("Enter the Value of  number a  : "))
b=int(input("Enter the value of number b : "))

print(f"Addition of Numbers is : {a+b}")

print(f"Subtraction of Numbers is : {a-b}")

print(f"Subtraction of Numbers is : {a+b}")

print(f"Division of Numbers is : {a/b}")

print(f"Modulus of Numbers is : {a%b}")


# Q13. Write a Python program to swap the values of two variables without
# using a temporary variable.

a=int(input("Enter the Value of  variable a  : "))
b=int(input("Enter the value of variable b : "))
a=a+b
b=a-b
a=a-b

print("The Value of a is  now :" , a )
print("The value of b is now " , b )


# .
# Q15. Write a Python program that takes the radius of a circle as input and
# calculates its area. Use the formula: Area = 3.14 * r^2.

Radius=int(input("Enter the Value of Radius of circle   : "))

Area = 3.14 * Radius**2

print(f"The Area of circle is {Area}")