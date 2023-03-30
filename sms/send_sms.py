import africastalking
from decouple import config

# Set your credentials
username = config("AT_USERNAME")
api_key = config("AT_API_KEY")

# Initialize the SDK
africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS

# Set the message recipients and the message body
recipients= []
# read numbers from a file
with open("recipients.txt", "r") as f:
    for line in f:
        # pick only the last 9 digits removing any whitespaces
        num = line
        # remove spaces
        num = num.strip().replace(" ", "")
        # add the country code
        num = f"+254{num[-9:]}"
        print(num)
        # add to the list
        recipients.append(num)

        
message = "Hello, from GDSC KARATINA UNIVERSITY!"

# Send the message
response = sms.send(message, recipients)

# Print the response
print(response)
