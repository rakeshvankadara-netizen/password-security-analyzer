import tkinter as tk


COMMON_PASSWORDS = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "admin"
]


def analyze_password():
    password = password_entry.get()

    is_common = password.lower() in COMMON_PASSWORDS
    numbers_only = password.isdigit()
    repeated = len(password) > 0 and len(set(password)) == 1

    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    number = any(char.isdigit() for char in password)
    special = any(not char.isalnum() for char in password)

    score = 0
    missing = []

    if length >= 12:
        score += 1

    if is_common:
        result_label.config(
            text="Password Score: 0/6\n"
                 "Strength: WEAK\n"
                 "Warning: This is a common password"
        )
        return

    if repeated:
        result_label.config(
            text="Password Score: 0/6\n"
                 "Strength: WEAK\n"
                 "Warning: Same character is repeated"
        )
        return

    if numbers_only:
        result_label.config(
            text="Password Score: 0/6\n"
                 "Strength: WEAK\n"
                 "Warning: Password contains only numbers"
        )
        return

    if length >= 8:
        score += 1
    else:
        missing.append("8 characters or more")

    if uppercase:
        score += 1
    else:
        missing.append("uppercase letter")

    if lowercase:
        score += 1
    else:
        missing.append("lowercase letter")

    if number:
        score += 1
    else:
        missing.append("number")

    if special:
        score += 1
    else:
        missing.append("special character")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    if missing:
        missing_text = "Missing: " + ", ".join(missing)
    else:
        missing_text = "All basic requirements met"

    if is_common:
        common_text = "Warning: This is a common password"
    else:
        common_text = ""

    result_label.config(
        text=f"Password Score: {score}/6\n"
             f"Strength: {strength}\n"
             f"{missing_text}\n"
             f"{common_text}"
    )


def clear_password():
    password_entry.delete(0, tk.END)
    result_label.config(
        text="Enter a password and click Analyze"
    )


window = tk.Tk()

window.title("Password Security Analyzer")
window.geometry("500x450")

title = tk.Label(
    window,
    text="PASSWORD SECURITY ANALYZER",
    font=("Arial", 18, "bold")
)

title.pack(pady=30)

password_label = tk.Label(
    window,
    text="Enter Password:",
    font=("Arial", 14)
)

password_label.pack(pady=10)

password_entry = tk.Entry(
    window,
    show="*",
    font=("Arial", 14),
    width=25
)

password_entry.pack(pady=10)

show_password = tk.BooleanVar()


def toggle_password():
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


show_button = tk.Checkbutton(
    window,
    text="Show Password",
    variable=show_password,
    command=toggle_password
)

show_button.pack()

analyze_button = tk.Button(
    window,
    text="ANALYZE PASSWORD",
    font=("Arial", 14),
    command=analyze_password
)

analyze_button.pack(pady=20)

clear_button = tk.Button(
    window,
    text="CLEAR",
    font=("Arial", 12),
    command=clear_password
)

clear_button.pack(pady=5)

result_label = tk.Label(
    window,
    text="Enter a password and click Analyze",
    font=("Arial", 12)
)

result_label.pack(pady=10)

window.mainloop()