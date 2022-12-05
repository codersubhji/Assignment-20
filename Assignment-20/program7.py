#7. Write a python program to access a function inside a function.
def fun1():
    print("first function print")
    def fun2(a,b):
        c=a+b
        print("sum of two number is ..:",c)
    fun2(3,10)
fun1() 
       