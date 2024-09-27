string="Temple"
repeted=""
for letter in string:
    if string.count(letter)>1 and letter not in repeted:
        repeted+=letter
print("number of repeted letters :",len(repeted))
print("repeted letter: ",repeted)
        
