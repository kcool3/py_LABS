import math 

#reads the input 
a = float(input())
b = float(input())

# calculate the hypotenuse
c = math.sqrt(a**2 + b**2)

#output the result with two decimal places
print('Hypotenuse: {:.2f}'.format(c))

