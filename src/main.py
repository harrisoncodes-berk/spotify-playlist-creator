from dotenv import dotenv_values

config = dotenv_values(".env")

CLIENT_ID = config["CLIENT_ID"]
CLIENT_SECRET = config["CLIENT_SECRET"]

print("Client ID: " + CLIENT_ID)
print("Client Secret: " + CLIENT_SECRET)