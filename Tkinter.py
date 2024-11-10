import customtkinter as ctk
from tkinter import messagebox

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key_length = len(key)
    key_nums = [ord(k) - ord('A') for k in key]  # Key converted to numbers
    text_nums = [ord(c) - ord('A') for c in text if c.isalpha()]  # Text converted to numbers

    for i, num in enumerate(text_nums):
        key_shift = key_nums[i % key_length]  # Cyclically use key characters
        
        if mode == 'encrypt':
            new_num = (num + key_shift) % 26  # Modular addition
        elif mode == 'decrypt':
            new_num = (num - key_shift + 26) % 26  # Modular subtraction
        
        result.append(chr(new_num + ord('A')))  # Convert back to letter
    
    # Combine the result, preserving non-alphabet characters (spaces, punctuation)
    final_result = []
    non_alpha_index = 0
    for c in text:
        if c.isalpha():
            final_result.append(result[non_alpha_index])
            non_alpha_index += 1
        else:
            final_result.append(c)
    
    return ''.join(final_result)

# Define functions for the GUI

def encrypt_message():
    message = message_entry.get().upper()
    key = key_entry.get().upper()
    
    if not message or not key:
        messagebox.showwarning("Input Error", "Please provide both message and key.")
        return
    
    encrypted_message = vigenere_cipher(message, key, mode='encrypt')
    result_label.configure(text=f"Encrypted message: {encrypted_message}")

def decrypt_message():
    message = message_entry.get().upper()
    key = key_entry.get().upper()
    
    if not message or not key:
        messagebox.showwarning("Input Error", "Please provide both message and key.")
        return
    
    decrypted_message = vigenere_cipher(message, key, mode='decrypt')
    result_label.configure(text=f"Decrypted message: {decrypted_message}")

def reset_fields():
    message_entry.delete(0, ctk.END)
    key_entry.delete(0, ctk.END)
    result_label.configure(text="Result will appear here")

# Create the main app window
app = ctk.CTk()
app.title("Vigenère Cipher Program")
app.geometry("500x400")

# UI Components
title_label = ctk.CTkLabel(app, text="Vigenère Cipher", font=("Arial", 24))
title_label.pack(pady=10)

message_label = ctk.CTkLabel(app, text="Enter your message:")
message_label.pack(pady=5)
message_entry = ctk.CTkEntry(app, width=300)
message_entry.pack(pady=5)

key_label = ctk.CTkLabel(app, text="Enter the key:")
key_label.pack(pady=5)
key_entry = ctk.CTkEntry(app, width=300)
key_entry.pack(pady=5)

# Buttons for Encrypt/Decrypt
encrypt_button = ctk.CTkButton(app, text="Encrypt", command=encrypt_message)
encrypt_button.pack(pady=10)

decrypt_button = ctk.CTkButton(app, text="Decrypt", command=decrypt_message)
decrypt_button.pack(pady=10)

# Reset button
reset_button = ctk.CTkButton(app, text="Reset", command=reset_fields)
reset_button.pack(pady=10)

# Result label
result_label = ctk.CTkLabel(app, text="Result will appear here", font=("Arial", 14))
result_label.pack(pady=20)

# Run the app
app.mainloop()
