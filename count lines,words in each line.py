string='''This is the most straightforward way to count the number
of lines in a text file in Python. The readlines() method reads all
lines from a file and stores it in a list. Next, use the len() function
to find the length of the list which is nothing but total lines present in a file.'''
str=string.split(".")
print("number of lines :",len(str)-1)
for i in range(len(str)-1):
    words=str[i].split()
    print("line ",i+1,":",len(words))
