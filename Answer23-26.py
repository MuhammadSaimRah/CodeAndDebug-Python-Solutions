# Q23. Write a Python program that takes an integer input and prints
# whether it's positive, negative. (Consider 0 as positive)

num=int(input("Enter the number : "))

if num>=0:
    print("The number is Positive")
else:
    print("The number is Negative")

# Q24. Write a program that takes a character as input and prints whether
# it's a vowel or a consonant. (Multiple OR will be used)

char = str(input("Enter a character : "))

if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print("The character is Vowel")
else:
    print("The character is Consonant")

# Q25. Write a program that takes two numbers as input and checks if the
# first number is divisible by the second.
    
num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))

if num1%num2 == 0:
    print("{0} is Divisible By {1}".format(num1,num2))
else:
    print("{0} is Not Divisible By {1}".format(num1,num2) )

# Q26. A student will not be allowed to sit in exam if his/her attendance is
# less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# 1. Print percentage of class attended
# 2. Print Is student is allowed to sit in exam or not

Class_held=int(input("Enter the number of class held : "))

Class_attended=int(input("Enter the number of class Attend : "))

percetage_of_attendance=Class_attended/Class_held*100

if percetage_of_attendance >=75:

    print("you can sit in the exame . Your Attendance percentage is {0}".format(percetage_of_attendance) )
else:
    print("You can not sit in the exame. Your Attendance percentage is ",percetage_of_attendance)