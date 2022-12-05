"""10. Write a python program to create a function to check whether a string is an anagram
or not."""
def isanagram(s1,s2):
    #checking terms of both string are in shorted or not 
    if sorted(s1)==sorted(s2):
        print("the strings are anagram ")
    else:
        print("the strings are not anagram")    
s1="listen"        
s2="silent"
isanagram(s1, s2)