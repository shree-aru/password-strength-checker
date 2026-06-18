import tkinter as tk
from tkinter import ttk, messagebox
from password_analyzer import analyze_password_strength

class PasswordAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("500x350")
        self.root.configure(padx=20, pady=20)

        # Title
        ttk.Label(root, text="Analyze Your Password", font=("Helvetica", 16, "bold")).pack(pady=(0, 20))

        # Input
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(root, textvariable=self.password_var, show="*", font=("Helvetica", 12), width=30)
        self.password_entry.pack(pady=10)

        # Show/Hide Checkbox
        self.show_password_var = tk.BooleanVar(value=False)
        self.show_password_cb = ttk.Checkbutton(root, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.show_password_cb.pack(pady=5)

        # Analyze Button
        self.analyze_btn = ttk.Button(root, text="Check Strength", command=self.check_strength)
        self.analyze_btn.pack(pady=15)

        # Result Labels
        self.strength_label = ttk.Label(root, text="Strength: --", font=("Helvetica", 14, "bold"))
        self.strength_label.pack(pady=5)

        self.feedback_text = tk.Text(root, height=5, width=50, state="disabled", wrap="word", bg=root.cget('bg'), relief="flat")
        self.feedback_text.pack(pady=10)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def check_strength(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Input Error", "Please enter a password.")
            return

        strength, feedback = analyze_password_strength(password)

        # Update strength label color based on result
        color_map = {
            "Very Weak": "red",
            "Weak": "orange",
            "Moderate": "#b5a300", # Dark yellow
            "Strong": "green",
            "Very Strong": "darkgreen"
        }
        self.strength_label.config(text=f"Strength: {strength}", foreground=color_map.get(strength, "black"))

        # Update feedback text
        self.feedback_text.config(state="normal")
        self.feedback_text.delete(1.0, tk.END)
        for item in feedback:
            self.feedback_text.insert(tk.END, f"- {item}\n")
        self.feedback_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordAnalyzerGUI(root)
    root.mainloop()
