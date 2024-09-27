def calculate_interest(amount,years,sc):
   if sc.lower()=='y':
      rate=12
   else:
       rate=10
   interest=(amount*years*rate)//100
   return interest
amount=float(input("enter amount: "))
years=int(input("enter number of years: "))
sc=input("enter senior citizen or not(y/n): ")
print("Simple Interest ",calculate_interest(amount,years,sc))
