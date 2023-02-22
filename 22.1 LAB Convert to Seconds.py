#Write a program that reads in hours, minutes, and seconds as input, and outputs the time in seconds only.
hours = int(input())
minutes = int(input())
seconds = int(input())



print(seconds)

# Read in  the hours, minutes, and seconds as user inputed integers.

hours = int(input())
minutes = int(input())
seconds = int(input())

#Convert the time in seconds 

total_seconds = hours * 3600 + minutes * 60 + seconds

# Output the time in seconds 
print("Seconds:", total_seconds)