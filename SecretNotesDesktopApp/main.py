import base64
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# --- Functions ---

def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) + ord(key_c)) % 256)
        encoded_chars.append(encoded_c)

    encoded_string = "".join(encoded_chars)
    base64_bytes = base64.urlsafe_b64encode(encoded_string.encode("latin-1"))
    return base64_bytes.decode("utf-8")


def decode(key, encoded_string):
    encoded_string = encoded_string.strip()
    if not encoded_string:
        return ""

    missing_padding = len(encoded_string) % 4
    if missing_padding:
        encoded_string += "=" * (4 - missing_padding)

    try:
        decoded_bytes = base64.urlsafe_b64decode(encoded_string.encode("utf-8"))
        decoded_string = decoded_bytes.decode("latin-1")
    except Exception:
        messagebox.showerror("Error", "Invalid encrypted string format!")
        return ""

    decoded_chars = []
    for i in range(len(decoded_string)):
        key_c = key[i % len(key)]
        decoded_c = chr((ord(decoded_string[i]) - ord(key_c)) % 256)
        decoded_chars.append(decoded_c)

    return "".join(decoded_chars)


def write_into_text(title, message):
    try:
        with open("Message.txt", "a", encoding="utf-8") as file:
            file.write(title.strip() + "\n")
            file.write(message.strip() + "\n")
    except IOError:
        messagebox.showerror("Error", "Message File Not Found")


def get_from_file_with_title(key, message_title):
    try:
        with open("Message.txt", "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

            for i in range(len(lines)):
                if lines[i] == message_title.strip():
                    if i + 1 < len(lines):
                        encrypted_message = lines[i + 1]
                        return decode(key, encrypted_message)

        messagebox.showerror("Error", "Message Not Found")
        return ""
    except FileNotFoundError:
        messagebox.showerror("Error", "Message File Not Found")
        return ""


def save_button_mission():
    key = master_key_input.get().strip()
    message = secret_message_input.get("1.0", "end-1c").strip()
    title = secret_title_input.get().strip()

    if key == "" or message == "" or title == "":
        messagebox.showerror("Error", "Please enter empty fields")
        return

    new_message = encode(key, message)
    write_into_text(title, new_message)

    # Kutuları temizle
    secret_title_input.delete(0, tk.END)
    master_key_input.delete(0, tk.END)
    secret_message_input.delete("1.0", tk.END)

    messagebox.showinfo("Success", "Message Saved Successfully")


def decrypt_button_mission():
    key = master_key_input.get().strip()
    message = secret_message_input.get("1.0", "end-1c").strip()
    title = secret_title_input.get().strip()

    if key == "":
        messagebox.showerror("Error", "Please enter your key")
        return

    result = ""
    # Eğer mesaj kutusu boşsa dosyadan başlığa göre ara
    if message == "" and title != "":
        result = get_from_file_with_title(key, title)
    # Eğer mesaj kutusunda şifreli metin varsa doğrudan onu çöz
    elif message != "":
        result = decode(key, message)

    if result:
        secret_message_input.delete("1.0", tk.END)
        secret_message_input.insert("1.0", result)


# --- GUI Configuration ---

window = tk.Tk()
window.title("Encryptor3000")
window.minsize(400, 600)
window.configure(background="lightblue")

# Secret Image
if os.path.exists("./logo.png"):
    img_ac = Image.open("./logo.png")
    img_resize = img_ac.resize((150, 100))
    img = ImageTk.PhotoImage(img_resize)
    panel = tk.Label(window, image=img, bg="lightblue")
    panel.pack()

# Label Title
title_label = tk.Label(font=("Courier", 10, "bold"), bg="lightblue", fg="black", text="Mesaj Basligini Giriniz..",
                       pady=10)
title_label.pack()

# Secret Title
secret_title_input = tk.Entry(width=30)
secret_title_input.pack()

# Label Mesaj
message_label = tk.Label(font=("Courier", 10, "bold"), fg="black", bg="lightblue", text="Mesajinizi Giriniz", pady=10)
message_label.pack()

# Secret Message Input Section
secret_message_input = tk.Text(height=10, width=30)
secret_message_input.pack()

# Key Label
key_label = tk.Label(font=("Courier", 10, "bold"), fg="black", bg="lightblue", text="Master Keyinizi Tuslayiniz",
                     pady=10)
key_label.pack()

# Key input
master_key_input = tk.Entry(width=30)
master_key_input.pack(pady=10)

# Save And Encrypt Button
save_button = tk.Button(command=save_button_mission, text="Save and Encrypt", width=20, height=1, fg="black",
                        bg="white", activebackground="black", activeforeground="white")
save_button.pack()

# Decrypt Button
decrypt_button = tk.Button(command=decrypt_button_mission, text="Decrypt", width=20, height=1, fg="black", bg="white",
                           activebackground="black", activeforeground="white")
decrypt_button.pack(pady=10)

window.mainloop()