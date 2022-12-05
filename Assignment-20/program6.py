"""6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30."""
def squares():
  list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,171,18,19,20,21,22,23,24,25,26,27,28,29,30]
  for i in list1:
    if i in (1,4,9,16,25):
       print(i,end=" ")
squares()   