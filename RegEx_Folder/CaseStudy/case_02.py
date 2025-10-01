import re

# Common operations

#Substitution(Replace)
text = "Python 2.7, Python 3.6"

new_text = re.sub(r"Python \d\.\d", "Python X", text)
print(new_text)

#Splitting strings
word_to_split = "Hello, world! How are you?"
result = re.split(r"\W", word_to_split)
print(result)

# compiling patterns
pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
result = pattern.search("Call 555-123-4567")

if result:
    print(result.group())

# Flags for special behavior
text = "Python\npython\nPYTHON"
result = re.findall(r"^python", text, flags= re.I | re.M)
print(result)
print(type(result)) # dataType: List












