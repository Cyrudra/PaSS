import random
import string

# Define colors for terminal output
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
cyan = '\033[96m'
clear = '\033[0m'
bold = '\033[01m'

# Colorful logo for ALEX
def print_logo():
    print(red + bold + "      *****     ")
    print(red + bold + "    *       *   ")
    print(red + bold + "   *  O   O  *  ")
    print(red + bold + "   *    \\_/    *  ")
    print(red + bold + "    *         *   ")
    print(red + bold + "      *****     ")
    print(lgreen + "         PASS  V1.0 \n" + clear)

def generate_passwords(personal_data):
    passwords = set()  # Use a set to avoid duplicates

    # Simple password variations
    for data in personal_data:
        passwords.add(data.lower())
        passwords.add(data.upper())
        passwords.add(data.capitalize())
        passwords.add(data + "123")
        passwords.add(data + "!")
        passwords.add("!" + data)

    # Adding combinations
    if len(personal_data) > 1:
        combined = personal_data[0] + personal_data[1]
        passwords.add(combined)
        passwords.add(combined[::-1])  # Reverse
        passwords.add(combined + "2024")
    
    return passwords

def generate_random_passwords(num_passwords):
    common_passwords = [
        "password", "123456", "123456789", "qwerty", "abc123",
        "letmein", "welcome", "monkey", "iloveyou", "admin"
    ]
    
    random_passwords = []
    
    for _ in range(num_passwords):
        # Choose a random common password and add random numbers
        common_password = random.choice(common_passwords)
        random_number = ''.join(random.choices(string.digits, k=3))  # 3 random digits
        random_passwords.append(common_password + random_number)

    return random_passwords

def main():
    print_logo()
    
    print(lgreen + bold + "         <=== Personal Data Password Generator ===> " + clear)

    # Gather personal data for password list
    personal_data = []
    fields = [
        "Full name", "Date of birth (DDMMYYYY)", "Mobile No", "Birth Place",
        "Present Place", "Father's name", "Father's DOB (DDMMYYYY)", "Father's Mobile No",
        "Mother's name", "Mother's DOB (DDMMYYYY)", "Mother's Mobile No",
        "Spouse's name", "Spouse's DOB (DDMMYYYY)", "Spouse's Mobile No",
        "Child's name", "Child's DOB (DDMMYYYY)", "2nd Child's Name", 
        "2nd Child's DOB (DDMMYYYY)", "2nd Child's Mobile No", "Pet Name"
    ]
    
    for field in fields:
        value = input(yellow + f"Enter your {field}: " + clear)
        personal_data.append(value)

    # Generate passwords from personal data
    passwords = generate_passwords(personal_data)

    # Save personal password list to a file
    with open('personal_passwords.txt', 'w') as f:
        for password in passwords:
            f.write(password + '\n')

    print(cyan + bold + "Possible passwords from personal data have been saved to 'personal_passwords.txt'." + clear)

    # Generate random password list
    num_random_passwords = int(input(yellow + "How many random passwords do you want to generate? " + clear))
    random_passwords = generate_random_passwords(num_random_passwords)

    # Save random passwords to a file
    with open('random_passwords.txt', 'w') as f:
        for password in random_passwords:
            f.write(password + '\n')

    print(cyan + bold + f"Random passwords have been saved to 'random_passwords.txt'." + clear)

if __name__ == "__main__":
    main()
