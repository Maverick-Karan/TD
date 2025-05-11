# This program checks if file exists, reads a file and displays its content

import os

# Get the file name from the user
file_name = input("Enter the file name to read: ")

# Check if the file exists
if os.path.exists(file_name):
    # Open the file in read mode
    file = open(file_name, "r")

    # Read the entire content of the file
    content = file.read()

    # Display the content
    print("\nContents of the file:")
    print(content)

    # Close the file
    file.close()
else:
    print("File not found.")
