"""2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not."""
def Num(num):
#if you want to take input by user to use this mathod 
# otherwise as a parameter as well as use 
    # num=int(input("Enter any number to check the number is prime or not...:"))
    for n in range(2,num):
        if num%n!=0:
            print(num,"is a prime number")
            break
        else:
           print(num,"is not a prime number")
           break
Num(2)                