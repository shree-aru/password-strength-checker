
import re
from nltk.corpus import wordnet

def analyze_password_strength(password):
    strength = 0
    feedback = []

    # Criteria 1: Length
    if len(password) < 8:
        feedback.append("Password is too short (min 8 characters).")
    elif len(password) < 12:
        strength += 1
        feedback.append("Password length is good, but could be longer.")
    else:
        strength += 2
        feedback.append("Password length is excellent.")

    # Criteria 2: Character types
    has_lower = re.search(r'[a-z]', password)
    has_upper = re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?\"{}|<>]', password)

    char_types = 0
    if has_lower: char_types += 1
    if has_upper: char_types += 1
    if has_digit: char_types += 1
    if has_special: char_types += 1

    if char_types < 3:
        feedback.append("Use a mix of uppercase, lowercase, numbers, and special characters.")
    else:
        strength += char_types
        feedback.append(f"Uses {char_types} types of characters.")

    # Criteria 3: Common patterns (simple examples)
    if re.search(r'(123|abc|password|qwerty)', password, re.IGNORECASE):
        strength -= 2
        feedback.append("Avoid common patterns like '123', 'abc', or 'password'.")

    # Criteria 3.5: Repeated characters
    if re.search(r'(.)\1{2,}', password):
        strength -= 2
        feedback.append("Avoid repeated characters (e.g., 'aaa', '111').")

    # Criteria 4: Dictionary word detection (using NLTK WordNet)
    is_dictionary_word = False
    for word in password.split():
        if wordnet.synsets(word.lower()):
            is_dictionary_word = True
            break
    if is_dictionary_word:
        strength -= 3
        feedback.append("Avoid using common dictionary words.")

    # Determine overall strength
    if strength < 3:
        overall_strength = "Very Weak"
    elif strength < 6:
        overall_strength = "Weak"
    elif strength < 9:
        overall_strength = "Moderate"
    elif strength < 12:
        overall_strength = "Strong"
    else:
        overall_strength = "Very Strong"

    return overall_strength, feedback



