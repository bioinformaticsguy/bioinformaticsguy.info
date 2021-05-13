string_without_line_breaks = ""

with open('foo.txt', "r+") as file:
    for line in file:
        stripped_line = line.rstrip()
        string_without_line_breaks += stripped_line


print(string_without_line_breaks)
