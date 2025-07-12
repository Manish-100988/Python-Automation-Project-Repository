import re

text = "hello world"
match = re.search("hello", text)

if match:
    print("Found!")
else:
    print("Not found!")