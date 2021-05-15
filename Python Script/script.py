string_without_line_breaks = ""

with open('foo.txt', "r+") as file:
    for line in file:
        stripped_line = line.rstrip() + " "
        string_without_line_breaks += stripped_line
    
    
with open ("oneLine.md", "w") as file:
    file.write(string_without_line_breaks)
    


# print(string_without_line_breaks)
