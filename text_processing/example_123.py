import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Python String Methods Explorer")
root.geometry("600x600")

# Function to display results of each string method
def apply_string_method(method_name):
    input_text = input_text_var.get()
    result = ""

    try:
        if method_name == "Uppercase":
            result = input_text.upper()
        elif method_name == "Lowercase":
            result = input_text.lower()
        elif method_name == "Title Case":
            result = input_text.title()
        elif method_name == "Strip Whitespace":
            result = input_text.strip()
        elif method_name == "Replace 'a' with '@'":
            result = input_text.replace("a", "@")
        elif method_name == "Check if Alphanumeric":
            result = str(input_text.isalnum())
        elif method_name == "Reverse String":
            result = input_text[::-1]
        elif method_name == "Split by Spaces":
            result = input_text.split()
        elif method_name == "Count 'a'":
            result = str(input_text.count("a"))
        elif method_name == "Find 'hello'":
            result = str(input_text.find("hello"))
        elif method_name == "Convert to List of Words":
            result = list(input_text)
        elif method_name == "Is Title Case?":
            result = str(input_text.istitle())
        else:
            result = "Unknown method selected."

        result_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Variables to hold input and result
input_text_var = tk.StringVar()
result_var = tk.StringVar()

# Entry to accept user input text
tk.Label(root, text="Enter text:").pack(pady=5)
input_entry = tk.Entry(root, textvariable=input_text_var, width=50)
input_entry.pack(pady=5)

# Label to display results
tk.Label(root, text="Result:").pack(pady=5)
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="red")
result_label.pack(pady=5)

# List of string methods to showcase
string_methods = [
    "Uppercase", "Lowercase", "Title Case", "Strip Whitespace",
    "Replace 'a' with '@'", "Check if Alphanumeric", "Reverse String",
    "Split by Spaces", "Count 'a'", "Find 'hello'", "Convert to List of Words", "Is Title Case?"
]

# Create a button for each string method
for method in string_methods:
    btn = ttk.Button(root, text=method, command=lambda m=method: apply_string_method(m))
    btn.pack(fill='x', padx=10, pady=2)

# Exit button at the bottom
exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

# Start the application
root.mainloop()