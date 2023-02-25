import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?w\w+\.(edu)$", email.lower()):
    print("Valid")
else:
    print("Invalid")
