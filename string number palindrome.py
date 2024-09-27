choice=input("enter (s/n): ")
if(choice.lower()=='s'):
    string="madam"
    reverse=""
    for i in range(len(string)-1,-1,-1):
        reverse+=string[i]
    if(string==reverse):
       print("palindrome")
    else:
       print("not a palindrome")
    
elif(choice.lower()=='n'):
    n=121
    rev=0
    k=n
    while n>0:
        rev=rev*10+n%10
        n//=10
    if(k==rev):
        print("number is palindrome")
    else:
        print("number is not a palindrome")
    
       
    
