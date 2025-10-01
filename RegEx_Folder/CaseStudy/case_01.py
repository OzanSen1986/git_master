import re
from collections import Counter

team = "John: 30, Jane: 25, Richard: 50 "
message = 'Call the emergency line at 112-657'

# find a match inside the list:
matches = re.findall(r"(\w+): (\d+)", team)
print(matches)

# Non capturing groups
result = re.search(r"(?:\d{3})-(\d{3})", '123-456')
print(result.group(1))

# Named Groups
pattern = r"(?P<name>\w+):(?P<age>\d+)"
match = re.search(pattern, "Alice: 30")
if match:
    print(match.group("name")) 
    print(match.group("age"))





















   