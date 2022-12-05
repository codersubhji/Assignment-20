"""3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""

def l1():
    
    list1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in list1:
        if i%2==0:
            print("Even number in list is ..:",i)
         
l1()