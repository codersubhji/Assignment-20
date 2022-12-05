"""9. Write a python program to create a function to check whether a string is a pangram
or not."""
import string
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True

string = 'mumbai'
if(ispangram(string) == True):
   print("It is pangram")
else:
   print("It is not pangram")
      




