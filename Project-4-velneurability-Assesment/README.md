# DecodeLabs-Internship

# Project 4: Vulnerability Assessment & Penetration Testing (VAPT)

## Overview

This project focuses on testing the security of the OWASP Juice Shop web application. The application was tested in a safe lab environment to identify common security vulnerabilities and understand how attackers can exploit them.

---

## Objective

The main goal of this project is to:

- Learn web application security testing.
- Identify common security vulnerabilities.
- Understand how security tools are used.
- Suggest ways to improve application security.

---

## Tools Used

- Kali Linux
- OWASP Juice Shop
- Burp Suite Community Edition
- Browser Developer Tools

---

## Vulnerabilities Identified

### 1. SQL Injection
A SQL Injection attack was used to bypass the login page and gain unauthorized access.

### 2. Information Disclosure
Burp Suite was used to inspect HTTP traffic and identify server information exposed in HTTP headers.

### 3. FTP Directory Exposure
The `/ftp` directory was publicly accessible and allowed access to sensitive files.

---

## Recommendations

- Use parameterized SQL queries.
- Restrict access to sensitive directories.
- Hide unnecessary server information.
- Apply secure authentication and access controls.

---

## Project Structure

```
Project-4/
│── README.md
│── Report.pdf
└── Screenshots/
    ├── sql_injection.png
    ├── burp_suite.png
    └── ftp_directory.png
```

---

## Author

**Maryam Malik**
Cybersecurity Intern
DecodeLabs Internship
