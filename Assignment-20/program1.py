"""1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements."""
def funs():
   my_list=[10,20,20,30,40,40,10,50,30,50]
   print("My original list is ",my_list)
   print("And")
   my_set=set(my_list)
   my_new_list=list(my_set)
   print("My new list is",my_new_list)
   
   
funs()    
