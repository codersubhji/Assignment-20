"""5. Write a python program to create a function to find the Min of three numbers."""
def Minmum(num1,num2,num3):
   if num3<num2 and num3<num1:
      print("minimm number is ",num3)
   elif num2<num3 and num2<num1:
      print("minimum number is ",num2) 
   else:
      print("minimum number is ",num1)
Minmum(10, 20, 50)      
         