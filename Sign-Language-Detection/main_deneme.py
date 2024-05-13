import tkinter as tk
from tkinter import ttk
import subprocess

def run_test(category):
    try:
        subprocess.run(["python", "test_yon.py", category])
    except FileNotFoundError:
        print("test.py dosyası bulunamadı.")

def main():
    root = tk.Tk()
    root.title("İşaret Dili Algılama Sistemi")
    root.geometry("1200x750")
    
    # Başlık etiketi
    label1 = tk.Label(root, text="İşaret Dili Algılama Sistemine Hoşgeldiniz!", font=("Monotype Corsiva", 25), fg="steel blue")
    label1.pack(pady=20)
    
    # Kategori seçimi için etiket
    label2 = tk.Label(root, text="Lütfen Bir Kategori Seçiniz!", font=("Times New Roman", 16, "italic"), fg="royal blue")
    label2.pack(pady=10)
    
    # Kategori butonları
    categories = ["Yiyecek", "Alfabe", "Hayvan", "Eşya", "Taşıt", "Yön", "Renk", "Fiil", "Meslek", "Sayı"]
    num_columns = 2
    for i in range(0, len(categories), num_columns):
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)
        for j in range(num_columns):
            if i + j < len(categories):
                button = tk.Button(button_frame, text=categories[i + j], font=("Times New Roman", 14), bg="lightblue", fg="black", width=15, command=lambda cat=categories[i + j]: run_test(cat))
                button.grid(row=0, column=j, padx=5)
    
    # Listview'lar için çerçeve oluştur
    listview_frame = tk.Frame(root)
    listview_frame.pack(pady=20)

    # Hakkında Listview
    listview1 = ttk.Treeview(listview_frame)
    listview1["columns"] = ("1")
    listview1.column("#0", width=400, minwidth=400)
    listview1.heading("#0", text="Hakkında", anchor=tk.CENTER)  # Başlığı ortala
    listview1.insert("", "end", text="Trakya Üniversitesi bitirme projesi.", values=(""))
    listview1.pack(side=tk.LEFT, padx=20)

    # Ana Sayfa Listview
    listview2 = ttk.Treeview(listview_frame)
    listview2["columns"] = ("1")
    listview2.column("#0", width=400, minwidth=400)
    listview2.heading("#0", text="Ana Sayfa", anchor=tk.CENTER)  # Başlığı ortala
    ana_sayfa_kategorileri = [
        "Yiyecek kategorisinde 15 kelime bulunmaktadır.",
        "Alfabe kategorisinde 15 kelime bulunmaktadır.",
        "Hayvan kategorisinde 15 kelime bulunmaktadır.",
        "Eşya kategorisinde 15 kelime bulunmaktadır.",
        "Taşıt kategorisinde 15 kelime bulunmaktadır.",
        "Yön kategorisinde 15 kelime bulunmaktadır.",
        "Renk kategorisinde 15 kelime bulunmaktadır.",
        "Fiil kategorisinde 15 kelime bulunmaktadır.",
        "Meslek kategorisinde 15 kelime bulunmaktadır.",
        "Sayı kategorisinde 15 kelime bulunmaktadır."
    ]
    for kategori in ana_sayfa_kategorileri:
        listview2.insert("", "end", text=kategori, values=(""))
    listview2.pack(side=tk.LEFT, padx=20)

    # İletişim Listview
    listview3 = ttk.Treeview(listview_frame)
    listview3["columns"] = ("1")
    listview3.column("#0", width=400, minwidth=400)
    listview3.heading("#0", text="İletişim", anchor=tk.CENTER)  # Başlığı ortala
    iletişim_bilgileri = ["example1@example.com", "example2@example.com", "example3@example.com", "example4@example.com"]
    for mail in iletişim_bilgileri:
        listview3.insert("", "end", text="", values=(mail,))
    listview3.pack(side=tk.LEFT, padx=20)

    # Yatay kaydırma çubukları ekle
    h_scrollbar = ttk.Scrollbar(listview_frame, orient="horizontal", command=lambda *args: _scroll(*args, listviews=(listview1, listview2, listview3)))
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    root.mainloop()

def _scroll(*args, listviews):
    for listview in listviews:
        listview.xview(*args)

if __name__ == "__main__":
    main()
