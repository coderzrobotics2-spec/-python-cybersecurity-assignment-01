password = input("Enter password: ")
password_length = len(password)

if password_length < 8:
    password_strength = "WEAK"
elif password_length < 12:
    password_strength = "MODERATE"
else:
    password_strength = "STRONG"

print(password_strength)