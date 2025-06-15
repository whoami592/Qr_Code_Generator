import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import pyfiglet

# Display stylish ASCII banner in console
banner = pyfiglet.figlet_format("QR Code Generator")
print(banner)
print("Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan")
print("=" * 60)

# Initialize main window
root = tk.Tk()
root.title("QR Code Generator by Mr Sabaz Ali Khan")
root.geometry("600x600")
root.configure(bg="#1e1e2e")

# Styling variables
font_style = ("Arial", 12, "bold")
bg_color = "#1e1e2e"
fg_color = "#ffffff"
button_color = "#6200ea"
button_hover = "#3700b3"

# Function to generate QR code
def generate_qr():
    data = entry.get().strip()
    if not data:
        messagebox.showwarning("Input Error", "Please enter a URL or text!")
        return

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Resize for display
    qr_image = qr_image.resize((250, 250), Image.LANCZOS)
    qr_photo = ImageTk.PhotoImage(qr_image)

    # Update label with QR code
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo  # Keep reference to avoid garbage collection

    # Enable save button
    save_button.config(state="normal")

# Function to save QR code
def save_qr():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if file_path:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(entry.get().strip())
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved as {file_path}")

# GUI Elements
# Header Label
header = tk.Label(
    root,
    text="QR Code Generator",
    font=("Arial", 20, "bold"),
    bg=bg_color,
    fg="#bb86fc"
)
header.pack(pady=10)

# Credit Label
credit = tk.Label(
    root,
    text="Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan",
    font=("Arial", 10, "italic"),
    bg=bg_color,
    fg="#03dac6"
)
credit.pack()

# Input Frame
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(pady=20)

# Input Label and Entry
tk.Label(
    input_frame,
    text="Enter URL or Text:",
    font=font_style,
    bg=bg_color,
    fg=fg_color
).grid(row=0, column=0, padx=5)
entry = tk.Entry(input_frame, width=40, font=font_style, bg="#2c2c3e", fg=fg_color, insertbackground=fg_color)
entry.grid(row=0, column=1, padx=5)

# Generate Button
generate_button = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    font=font_style,
    bg=button_color,
    fg=fg_color,
    activebackground=button_hover,
    relief="flat",
    padx=10,
    pady=5
)
generate_button.pack(pady=10)

# QR Code Display Label
qr_label = tk.Label(root, bg=bg_color)
qr_label.pack(pady=10)

# Save Button (initially disabled)
save_button = tk.Button(
    root,
    text="Save QR Code",
    command=save_qr,
    font=font_style,
    bg=button_color,
    fg=fg_color,
    activebackground=button_hover,
    relief="flat",
    padx=10,
    pady=5,
    state="disabled"
)
save_button.pack(pady=10)

# Button hover effects
def on_enter(e, btn):
    btn['background'] = button_hover

def on_leave(e, btn):
    btn['background'] = button_color

generate_button.bind("<Enter>", lambda e: on_enter(e, generate_button))
generate_button.bind("<Leave>", lambda e: on_leave(e, generate_button))
save_button.bind("<Enter>", lambda e: on_enter(e, save_button))
save_button.bind("<Leave>", lambda e: on_leave(e, save_button))

# Start main loop
root.mainloop()