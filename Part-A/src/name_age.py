"""TODO: Replace with a one-line summary of the program's purpose (<73 chars).

Input:
    User's name as a string entered.
    User's age as an integer entered.

Process:
    Subtract the user's age from the current year for the birth.

Output:
    The string displaying the user's name and birth year on the screen.

Typical usage example:
                     What is your name? Alex
                     How old are you? 24
                     Hello Alex! You were born in 2002.

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input
name = input("What is your name? ")
age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
