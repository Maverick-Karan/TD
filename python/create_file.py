
# This program creates a file and writes to it with inouts from user

# Get the file name from the user
file_name = input("Enter the name of the file to create: ")

# Open the file in write mode
file = open(file_name, "w")

# Get content from the user
data = input("Enter the text to write to the file: ")

# Write the data to the file
file.write(data)

# Confirm what's written
print(f"\nData written to file '{file_name}':")
print(data)

# Close the file
file.close()
