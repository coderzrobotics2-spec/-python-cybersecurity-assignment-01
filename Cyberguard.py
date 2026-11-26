tool_version = 1.0

print("========================================")
print("           CYBERGUARD v" + str(1.0)           )
print("     PERSONAL SECURITY MONITORING SYSTEM")
print("========================================")
print()
print("Welcome, Security Analyst!")
print()
print("Your mission is to monitor account information and identify potential threats.")
print("Starting security assessment...")
print()

username = input("Enter username: ")
email = input("Enter email address: ")
password = input("Enter password: ")
age = int(input("Enter age: "))
ip_address = input("Enter IP address: ")
failed_login_attempts = 0
account_status_answer = input("Is the account Active or Inactive? ")

if account_status_answer.lower() == "active":
    account_active = True
else:
    account_active = False



if account_active == False:
    threat_level = "ACCOUNT INACTIVE"
    recommendation_1 = "Verify and Reactivate the account if necessary."
    recommendation_2 = "re-enabling access."
elif failed_login_attempts >= 1 and failed_login_attempts <= 4:
    threat_level = "LOW"
    recommendation_1 = "Monitor the account for further failed attempts"
    recommendation_2 = "Send OTP verification to the user for added security."
elif failed_login_attempts >= 5:
    threat_level = "HIGH"
    recommendation_1 = "Investigate the login activity and secure the account immediately"
    recommendation_2 = "Change password and enable two-factor authentication."
else:
    threat_level = "LOW"
    recommendation_1 = "No action required. Continue routine monitoring"
    recommendation_2 = "Send OTP verification to the user for added security."

if threat_level == ("HIGH"):
    threat_level = "Critical warning: Possible brute-force attack"
elif threat_level == ("LOW"):
    threat_level = "Low Security Alert. Check Your Phone For OTP to continue Login Process"
else:
    threat_level = "Account Inactive"
    

#FEATURE 4 PASSWWORD
password_length = len(password)

if password_length < 8:
    password_strength = "WEAK"
elif password_length < 12:
    password_strength = "MODERATE"
else:
    password_strength = "STRONG"

print(password_strength)

#FEATURE 5 SECURITY ANALYST REPORT

print("========================================")
print("          CYBERGUARD SECURITY REPORT")
print("========================================")
print()
print("USER INFORMATION")
print("----------------------------------------")
print("Username: " + username)
print("Email: " + email)
print("Age: " + str(age))
print("IP Address: " + ip_address)
print("Account Status: " + account_status_answer)
print()
print("SECURITY ANALYSIS")
print("----------------------------------------")
print("Password Assessment: " + password_strength)
print("Failed Login Attempts: " + str(failed_login_attempts))
print()
print("THREAT DETECTION")
print("----------------------------------------")
print(threat_level)
print()
print("FINAL SECURITY STATUS")
print("----------------------------------------")
print("THREAT LEVEL: " + threat_level)
print()
print("RECOMMENDATION:")
print(recommendation_1)
print(recommendation_2)
if password_strength == "WEAK":
    print("Please Strengthen Your Password to Avoid Security Breaches")
print()
print("========================================")
print("          END OF SECURITY REPORT")
print("========================================")




print("----------------------------------------")
print("            Log In Process              ")
print("----------------------------------------")

username_1 = input("Enter Username ")
password_1 = input("Enter password: ")
if password != password_1 and username != username_1:
    print("Wrong Username and Password")
    failed_login_attempts += 1
elif password == password_1 and username != username_1:
    print("Wrong Username")
    failed_login_attempts += 1
elif password != password_1 and username == username_1:
    print("Wrong Password")
    failed_login_attempts += 1
else:
    print("Password & Username Accepted")
    print("Login Successful")
    print("========================================")
    print("          CYBERGUARD SECURITY REPORT")
    print("========================================")
    print()
    print("USER INFORMATION")
    print("----------------------------------------")
    print("Username: " + username)
    print("Email: " + email)
    print("Age: " + str(age))
    print("IP Address: " + ip_address)
    print("Account Status: " + account_status_answer)
    print()
    print("SECURITY ANALYSIS")
    print("----------------------------------------")
    print("Password Assessment: " + password_strength)
    print("Failed Login Attempts: " + str(failed_login_attempts))
    print()
    print("THREAT DETECTION")
    print("----------------------------------------")
    print(threat_level)
    print()
    print("FINAL SECURITY STATUS")
    print("----------------------------------------")
    print("THREAT LEVEL: " + threat_level)
    print()
    print("RECOMMENDATION:")
    print(recommendation_1)
    print(recommendation_2)
    if password_strength == "WEAK":
        print("Please Strengthen Your Password to Avoid Security Breaches")
    print()
    print("========================================")
    print("          END OF SECURITY REPORT")
    print("========================================")



