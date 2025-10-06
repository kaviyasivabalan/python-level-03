print("Government of Tamil Nadu")
print("Electricity Board")
print("-----------------")
print("Bill Receipt")
print("------------")
no=int(input("enter the EB.No:"))
Name=input("enter the customer name:")
previous=int(input("enter the previous unit:"))
current=int(input("enter the current unit:"))
unit=current-previous
print("unit consumed:",unit)
if(unit>=1000):
   amt=unit*10
   print("amount to be paid:",amt)
elif(unit>=500):
   amt=unit*5
   print("amount to be paid:",amt)
elif(unit>=100):
   amt=unit*2
   print("amount to be paid:",amt)
else:
   print("amount to be paid:",nill)
