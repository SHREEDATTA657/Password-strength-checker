import re
# Function to check the strength of a password
def check_password_strength(password):
    # Check for minimum length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."

    # Check for digits
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>=+\[\]\\;\'/~`]', password):
        return "Weak: Password must contain at least one special character."

    return "Strong: Your password is strong."
# Function to prompt the user for a password and check its strength
def password_strength_checker():
        while True:
             password = input("Enter your password (or 'quit' to exit) ")
             if password.lower() == 'quit':
                 print("Exiting the password strength checker.")
                 break
             strength = check_password_strength(password)
             print(strength)
# Main function to run the password strength checker
if __name__ == "__main__":
    password_strength_checker()