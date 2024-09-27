num=(1,2,3,4,5,6,7,8,9)
ec=0
oc=0
for i in range(len(num)):
    if i%2==0:
        ec+=1
    else:
        oc+=1
print("even count",ec)
print("oddd count:",oc)
