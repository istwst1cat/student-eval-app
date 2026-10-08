# 🏫 Student Performance Evaluation Console
### *Independent Relational Database Application Portfolio Highlight*

A clean, desktop application built from scratch to streamline academic data entry and performance logging. This terminal features a structural Graphical User Interface (GUI), enforces strict boundary data validation logic, and implements permanent data storage through a native relational database layer.

Developed independently by **Issac Qaiser** as a cornerstone portfolio display for university.

---

## ✨Features✨

* **Relational Storage Layer:** Automatically maps data inputs to an isolated SQLite backend engine (`performance_records.db`), securing permanent data persistence on the local storage disk.
* **Data Integrity Validation:** Houses strict boundary math validation loops that ensure student grades settle precisely within valid academic limits (0-100).
* **Mathematical Balance Safeguards:** Automatically adds individual subject marks in the background to verify that the computed sum balances perfectly with the manual entry total, blocking anomalous or corrupted data entries.
* **Automated Data Cleaning:** Utilizes smart shortcuts to clear whitespace data, enforce standard title-casing format, and maintain standard database structure.

---

## 🔌 System Dependencies & Requirements

To launch this desktop application locally, your runtime environment only requires standard Python installations. The core libraries used are entirely native:

* **`tkinter`** - Compiles the functional windows, drop-down menus, and user interaction frames.
* **`sqlite3`** - Operates the localized SQL relational query strings and disk indexing logic.
* **`datetime`** - Automatically captures real-time data entry timestamps.
---

## 💻 Local Setup & Execution

1. **Navigate directly to the repository project folder via terminal or cmd:**
   ```bash
   cd path/to/your/student-eval-app
   ```

2. **Execute the script layout natively using Python:**
   ```bash
   python student_performance_form.py
   ```
   *The application will instantly launch a secure GUI evaluation window on your desktop screen.*
