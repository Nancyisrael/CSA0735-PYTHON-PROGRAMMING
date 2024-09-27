names=input("enter names:").split()
order=input("enter the order(A/D) : ")
if order.upper()=='A':
  names.sort()
  print("ascending order :",names)
elif order.upper()=='D':
  names.sort(reverse=True)
  print("decending order :",names)
else:
    print("invalid order")
