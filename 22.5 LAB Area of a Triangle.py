import math 
#Read inputs 
a = float(input())
b = float(input())
c = float(input())

#Calculate the semi-perimeter
s = (a + b + c) / 2

#calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))


#print the output with three decimal places
print('The area of the trianfle is: {:.3f}'.format(area))

