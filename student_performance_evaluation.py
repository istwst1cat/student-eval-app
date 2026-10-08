import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ----------------- RELATIONAL DATABASE SYSTEM LAYER -----------------
class PerformanceDatabase:
    def __init__(self, db_name="performance_records.db"):
        """Initializes secure relational SQLite data architecture."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._build_infrastructure()

    def _build_infrastructure(self):
        """Constructs indexed system tables to prevent data loss threads."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS evaluations (
                record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                father_name TEXT NOT NULL,
                class_level TEXT NOT NULL,
                section_name TEXT NOT NULL,
                math_marks INTEGER NOT NULL,
                english_marks INTEGER NOT NULL,
                science_marks INTEGER NOT NULL,
                total_marks INTEGER NOT NULL,
                remarks TEXT,
                timestamp TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_record(self, name, father, cls, sec, math, eng, sci, total, remarks):
        """Streams sanitized academic vectors directly into permanent disk storage."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.cursor.execute("""
                INSERT INTO evaluations 
                (student_name, father_name, class_level, section_name, math_marks, english_marks, science_marks, total_marks, remarks, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (name.strip().title(), father.strip().title(), cls, sec, int(math), int(eng), int(sci), int(total), remarks.strip(), timestamp))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database Pipeline Fault: {e}")
            return False

# Initialize database globally
db = PerformanceDatabase()

# ----------------- USER INTERFACE ARCHITECTURE -----------------
root = tk.Tk()
root.title("Student Performance Evaluation")
root.geometry("900x650")
root.configure(bg="#d9e8ff")

# ===== HEADER =====
header = tk.Label(root, text="Student Performance Evaluation Form",
                  font=("Helvetica", 22, "bold"), bg="#d9e8ff")
header.pack(pady=20)

# ===== MAIN FRAME =====
main_frame = tk.Frame(root, bg="#d9e8ff")
main_frame.pack(pady=10)

def create_field(label_text, row):
    label = tk.Label(main_frame, text=label_text, bg="#d9e8ff",
                     font=("Arial", 12, "bold"))
    label.grid(row=row, column=0, padx=10, pady=8, sticky="w")

    entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry.grid(row=row, column=1, padx=10, pady=8)
    return entry

# ===== ENTRY CORE VALUES =====
name_entry = create_field("Student Name:", 0)
father_entry = create_field("Father's Name:", 1)

tk.Label(main_frame, text="Class:", bg="#d9e8ff",
         font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=8, sticky="w")

class_var = tk.StringVar()
class_dropdown = ttk.Combobox(main_frame, textvariable=class_var,
                              values=["6", "7", "8", "9", "10", "11", "12"],
                              font=("Arial", 12), width=28, state="readonly")
class_dropdown.grid(row=2, column=1, padx=10, pady=8)

tk.Label(main_frame, text="Section:", bg="#d9e8ff",
         font=("Arial", 12, "bold")).grid(row=3, column=0, padx=10, pady=8, sticky="w")

section_var = tk.StringVar()
section_dropdown = ttk.Combobox(main_frame, textvariable=section_var,
                                values=["A", "B"],
                                font=("Arial", 12), width=28, state="readonly")
section_dropdown.grid(row=3, column=1, padx=10, pady=8)

math_entry = create_field("Math Marks (0-100):", 4)
english_entry = create_field("English Marks (0-100):", 5)
science_entry = create_field("Science Marks (0-100):", 6)
total_entry = create_field("Expected Total Marks:", 7)

# ===== REMARKS PANELS =====
remarks_label = tk.Label(root, text="Teacher Remarks Evaluation:",
                         font=("Arial", 12, "bold"), bg="#d9e8ff")
remarks_label.pack()

remarks_box = tk.Text(root, height=4, width=80, font=("Arial", 12))
remarks_box.pack(pady=10)

# ===== STRUCTURAL DATA VALIDATION ENGINE =====
def validate():
    if not name_entry.get().strip() or not father_entry.get().strip():
        messagebox.showerror("Validation Failure", "Student identity cannot be left empty.")
        return False

    if not class_var.get() or not section_var.get():
        messagebox.showerror("Validation Failure", "Please select valid structural grid groupings (Class/Section).")
        return False

    # Numerical verification loop
    entries = {"Math": math_entry, "English": english_entry, "Science": science_entry, "Total": total_entry}
    vals = {}
    
    for name, entry in entries.items():
        val_str = entry.get().strip()
        if not val_str.isdigit():
            messagebox.showerror("Validation Failure", f"{name} parameters must consist strictly of integer digits.")
            return False
        vals[name] = int(val_str)

    # Advanced logical safety boundaries checks
    for key in ["Math", "English", "Science"]:
        if vals[key] < 0 or vals[key] > 100:
            messagebox.showerror("Logical Matrix Fault", f"{key} marks must settle within limits (0-100).")
            return False

    computed_sum = vals["Math"] + vals["English"] + vals["Science"]
    if vals["Total"] != computed_sum:
        messagebox.showerror("Mathematical Disconnect", f"Reported total ({vals['Total']}) does not balance with actual sum ({computed_sum}).")
        return False

    return True

# ===== OPERATIONS PIPELINE LOGIC =====
def submit():
    if validate():
        success = db.insert_record(
            name_entry.get(),
            father_entry.get(),
            class_var.get(),
            section_var.get(),
            math_entry.get(),
            english_entry.get(),
            science_entry.get(),
            total_entry.get(),
            remarks_box.get("1.0", tk.END)
        )
        
        if success:
            messagebox.showinfo("Persistence Confirmed", "Data successfully committed to SQLite storage!")
            clear()
        else:
            messagebox.showerror("System Failure", "Please review the information and try again.")

def clear():
    name_entry.delete(0, tk.END)
    father_entry.delete(0, tk.END)
    class_var.set("")
    section_var.set("")
    for entry in [math_entry, english_entry, science_entry, total_entry]:
        entry.delete(0, tk.END)
    remarks_box.delete("1.0", tk.END)

# ===== BUTTON INTERACTION MATRIX =====
button_frame = tk.Frame(root, bg="#d9e8ff")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Submit Record", font=("Helvetica", 11, "bold"),
          width=15, bg="#4CAF50", fg="white", command=submit).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Clear", font=("Helvetica", 11, "bold"),
          width=15, command=clear).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Terminate", font=("Helvetica", 11, "bold"),
          width=15, bg="#F44336", fg="white", command=root.destroy).grid(row=0, column=2, padx=10)

root.mainloop()