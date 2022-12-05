"""4. Write a python program to create a function that checks whether a passed string is
palindrome or not."""

def pldr(str1):
    temp=str1
    
    revs=0
    while temp>0:
        rem=temp%10
        revs=revs*10+rem
        temp=temp//10
    if str1==revs:
        print("Yes it is Palindrome")
    else:
        print("Sorry It is not Palindrome")    
pldr(323)            
        
        