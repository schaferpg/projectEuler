# Problme 22
# https://projecteuler.net/problem=22

import string


file = open("/Users/peter/Documents/0022_names.txt")
content = file.read()
file.close()

# splits lines seperated by comma, removes double quotation marks and sorts it
# alphabetically 

replace_content = content.replace('"','')
split_content = replace_content.split(",")
split_content = (sorted(split_content))

# Creates a list of upper case alphabet letters
upper = list(string.ascii_uppercase)

# Takes the input of name and returns the value of the letter's postion in the
# alphabet added together
def calculate_name_value(name):
    total_name = 0

    for n in name:
        total_name += upper.index(n) + 1
        
    return total_name

total = 0

# While loop that adds to the total
# the postion in the list * the numeric value of the word.
i = 0
while (i < len(split_content)): 
    total += (calculate_name_value(split_content[i]) * (i+1))
    i += 1
    
print(total)
