
    # List of profane words to censor
profane_words = ["Motherfucking bastard", "fucker"]

with open("Cleansing.txt", "r+") as f:
    # Read all lines from the file
    lines = f.readlines()
    
    # Create a new list for updated lines
    updated_lines = []
    
    for line in lines:
        # Replace profane words in the line with '####'
        for word in profane_words:
            # Perform case-insensitive replacement
            line = line.replace(word, "####").replace(word.upper(), "####").replace(word.lower(), "####")
        updated_lines.append(line)
    
    # Move the file cursor to the beginning and clear the file
    f.seek(0)
    f.truncate()
    
    # Write the updated lines back to the file
    f.writelines(updated_lines)
    # The original code whihc didd not working
    
    """a= ["Motherfucking bastard ","fucker"]
with open("Cleansing.txt","r+") as  f:
    f.seek(0)
    Updated_list=[]
   #  d=f.readlines()as we are using f.readlines cursor is already at the end of file dut to this 
    #f.redlines is useless due to this we hace to use f.seek to return to is orignal value
    c=f.readlines()
    for i in c:
        for j in a:
            if j.upper() == i.upper():#
                 Here is main logic erroe bcoz this is comparing whole statment with a line whihc is not what we want due to this it does no\
            due to this we were not able to meet the condition and code was not working  
                c=c.replace(j,"####")
                Updated_list.append(i)
            else:
                Updated_list.append(i)
    f.seek(0)
    f.truncate()
    f.writelines(Updated_list )"""