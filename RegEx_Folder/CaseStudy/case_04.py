import re

text = "foo, foobar"

match = re.match(r"foo$", text)

if match:
    print("Matched")
else:
    print("Invalid match")