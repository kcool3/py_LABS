lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))

# FIXME (1): Finish reading other items into variables, then output the three ingredients
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = int(input("How many servings does this make?\n"))

# Outputting lemonade ingredients and serving size
print(f"\nLemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water:.2f} cup(s) water")
print(f"{agave_nectar:.2f} cup(s) agave nectar")
print()

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

# Prompting the user for desired servings
desired_servings = int(input("How many servings would you like to make?\n"))

# Adjusting ingredient amounts
lemon_juice_cups = lemon_juice_cups / servings * desired_servings
water = water / servings * desired_servings
agave_nectar = agave_nectar / servings * desired_servings
servings = desired_servings

# Outputting lemonade ingredients and serving size
print(f"\nLemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water:.2f} cup(s) water")
print(f"{agave_nectar:.2f} cup(s) agave nectar")


# FIXME (3): Convert and output the ingredients from (2) to gallons

# Converting ingredient measurements to gallons
lemon_juice_gallons = lemon_juice_cups / 16
water_gallons = water / 16
agave_nectar_gallons = agave_nectar / 16

# Outputting lemonade ingredients and serving size
print(f"\nLemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_gallons:.2f} gallon(s) lemon juice")
print(f"{water_gallons:.2f} gallon(s) water")
print(f"{agave_nectar_gallons:.2f} gallon(s) agave nectar")

