import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("C:\\Users\\m s i\\Documents\\SEMESTER 3\\Pemrograman Multiplatform\\Praktikum\\PROJECT\\DatabaseProgram.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
nama_siswa TEXT, 
biologi REAL,
fisika REAL,
binggris REAL,                             
prediksi_fakultas TEXT)''')

conn.commit()
conn.close()

def fungsi_hitung():
    nama_siswa = nama_entry.get()
    nilai_biologi = float(biologi_entry.get())
    nilai_fisika = float(fisika_entry.get())
    nilai_binggris = float(binggris_entry.get())

    prediksi_fakultas = ""

    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_binggris:
        prediksi_fakultas="Hasil Prediksi: Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_binggris:
        prediksi_fakultas="Hasil Prediksi: Teknik"
    elif nilai_binggris > nilai_biologi and nilai_binggris > nilai_fisika:
        prediksi_fakultas="Hasil Prediksi: Bahasa"
    else:
        prediksi_fakultas ="Tidak Dapat Diprediksi"

    hasil_label.config(text=prediksi_fakultas)

    conn = sqlite3.connect("C:\\Users\\m s i\\Documents\\SEMESTER 3\\Pemrograman Multiplatform\\Praktikum\\PROJECT\\DatabaseProgram.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hasil_prediksi (nama_siswa, biologi, fisika, binggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
               (nama_siswa, nilai_biologi, nilai_fisika, nilai_binggris, prediksi_fakultas))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Informasi", "Data Berhasil Di-Submit")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.configure(bg="#ff7100")

# Membuat label judul
judul_label = tk.Label(root, text= " Selamat Datang Calon Mahasiswa Baru",font=("Chiller", 40, ),  bg= "#ff7100")
judul_label.pack(pady=5)

nama_label = tk.Label(root, text= "Nama Siswa : ",  font=("Calibri", 10, ),  bg= "#ff7100")
nama_label.pack()
nama_entry = tk.Entry(root, bg="#9baccf")
nama_entry.pack(pady=10)

biologi_label = tk.Label(root, text= "Nilai Mata Pelajaran Biologi : ", font=("Calibri", 10, ),  bg= "#ff7100")
biologi_label.pack()
biologi_entry = tk.Entry(root, bg="#9baccf")
biologi_entry.pack(pady=10)

fisika_label = tk.Label(root, text= "Nilai Mata Pelajaran Fisika : ", font=("Calibri", 10, ),  bg= "#ff7100")
fisika_label.pack()
fisika_entry = tk.Entry(root, bg="#9baccf")
fisika_entry.pack(pady=10)

binggris_label = tk.Label(root, text= "Nilai Mata Pelajaran Bahasa Inggris : ", font=("Calibri", 10, ),  bg= "#ff7100")
binggris_label.pack()
binggris_entry = tk.Entry(root, bg="#9baccf")
binggris_entry.pack(pady=10)

# Membuat tombol Hasil Prediksi
hasil_button = tk.Button(root, text="Submit Nilai", command=fungsi_hitung, bg="#9baccf")
hasil_button.pack(pady=20)


# Membuat label luaran hasil produksi
hasil_label = tk.Label(root, text="Hasil Prediksi: " , font=("Chiller", 40),  bg= "#ff7100")
hasil_label.pack()

root.mainloop()