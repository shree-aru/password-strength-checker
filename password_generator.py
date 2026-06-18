import random
import string

def generate_password(length=16, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a cryptographically strong random password."""
    if length < 8:
        print("Warning: Password length should be at least 8 characters. Setting to 8.")
        length = 8

    characters = string.ascii_lowercase
    required_chars = [random.choice(string.ascii_lowercase)]

    if use_uppercase:
        characters += string.ascii_uppercase
        required_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        characters += string.digits
        required_chars.append(random.choice(string.digits))
    if use_special:
        special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        characters += special
        required_chars.append(random.choice(special))

    # Fill remaining length with random characters
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [random.choice(characters) for _ in range(remaining_length)]
    
    # Shuffle to avoid predictable positions
    random.shuffle(password_chars)
    
    return "".join(password_chars)

def generate_multiple(count=5, length=16):
    """Generate multiple strong passwords."""
    passwords = []
    for _ in range(count):
        passwords.append(generate_password(length))
    return passwords

def generate_passphrase(word_count=4, separator="-"):
    """Generate a memorable passphrase using random words."""
    word_list = [
        "alpha", "brave", "cipher", "delta", "echo", "frost", "gamma", "hydra",
        "ionic", "joker", "karma", "lunar", "metro", "nexus", "orbit", "prism",
        "quark", "raven", "sigma", "titan", "ultra", "viper", "wrath", "xenon",
        "yacht", "zephyr", "blaze", "crest", "drift", "ember", "flare", "ghost",
        "haven", "ivory", "jewel", "knack", "lyric", "maple", "noble", "oasis",
        "pearl", "quest", "ridge", "storm", "thorn", "unity", "valor", "whirl"
    ]
    words = random.sample(word_list, word_count)
    # Add a random number for extra security
    words.append(str(random.randint(10, 99)))
    return separator.join(words)

if __name__ == "__main__":
    print("=== Password Generator ===\n")
    
    print("1. Generate Strong Password")
    print("2. Generate Multiple Passwords")
    print("3. Generate Passphrase")
    
    choice = input("\nChoose an option: ")
    
    if choice == "1":
        length = int(input("Enter desired length (min 8): "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    elif choice == "2":
        count = int(input("How many passwords? "))
        length = int(input("Enter desired length (min 8): "))
        passwords = generate_multiple(count, length)
        print("\nGenerated Passwords:")
        for i, pw in enumerate(passwords, 1):
            print(f"  {i}. {pw}")
    elif choice == "3":
        word_count = int(input("How many words? (3-6): "))
        passphrase = generate_passphrase(word_count)
        print(f"\nGenerated Passphrase: {passphrase}")
    else:
        print("Invalid option.")
