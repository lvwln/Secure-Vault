# 🛡️ Secure Vault MFA API

A high-security Backend API built to demonstrate proficiency in **Identity & Access Management (IAM)** and **Functional Programming** constraints.

## 🚀 Overview
This project simulates a secure login flow using **TOTP (Time-based One-Time Password)** authentication. It was designed to align with the technical standards of the HENNGE Global Internship, specifically focusing on stateless logic and custom security protocols.

## ✨ Key Features
* **Custom TOTP Logic:** Implements the 10-digit SHA-512 TOTP variant.
* **Hacker Mindset (No-Loops):** All internal data searching and log processing are handled via **Recursion** to ensure side-effect-free code.
* **Secure Session Management:** Issues **JWT (JSON Web Tokens)** upon successful MFA verification.
* **Unix-Ready:** Developed and tested in a Unix-like environment.

## 🛠️ Architecture


## 💻 How to Use
1. **Clone the repo:** `git clone https://github.com/lvwln/Secure-Vault.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the server:** `python app.py`
4. **Test the Login:** Send a POST request to `/login` with your email and 10-digit OTP.

## 🎓 Academic Context
This project integrates concepts of **Big Data and Security** explored during my exchange program at **Woosong University, South Korea**, and mirrors the "No-Loop" challenge requirements set by HENNGE.
