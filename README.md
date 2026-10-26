# Student Performance Evaluation Architecture

An independent desktop app programmed to combine academic data entry with localized relational storage. Built entirely within native Python frameworks, this program combines a structured Graphical User Interface (GUI) with precise evaluation safeguards to guarantee data integrity prior to disk persistence.

I designed and developed this repository independently to serve as a showcase of transactional logic, interface engineering, and relational database administration.

## Technical Implementations

* **Isolated Persistence Layer:** Programmatically maps unstructured runtime inputs directly to a local SQLite backend (`performance_records.db`), ensuring reliable data records.
* **Conditional Input Guards:** Enforces strict execution loops that constrain numerical grades to valid academic boundaries (0–100) before any write operation occurs.
* **Mathematical Checks:** Evaluates individual subject matrices in the background, validating that the computed sum corresponds perfectly with manual totals to block anomalous entries.
* **String Standardization Filters:** Uses integrated sanitization routines to eliminate trailing whitespace and enforce standard title-casing across database records.

## System Dependencies & Framework

The application relies exclusively on native Python standard libraries:

* **tkinter** - Provides the functional windows, interactive dropdown menus, and layout grids.
* **sqlite3** - Coordinates the underlying database connections and query operations to store structured student logs permanently on the disk.
* **datetime** - Allows for precise data-entry history within the performance_records.db file.

## Local Deployment & Execution

1. Navigate directly to the repository project directory via your terminal interface:
   ```bash
   cd path/to/your/student-eval-app
   ```

2. Execute the script runtime layout natively:
   ```bash
   python student_performance_evaluation.py
   ```
