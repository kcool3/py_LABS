# read the input 
num_pizzas = int(input())

#Calculate the subtotal and total with tax
pizza_price = 9.99
subtotal = num_pizzas * pizza_price
tax_rate = 0.06
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

#output the results with the correct formatting
print('Subtotal: ${:.2f}'.format(subtotal))
print('Total due: ${:.2f}'.format(total))
