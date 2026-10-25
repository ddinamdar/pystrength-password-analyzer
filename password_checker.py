import re
import string


def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$...)")

    common_passwords = [
        "password", "123456", "password123", "admin",
        "letmein", "qwerty", "abc123", "iloveyou"
    ]
    if password.lower() in common_passwords:
        score = 0
        feedback = ["This is a commonly used password — change it immediately"]

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MODERATE"
    elif score == 5:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return strength, score, feedback


def main():
    print("=" * 45)
    print("   Password Strength Analyzer — PyStrength")
    print("        Mohammed Danish Inamdar")
    print("=" * 45)

    while True:
        password = input("\nEnter password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Exiting. Stay secure.")
            break

        strength, score, feedback = check_strength(password)

        print(f"\nStrength : {strength}")
        print(f"Score    : {score}/6")

        if feedback:
            print("\nSuggestions:")
            for tip in feedback:
                print(f"  → {tip}")
        else:
            print("\n✓ Password looks strong!")

        print("-" * 45)


if __name__ == "__main__":
    main()