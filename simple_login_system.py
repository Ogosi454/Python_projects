# Simple log in system (ask for username and password)
#
# Behavior: the user is allowed up to MAX_ATTEMPTS (3) attempts to log in.
# The script prompts again on incorrect username/password and exits with
# a final "access denied" message after the maximum attempts.
correct_username = "harry"
correct_password = "harry254"

# Allow the user up to 3 attempts before terminating
MAX_ATTEMPTS = 3

for attempt in range(1, MAX_ATTEMPTS + 1):
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == correct_username and password == correct_password:
        print("Login successful. Enjoy our services.")
        break

    # incorrect credentials
    if attempt < MAX_ATTEMPTS:
        print(f"Incorrect username or password — try again ({MAX_ATTEMPTS-attempt} attempts left)")
    else:
        print("Incorrect username or password. Maximum attempts reached — access denied.")
