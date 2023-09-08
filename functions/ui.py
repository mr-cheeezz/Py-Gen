import tkinter as tk
import pyperclip

def create_ui():
    root = tk.Tk()
    root.title("Password/PIN Generator")

    # Define colors using the provided CSS colors
    BACKGROUND_COLOR = "#232425"
    BACKGROUND_SECONDARY_COLOR = "#3b3d42"
    HEADER_COLOR = "#1b1c1d"
    TEXT_COLOR = "#a9a9b3"
    COLOR_SECONDARY = "#73747b"
    BORDER_COLOR = "#4a4b50"
    BOLD_COLOR = "#fff"

    # Function to generate a password
    def generate_password():
        length = int(length_entry.get())
        password_in_chrs = ''.join(secrets.choice(chrs) for _ in range(length))
        password_output.config(text=password_in_chrs)
        # Set the generated password to the clipboard
        pyperclip.copy(password_in_chrs)

    # Function to generate a PIN
    def generate_pin():
        length = int(length_entry.get())
        password_in_nmbrs = ''.join(secrets.choice(nmbrs) for _ in range(length))
        password_output.config(text=password_in_nmbrs)
        # Set the generated PIN to the clipboard
        pyperclip.copy(password_in_nmbrs)

    # Create the main window
    root.configure(bg=BACKGROUND_COLOR)

    # Create a label and entry for password length
    length_label = tk.Label(root, text="Enter Length:", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, padx=10, pady=5)
    length_label.pack()
    length_entry = tk.Entry(root)
    length_entry.pack()

    # Create buttons for generating password and PIN with custom styling
    button_style = {
        "fg": BOLD_COLOR,
        "bg": COLOR_SECONDARY,
        "borderwidth": 0,
        "highlightthickness": 0,
        "relief": "flat",
        "padx": 15,
        "pady": 5,
        "font": ("Helvetica", 12)
    }

    password_button = tk.Button(root, text="Generate Password", command=generate_password, **button_style)
    password_button.pack(pady=5)
    pin_button = tk.Button(root, text="Generate PIN", command=generate_pin, **button_style)
    pin_button.pack(pady=5)

    # Create a label to display the generated password/PIN
    password_output = tk.Label(root, text="", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, padx=10, pady=5, font=("Helvetica", 14))
    password_output.pack()

    # Create a "Copy" button with custom styling
    copy_button_style = {
        "fg": BOLD_COLOR,
        "bg": COLOR_SECONDARY,
        "borderwidth": 0,
        "highlightthickness": 0,
        "relief": "flat",
        "padx": 15,
        "pady": 5,
        "font": ("Helvetica", 12)
    }

    copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: pyperclip.copy(password_output.cget("text")), **copy_button_style)
    copy_button.pack(pady=10)

    # Start the Tkinter main loop
    root.mainloop()
