somestring = "here is a string"
substring = "string"

if substring in somestring:
    newstring = somestring.replace(substring, "")
print(newstring)