# Student Performance Evaluation Architecture

An independent desktop environment engineered from the ground up to synthesize academic data entry with localized relational storage. Built entirely within native Python frameworks, this utility couples a structured Graphical User Interface (GUI) with precise evaluation safeguards to guarantee data integrity prior to disk persistence.

I designed and developed this repository independently to serve as an empirical showcase of transactional logic, interface engineering, and relational database administration.

## Technical Implementations

* **Isolated Persistence Layer:** Programmatically maps unstructured runtime inputs directly to a local SQLite backend engine (`performance_records.db`), ensuring reliable data preservation.
* **Deterministic Input Guards:** Enforces strict execution loops that constrain numerical grades to valid academic boundaries (0–100) before any write operation occurs.
* **Mathematical Synthesis Check:** Evaluates individual subject matrices in the background, validating that the computed sum corresponds perfectly with manual totals to block anomalous entries.
* **String Standardization Filters:** Leverages integrated sanitization routines to eliminate trailing whitespace and enforce standard title-casing across database records.

## System Dependencies & Architecture

To maintain a zero-dependency deployment footprint, the application relies exclusively on native Python standard libraries:

* **tkinter** - Compiles the functional windows, interactive dropdown menus, and layout grids.
* **sqlite3** - Manages the underlying relational query execution and disk indexing channels.
* **datetime** - Captures localized chronological timestamps for audit trails.

## Local Deployment & Execution

1. Navigate directly to the repository project directory via your terminal interface:
   ```bash
   cd path/to/your/student-eval-app
   ```

2. Execute the script runtime layout natively:
   ```bash
   python student_performance_evaluation.py
   ```
