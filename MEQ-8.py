tuple1=(1,2,3)
tuple2=(4,5,6)
count=0
concatenatedtuple=tuple1+tuple2
print("concatenated tuple: ",concatenatedtuple)
for i in range(len(concatenatedtuple)):
    if concatenatedtuple[i]==3:
       count+=1
       print("index of element :",i)
print("number of occurences : ",count)
       
