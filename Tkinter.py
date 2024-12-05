import tkinter
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Inisialisasi CustomTkinter
ctk.set_appearance_mode("light")  # Setel mode tampilan ke mode terang untuk latar belakang terang
ctk.set_default_color_theme("blue")  # Gunakan tema "blue" bawaan

def vigenere_cipher(teks, kunci, mode='encrypt'):
    hasil = []
    panjang_kunci = len(kunci)
    angka_kunci = [ord(k) - ord('A') for k in kunci]  # Kunci diubah menjadi angka
    angka_teks = [ord(c) - ord('A') for c in teks if c.isalpha()]  # Teks diubah menjadi angka

    for i, num in enumerate(angka_teks):
        pergeseran_kunci = angka_kunci[i % panjang_kunci]  # Gunakan karakter kunci secara siklik

        if mode == 'encrypt':
            angka_baru = (num + pergeseran_kunci) % 26  # Penambahan modular
        elif mode == 'decrypt':
            angka_baru = (num - pergeseran_kunci + 26) % 26  # Pengurangan modular

        hasil.append(chr(angka_baru + ord('A')))  # Kembalikan ke huruf

    # Gabungkan hasilnya, mempertahankan karakter non-alfabet (spasi, tanda baca)
    hasil_akhir = []
    indeks_non_alfabet = 0
    for c in teks:
        if c.isalpha():
            hasil_akhir.append(hasil[indeks_non_alfabet])
            indeks_non_alfabet += 1
        else:
            hasil_akhir.append(c)

    return ''.join(hasil_akhir)

# Definisikan fungsi untuk GUI
def encrypt_message():
    pesan = message_entry.get().upper()
    kunci = key_entry.get().upper()

    if not pesan or not kunci:
        messagebox.showwarning("Kesalahan Input", "Harap masukkan pesan dan kunci.")
        return

    pesan_terenkripsi = vigenere_cipher(pesan, kunci, mode='encrypt')
    result_label.configure(text=f"Pesan terenkripsi: {pesan_terenkripsi}")

def decrypt_message():
    pesan = message_entry.get().upper()
    kunci = key_entry.get().upper()

    if not pesan or not kunci:
        messagebox.showwarning("Kesalahan Input", "Harap masukkan pesan dan kunci.")
        return

    pesan_terdekripsi = vigenere_cipher(pesan, kunci, mode='decrypt')
    result_label.configure(text=f"Pesan terdekripsi: {pesan_terdekripsi}")

def reset_fields():
    message_entry.delete(0, ctk.END)
    key_entry.delete(0, ctk.END)
    result_label.configure(text="Hasil akan muncul di sini")

def add_image():
    image_path = "C:\\Users\\showa\\Downloads\\Python app\\666UR-Yuki-Setsuna-This-Scrunchie-Is-Too-Cute-for-Words-Colorful-Knitting-KeJFeJ-ai-brush-removebg-5xpnjt5r.png"
    
    # Buka gambar menggunakan PIL
    gambar = Image.open(image_path)
    gambar = gambar.resize((400, 200))  # Ubah ukuran gambar ke ukuran yang diinginkan
    gambar = ImageTk.PhotoImage(gambar)
    
    # Buat label untuk gambar
    image_label = ctk.CTkLabel(app, image=gambar, text="")
    image_label.image = gambar  # Simpan referensi untuk menghindari penghapusan otomatis
    image_label.place(relx=1.0, rely=1.0, anchor='se')  # Posisi di kanan bawah

    # Kirim label gambar ke latar belakang
    image_label.lower()


# Buat jendela aplikasi utama
app = ctk.CTk()
app.title("Program Vigenère Cipher")
app.geometry("500x400")

# Komponen UI
title_label = ctk.CTkLabel(app, text="Vigenère Cipher", font=("Arial", 24), text_color="#c5267e")
title_label.pack(pady=10)

message_label = ctk.CTkLabel(app, text="Masukkan pesan Anda:", text_color="#c5267e")
message_label.pack(pady=5)
message_entry = ctk.CTkEntry(app, width=300)
message_entry.pack(pady=5)

key_label = ctk.CTkLabel(app, text="Masukkan kunci:", text_color="#c5267e")
key_label.pack(pady=5)
key_entry = ctk.CTkEntry(app, width=300)
key_entry.pack(pady=5)

encrypt_button = ctk.CTkButton(app, text="Enkripsi", command=encrypt_message, fg_color="#F5D0A9", hover_color="#F9C6A2", text_color="#c5267e")
encrypt_button.pack(pady=10)

decrypt_button = ctk.CTkButton(app, text="Dekripsi", command=decrypt_message, fg_color="#F5D0A9", hover_color="#F9C6A2", text_color="#c5267e")
decrypt_button.pack(pady=10)

reset_button = ctk.CTkButton(app, text="Reset", command=reset_fields, fg_color="#F5D0A9", hover_color="#F9C6A2", text_color="#c5267e")
reset_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="Hasil akan muncul di sini", font=("Arial", 14), text_color="#c5267e")
result_label.pack(pady=20)

add_image()

# Jalankan aplikasi
app.mainloop()
