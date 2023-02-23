import math 
# read input 
radius = float(input())
height = float(input())

#calculate volume and surface area
volume = math.pi * pow(radius, 2) * height
surface_area = 2 *math.pi * radius * height + 2 * math.pi * pow(radius, 2)


#print the output
print('Volume: {:.1f} cubic inches'.format(volume))
print('Surface area: {:.1f} square inches'.format(surface_area))