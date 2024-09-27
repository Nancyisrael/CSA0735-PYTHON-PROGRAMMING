str="I am a  Programmer"
ch='p'
for i in range(len(str)):
    if str[i].lower()==ch:
        print("character is found at index :",i)
        break
else:
        print("character was not found")
       
