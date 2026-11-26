# CyberGuard v1.0

**Personal Security Monitoring System**

CyberGuard is a beginner-level Python program that plays the role of a junior cybersecurity analyst's first tool. It collects basic account information, checks the account's status and password strength, assesses the login attempts, evaluate it to a threat level and prints a security report that changes depending on the information entered.

This is a simple educational project. It is not a real security tool.

Features

1. Welcome Text
2. User information collection: asks for username, email, password, age, IP address and account status (Active or Inactive), and converts each answer to the right data type and stores them as variables.
3. Security threat detection: sets a threat level from the account status and the number of failed login attempts. Results may vary depending on the combination

   | Condition                          | Result |
   | Account is inactive                | Account Inactive 
   | 1 to 4 failed login attempts       | Low Security Alert
   | 5 or more failed login attempts    | Critical warning: Possible brute-force attack 
   | Active account, no failed attempts | Low threat, no action required 

4. Password strength checker: Checks the password length and accessess its strength

   | Length                  | Rating   |
   | Fewer than 8 characters | WEAK     |
   | 8 to 11 characters      | MODERATE |
   | 12 or more characters   | STRONG   |

5. Security analyst report: prints user information, security analysis, threat detection, the final threat level and a recommendation. The actual password is never shown in the report.
6. Login process: asks the user to log in with the username and password they registered. Wrong credentials print a specific message ("Wrong Username", "Wrong Password" or both) and add one to the failed login attempts counter. A correct login prints "Login Successful" followed by the full security report.(An extra process I decided to through in also add a stoke to every falied attempt)


## How to Run

1. Clone or download this repository.
2. Open file in vscode
3. Open a terminal in the project folder.
4. Run:
   python user_security_system.py

5. Follow the prompts. Use a **sample password only**, never a real one.

