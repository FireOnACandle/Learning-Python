print ("Basic Addition")
print() 

x = int (input ("Enter the first number :"))
x1 = int (input ("Enter the second number :"))
sum = x + x1

print()
print("The sum of those two numbers is :", sum) 

if (sum % 2)== 0:
 print("Sum of those two numbers is Even")
  
else:
 print("Sum of those two numbers is Odd") 
 
if sum <0:
 print("The number is negative")
 
elif sum > 0:
 print("The number is positive")

else:
 print("Sum is 0")
