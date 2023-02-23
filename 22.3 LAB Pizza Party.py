import math 
#read input
num_people = int(input())

#Calculate the number of pizzas needed
num_pizzas = math.ceil(num_people * 2 / 12)

#Calculate the cost of the pizzas

cost = num_pizzas * 14.95

#Output the result with two decimal places

print( 'Pizzas: {}'.format(num_pizzas))
print('Cost: ${:.2f}'.format(cost))
