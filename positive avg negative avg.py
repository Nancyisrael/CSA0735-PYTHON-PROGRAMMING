lp=list()
ln=list()
while True:
    s=int(input("enter any number :"))
    if s==-1:
        break
    else:
        if s>0:
            lp.append(s)
        elif s<0:
            ln.append(s)
            
ps=sum(lp)
ns=sum(ln)
pc=len(lp)
nc=len(ln)
pa=ps/pc
na=ns/nc
print("positive average :",pa)
print("negative average :",na)

    
