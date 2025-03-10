# 🔑 Username and Password Validator
This Python script validates usernames and passwords based on specific criteria (such as length, character types, and restrictions) and provides a function to generate secure passwords that meet all requirements.
<br><br>

## Python Script
Please view the Python script 🔗[here](Username-Password-Validator.py).
<br><br>

## Context
This project was developed as part of a Python course, focusing on building a system for validating usernames and passwords with secure standards. The objective was to ensure that usernames and passwords meet common security requirements, preventing weak credentials. The username validation function checks factors such as length, character variety (uppercase, lowercase, and digits), and ensures the username does not start or end with a digit. Similarly, the password validation function enforces rules for length, inclusion of uppercase and lowercase letters, digits, and special characters. To aid users who struggle to meet these criteria, the system also includes a password generator feature. This project highlights the application of Python in building functional programs, reinforcing concepts like string manipulation, conditional statements, and user input validation.

<sup><sub>Word Count: 124 words</sub></sup>
<br><br>

## Analysis and Results
The username and password validation functions effectively met the security requirements outlined. The username validation checks for length, character variety (uppercase, lowercase, digits), alphanumeric characters, and restrictions on starting/ending with digits. The function accurately flagged invalid usernames, considering the username requirements. The password validation function ensured passwords were at least 8 characters long, contained uppercase and lowercase letters, digits, and special characters. It also prevented the inclusion of the username within the password. Additionally, the system offered an option to generate a random password if the user's input did not meet the requirements, helping users create secure passwords easily. However, there are improvements that could be made to the code: adding detailed prompts or error messages could  quickly identify which specific rule the user violated, making it easier for them to correct their input. For example, instead of a generic "Password is invalid," the code could return "Password must contain at least one special character" to provide clearer guidance.

<sup><sub>Word Count: 160 words</sub></sup>
<br><br>

## Output
![Username and Password Validator Output](Username-Password-Validator-Output.png)
<br><br>

## Language Used
- **Python**
