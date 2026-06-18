"""
Password breach checker using the Have I Been Pwned API.
Uses k-anonymity model — only the first 5 chars of the SHA-1 hash are sent.
Your full password NEVER leaves your machine.
"""

import hashlib
import urllib.request

def check_password_breach(password):
    """Check if a password has been found in known data breaches."""
    # Step 1: SHA-1 hash the password
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # Step 2: Query the HIBP API with only the prefix (k-anonymity)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "PasswordStrengthChecker"})
        response = urllib.request.urlopen(request)
        data = response.read().decode('utf-8')
    except Exception as e:
        return None, f"Error contacting breach database: {e}"

    # Step 3: Check if our suffix appears in the results
    for line in data.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count), None

    return 0, None

def format_breach_result(password):
    """Check and display breach results in a user-friendly format."""
    count, error = check_password_breach(password)
    
    if error:
        print(f"⚠️  {error}")
        return
    
    if count == 0:
        print("✅ Great news! This password has NOT been found in any known data breaches.")
    else:
        print(f"🚨 WARNING: This password has been found in {count:,} data breach(es)!")
        print("   You should change this password immediately.")

if __name__ == "__main__":
    print("=== Password Breach Checker ===")
    print("(Your password is hashed locally and never sent in full)\n")
    
    pw = input("Enter a password to check: ")
    format_breach_result(pw)
