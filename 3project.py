   
import re

try:
    file = open("data.txt", "r")
    text = file.read()

    emails = re.findall(r'\S+@\S+', text)

    with open("emails.txt", "w") as output:
        for email in emails:
            output.write(email + "\n")

    print("Emails extracted successfully")

except FileNotFoundError:
    print("data.txt file not found. Please check file location.")