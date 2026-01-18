# Bank Management System 🏦

A versatile banking application built with **Python**, offering two different interfaces: a modern **Streamlit Web App** and a classic **Command Line Interface (CLI)**.

This project simulates a core banking environment where users can create accounts, manage funds, and view transaction details. It features a **modular architecture**, where the backend logic (`bank.py`) is reused across both the Web UI (`app.py`) and the CLI (`main.py`) to ensure clean code and "Separation of Concerns."

## 🚀 Key Features

* **Dual Interface:** Run the project as a Web App (Streamlit) or a Terminal Tool (CLI).
* **Account Management:** Create new bank accounts with unique, auto-generated account numbers.
* **Secure Transactions:**
    * **Deposit:** Add funds to your account instantly.
    * **Withdraw:** Secure withdrawals with balance validation checks.
* **Data Persistence:** Uses a JSON-based database (`data.json`) to store user records permanently, so data is not lost when the app closes.
* **Real-time Updates:** View account details and updated balances immediately after any transaction.
* **Security:** PIN validation system (supports PINs with leading zeros, e.g., "0701").
* **CRUD Operations:** Full capability to Create, Read (View), Update (Edit Info), and Delete accounts.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Web UI)
* **Backend:** Python 3.13.3 (Object-Oriented Programming)
* **Database:** JSON (Lightweight file-based storage)

## 📂 Project Structure

```text
Bank-Management-System/
│
├── app.py           # Option A: The Streamlit Web Interface
├── main.py          # Option B: The Command Line Interface (CLI)
├── bank.py          # Backend: Shared logic for both interfaces
├── data.json        # Database: Stores user account data (Auto-generated)
├── requirements.txt # List of dependencies
└── README.md        # Documentation
