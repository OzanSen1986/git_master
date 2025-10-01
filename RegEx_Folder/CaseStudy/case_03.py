import re
# Email Validation
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, "oznsn98@hotmail.com"):
    print("Valid email")
else:
    print("Invalid email due to some special characters not allowed.")

# Extract URLs
text = "Visit https://example.com or http://test.org and http://wikepidia.com"
urls = re.findall(r"https?://[^\s]+", text)

print(urls)

# Password Strength Check
# At least 8 chars, 1 uppercase, 1 digit, 1 special char
pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
if re.match(pattern, "StrongPass1!"):
    print("Valid password")
else:
    print("Invalid password")