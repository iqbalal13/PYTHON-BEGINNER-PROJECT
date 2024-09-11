# Get user input for name and date of birth
name = input("Enter your name: ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")

# Extract the year from the date of birth
year_of_birth = dob.split('-')[0]

# Check the year of birth to categorize the person
if int(year_of_birth) >= 2000:
    category = "Generation Z"
elif int(year_of_birth) >= 1980:
    category = "Millennial"
elif int(year_of_birth) >= 1965:
    category = "Generation X"
else:
    category = "Baby Boomer or earlier"

# Print the name, date of birth, and category
print(f"Name: {name}")
print(f"Date of Birth: {dob}")
print(f"Category: {category}")