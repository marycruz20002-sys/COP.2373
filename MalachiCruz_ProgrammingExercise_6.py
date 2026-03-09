import re

def validate_phone_number(phone_number):
    """
    Validates a US phone number in various formats.
    """
    # Regex allows formats like: (XXX) XXX-XXXX, XXX-XXX-XXXX, XXX XXX XXXX, XXXXXXXXXX, etc.
    # It also handles an optional leading '1' country code.
    pattern = re.compile(r"^(1\s*[-.\s]*)?\(?\d{3}\)?\s*[-.\s]?\d{3}\s*[-.\s]?\d{4}$")
    return bool(re.match(pattern, phone_number))

def validate_ssn(ssn):
    """
    Validates a US Social Security Number in XXX-XX-XXXX or XXXXXXXXX format.
    It excludes certain invalid number ranges (e.g., 000, 666 area numbers).
    """
    # Stricter pattern excluding known invalid ranges
    # This regex is an approximation of validity and only checks format, not if the number is actually issued
    pattern = re.compile(r"^(?!000|666)(?:[0-8][0-9]{2})[- ]?(?!00)[0-9]{2}[- ]?(?!0000)[0-9]{4}$")
    return bool(re.match(pattern, ssn))

def validate_zip_code(zip_code):
    """
    Validates a US zip code in 5-digit (XXXXX) or ZIP+4 (XXXXX-XXXX) format.
    """
    # Pattern matches 5 digits, optionally followed by a hyphen and 4 more digits
    pattern = re.compile(r"^\d{5}(?:[-\s]\d{4})?$")
    return bool(re.match(pattern, zip_code))

def main():
    """
    Gets input from the user and displays if the inputs are valid.
    """
    print("--- Input Validation Tool ---")
    phone_input = input("Enter a phone number: ")
    ssn_input = input("Enter a Social Security Number: ")
    zip_input = input("Enter a ZIP code: ")

    print("\n--- Validation Results ---")
    # Validate and display results
    print(f"Phone Number: {'Valid' if validate_phone_number(phone_input) else 'Invalid'}")
    print(f"SSN: {'Valid' if validate_ssn(ssn_input) else 'Invalid'}")
    print(f"ZIP Code: {'Valid' if validate_zip_code(zip_input) else 'Invalid'}")

if __name__ == "__main__":
    main()
