import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Custom styling configuration
COLORS = {
    "primary": "#2c3e50",
    "secondary": "#3498db",
    "background": "#ecf0f1",
    "text": "#2c3e50"
}

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        
        self.login_win = tk.Toplevel(self.root)
        self.login_win.title("Student Portal Login")
        self.login_win.geometry("350x200")
        self.login_win.configure(bg=COLORS["background"])
        
        self.valid_username = "admin"
        self.valid_password = "password123"
        
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        main_frame = ttk.Frame(self.login_win)
        main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="🔒 Student Portal", 
                font=('Helvetica', 14, 'bold'), 
                foreground=COLORS["primary"]).pack(pady=10)

        ttk.Label(main_frame, text="Username:").pack(pady=5)
        self.username_entry = ttk.Entry(main_frame)
        self.username_entry.pack(pady=5)

        ttk.Label(main_frame, text="Password:").pack(pady=5)
        self.password_entry = ttk.Entry(main_frame, show="•")
        self.password_entry.pack(pady=5)

        login_btn = ttk.Button(main_frame, text="Login", 
                             command=self.validate_login,
                             style="Primary.TButton")
        login_btn.pack(pady=10)

        # Configure styles
        style = ttk.Style()
        style.configure("Primary.TButton", 
                      foreground="white", 
                      background=COLORS["secondary"],
                      font=('Helvetica', 10))

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == self.valid_username and password == self.valid_password:
            self.login_win.destroy()
            self.root.destroy()
            MainApplication()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
            self.password_entry.delete(0, tk.END)

class MainApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management System")
        self.root.geometry("800x600")
        self.root.configure(bg=COLORS["background"])
        
        self.configure_styles()
        self.create_dashboard()
        self.root.mainloop()

    def configure_styles(self):
        style = ttk.Style()
        style.configure("Card.TFrame", background="white")
        style.configure("Feature.TButton", 
                      font=('Helvetica', 12),
                      padding=10,
                      width=20)
        
    def create_dashboard(self):
        header = ttk.Frame(self.root, style="Card.TFrame")
        header.pack(fill=tk.X, padx=20, pady=20)
        ttk.Label(header, text="🎓 Student Dashboard", 
                font=('Helvetica', 18, 'bold'),
                foreground=COLORS["primary"]).pack(pady=10)

        # Feature buttons
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=50)
        
        features = [
            ("📊 Grade Calculator", self.open_grade_calculator),
            ("📝 Student Notes", self.open_notes),
            ("🧮 Basic Calculator", self.open_calculator)
        ]
        
        for text, command in features:
            btn = ttk.Button(btn_frame, text=text, 
                           command=command,
                           style="Feature.TButton")
            btn.pack(pady=15)

    def open_grade_calculator(self):
        GradeCalculator()
        
    def open_notes(self):
        NotesWindow()
        
    def open_calculator(self):
        BasicCalculator()

class GradeCalculator(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Grade Calculator")
        self.geometry("500x400")
        self.subjects = ["Math", "Science", "English", "History", "Computer Science"]
        self.entries = []
        
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        ttk.Label(main_frame, text="📚 Enter Marks (0-100)", 
                font=('Helvetica', 14)).pack(pady=10)

        # Subject entries
        for idx, subject in enumerate(self.subjects):
            row_frame = ttk.Frame(main_frame)
            row_frame.pack(fill=tk.X, pady=5)
            
            ttk.Label(row_frame, text=f"{subject}:", width=15).pack(side=tk.LEFT)
            entry = ttk.Entry(row_frame)
            entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
            self.entries.append(entry)

        # Calculate button
        ttk.Button(main_frame, text="Calculate Grades", 
                 command=self.calculate,
                 style="Primary.TButton").pack(pady=20)
        
        # Result display
        self.result_frame = ttk.Frame(main_frame, style="Card.TFrame")
        self.result_frame.pack(fill=tk.X, pady=10)
        
        self.total_label = ttk.Label(self.result_frame, text="Total: ")
        self.total_label.pack(pady=5)
        
        self.percentage_label = ttk.Label(self.result_frame, text="Percentage: ")
        self.percentage_label.pack(pady=5)
        
        self.grade_label = ttk.Label(self.result_frame, text="Grade: ", 
                                   font=('Helvetica', 12, 'bold'))
        self.grade_label.pack(pady=5)

    def calculate(self):
        try:
            marks = [float(entry.get()) for entry in self.entries]
            if any(mark < 0 or mark > 100 for mark in marks):
                raise ValueError("All marks must be between 0-100")
            
            total = sum(marks)
            percentage = (total / 500) * 100
            
            grade = "A+" if percentage >= 90 else \
                    "A" if percentage >= 80 else \
                    "B" if percentage >= 70 else \
                    "C" if percentage >= 60 else \
                    "D" if percentage >= 50 else "F"
            
            self.total_label.config(text=f"Total: {total}/500")
            self.percentage_label.config(text=f"Percentage: {percentage:.2f}%")
            self.grade_label.config(text=f"Grade: {grade}", foreground=self.get_grade_color(grade))
            
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def get_grade_color(self, grade):
        colors = {
            "A+": "#27ae60",
            "A": "#2ecc71",
            "B": "#f1c40f",
            "C": "#e67e22",
            "D": "#e74c3c",
            "F": "#c0392b"
        }
        return colors.get(grade, COLORS["text"])

class NotesWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Student Notes")
        self.geometry("600x500")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.text_area = tk.Text(main_frame, wrap=tk.WORD, font=('Helvetica', 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="💾 Save", 
                 command=self.save_file,
                 style="Primary.TButton").pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame, text="📂 Open", 
                 command=self.open_file,
                 style="Primary.TButton").pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame, text="🧹 Clear", 
                 command=self.clear_text,
                 style="Danger.TButton").pack(side=tk.LEFT, padx=5)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get("1.0", tk.END))
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file:\n{str(e)}")

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

class BasicCalculator(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Input fields
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        self.num1_entry = ttk.Entry(input_frame)
        self.num1_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        self.operator = ttk.Combobox(input_frame, values=["+", "-", "×", "÷"], width=3)
        self.operator.pack(side=tk.LEFT, padx=5)
        self.operator.current(0)
        
        self.num2_entry = ttk.Entry(input_frame)
        self.num2_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        # Calculate button
        ttk.Button(main_frame, text="Calculate", 
                 command=self.calculate,
                 style="Primary.TButton").pack(pady=10)
        
        # Result display
        self.result_label = ttk.Label(main_frame, text="Result: ", 
                                    font=('Helvetica', 14))
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            op = self.operator.get()
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "×":
                result = num1 * num2
            elif op == "÷":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = num1 / num2
            
            self.result_label.config(text=f"Result: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    LoginWindow()