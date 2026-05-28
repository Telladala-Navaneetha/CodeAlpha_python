import re

# Open and read the input file
with open("input.txt", "r") as file:
    text = file.read()

# Find all email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save emails to another file
with open("emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print("Email addresses extracted successfully!")