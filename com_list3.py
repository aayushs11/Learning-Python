var= [2,3,4,5,6,7,8,9]
print(var)

#square of even numbers
num1= [x**2 for x in var if x%2==0]
print('The square of even number are:',num1)

#square of odd numbers
num2= [x**2 for x in var if x%2!=0]
print('The square of odd number are:',num2)
#OR
num3= [x**2 for x in var if x%2==1]
print('ALternative! The square of odf number are:',num3)