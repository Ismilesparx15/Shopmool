import json

# Load the configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Access credentials
URL = config["url"]
MOBILE_NUMBER = config["mobile_number"]
OTP = config["otp"]

# Product details
COLOR = "Green"  # Replace with the actual color option value
# SIZE = "desired_size_option"    # Replace with the actual size option value
