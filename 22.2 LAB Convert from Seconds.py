# Read in the total number of seconds as an integer
total_seconds = int(input())

# Calculate the number of hours, minutes, and seconds
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Output the time in hours, minutes, and seconds
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)