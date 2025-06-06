with open("Moiz.txt", "r+") as f:
    c = f.read()  # Read the entire content of the file
    a = "Oversmart"
    if a.upper() in c.upper():  # Check if the capitalized word exists in the content
        d = c.replace(a, "####")  # Replace the word with "####"
        print(d)
        # Go back to the beginning of the file
        f.seek(0)
        f.truncate()  # Remove old content from the file
        
        # Write the modified content back to the file
        f.write(d)  # Write the modified content