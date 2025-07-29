import datetime

# Get the current date and time
now = datetime.datetime.now()

# Extract day of the week
day_of_week = now.strftime("%A")

# Print results
print("Current Date and Time:", now)
print("Today is:", day_of_week)