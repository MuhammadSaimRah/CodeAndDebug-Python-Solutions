#Q4. Write a Python program to add two numbers entered by the user.

A=int(input("Enter the Number A : " ))

B=int(input("Enter the Number B : " ))

print(f"The Sum of number A and B is  : {A+B}")

#Q5. Convert a string to an integer and vice versa

x = "44"    # This is a string
print(x,type(x))
x = int("44")       # x converted into int type
print(x,type(x))    


y = 11
print(y,type(y)) # the y is now int datatype
y =str(y)
print(y,type(y)) # y converted into string datatype

# Q6. Write a Python program to calculate the area of a rectangle using user
# input for length and width.


length=int(input("Enter the length of Rectangle : "))
width=int(input("Enter the width of Rectangle : "))

print(f"The Area of Rectangle is : {length*width}")

# Q7. Write a Python program to calculate the average of three numbers
# entered by the user.

a=float(input("Enter the number a :"))
b=float(input("Enter the number b :"))
c=float(input("Enter the number c :"))
average=a+b+c/3
print("The Average of Three number is %.2f" %average)

# Q8. Convert a float to an integer and vice versa.

# the answer of this question is same as the question 5  the difference is that in question 5 we convert str into int and now float into int

# Q9. Write a program that converts a temperature in Fahrenheit to Celsius.
#  he formula is: Celsius = (Fahrenheit - 32) * 5/9.



f = 20 #temperature in Fahrenheit
c = float((f - 32) * 5/9)
print(f"The Temperatue in Celsius is %.2f"%c)

# Q10. Calculate sum of 5 subjects and Find percentage.


phy=25
eng=75
math=22
cs=75
ps=45
sum=(ps+cs+math+eng+phy)
percentage=sum/500*100
print(f"The percentage of marks is {percentage}")


# Q11. Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)


match_played=int(input("Enter the number of matches you played  : "))
match_won=int(input("Enter the number of matches you win : "))
match_lost=int(input("Enter the number of matches you lost : "))
tie = (match_played-match_won-match_lost)
points=tie*2+match_won*4
print(f"the number of tie matches is : {tie} and total points is  : {points}")
