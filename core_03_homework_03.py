import re

# Function to format phone numbers
def normalize_phone(phone_number: str) -> str:
    """
    Formats a given phone number

    Parameters:
        phone_number (str): phone number to be formatted
    
    Returns:
        (str):  formatted phone number or empty string if the phone number 
                is supposed to be Ukrainian and broken
    """
    # Phone numbers starting with "+" followed by varying number of digits
    if "+" in phone_number:
        _, number_after_plus = phone_number.split("+")
        return "+" + re.sub(r"\D", "", number_after_plus)
    # Incomplete Ukrainian phone numbers
    only_numbers = re.sub(r"\D", "", phone_number)
    if len(only_numbers) == 12:
        return "+" + only_numbers
    if len(only_numbers) == 10:
        return "+38" + only_numbers
    # Broken Ukrainian phone numbers
    return ""
