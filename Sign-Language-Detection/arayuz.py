import os
from subprocess import call
from customtkinter import *
from PIL import Image
import tkinter as tk
# -*- coding: utf-8 -*-

def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))

def change_working_directory(script_dir):
    os.chdir(script_dir)

def open_new_window(text):
    new_window = CTk()
    new_window.geometry("980x600")
    new_window.resizable(0, 0)
    
    # Ana pencerenin arka plan rengini ayarla
    new_window.configure(bg="black")
    
    # Metni gösterecek frame'i oluştur
    text_frame = tk.Frame(master=new_window, bg="black")
    text_frame.pack(pady=(30, 0), padx=30, fill="both", expand=True)

    # Çok satırlı metin widget'ı oluştur
    text_widget = tk.Text(master=text_frame, font=("Arial", 15), wrap="word")
    text_widget.pack(pady=10, padx=10, fill="both", expand=True)

    # Metni text widget'ına ekle
    text_widget.insert("1.0", text)

    # Metnin tamamını görüntülemek için scroll et
    text_widget.configure(state='disabled')  # Metin düzenlenemez durumda ayarla
    text_widget.see("1.0")  # Metnin başlangıcını görünür kıl
    text_widget.configure(state='normal')  # Metin düzenlenebilir duruma geri dön
    
    new_window.mainloop()
    
def handle_image_click(image_name):
    if image_name == "foto-5.png":
        open_new_window("""                     İşitme Engelliler 
                        
    Ülkemizde yılda yaklaşık 1.100.000’ e yakın bebek doğmakta ve her bin bebekten 2-3’ü işitme 
    kaybı ile dünyaya gelmektedir. 
    
    Çocukluk döneminde geçirilen hastalıklar, kulak enfeksiyonları, kazalar ve kullanılan bazı ilaçlar 
    nedeniyle bu oran geçici işitme kayıplarıyla birlikte %6’ya kadar çıkmaktadır. 
    
    Ülkemizdeki işitme engelli sayısına ilişkin verilere baktığımızda; Aile ve Sosyal Hizmetler 
    Bakanlığınca oluşturulan Ulusal Engelli Veri Sisteminde kayıtlı ve hayatta olan engelli sayısı;
     
    1.414.643’ü erkek, 1.097.307’si kadın olmak üzere 2.511.950 olduğu görülmekte ve bunların 
    179.867’sini işitme engelliler oluşturmaktadır.
    
                        Dilsiz Çevirmeni Projesi
                                             
    Projemiz, 'Dijital erişilebilirlik her bireyin temel hakkıdır; doğduğumuz şartlar ne olursa olsun, 
    yaşamın her alanında eşit fırsatlara sahip olmalıyız' ilkesini benimseyerek, toplumsal adalet ve 
    eşitlik için çaba göstermektedir.
    
    Proje kapsamında Türk alfabesini içeren 29 harften oluşan bir alfabeyi kamera aracılığıyla tanıyan 
    bir sistem geliştirilmiştir. Ayrıca, işaret dili kullanarak 100 farklı kelimeyi tanımlayan bir veritabanı 
    oluşturulmuştur. 
    

""")
   
        
#Kamera açma
def run_test(test_file):
    call(["python", test_file])

#Kategori sayfası
def open_category_window():
    category_window = CTk()
    category_window.geometry("300x500")
    category_window.resizable(0, 0)

    CTkLabel(master=category_window, text="Kategori Seçiniz", font=("Arial Bold", 20)).pack(pady=(20, 30))

    categories = ["Esya", "Fiil", "Hayvan", "Meslek", "Renk",
                  "Sayi", "Tasit", "Yiyecek", "Yon"]

    for category in categories:
        CTkButton(master=category_window, text=category, font=("Arial", 12), command=lambda c=category: run_test(f"test_{c.lower()}.py")).pack(pady=5)

    category_window.mainloop()

#Cümle sayfası olacak
def open_sentences_window():
    sentences_window = CTk()
    sentences_window.geometry("300x400")
    sentences_window.resizable(0, 0)

script_dir = get_script_directory()
change_working_directory(script_dir)

app = CTk()
app.geometry("980x600")
app.resizable(0, 0)

set_appearance_mode("dark")

#Başlık
CTkLabel(master=app, text="Dilsiz Cevirmeni", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(43, 18), padx=(56,0))

stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")
quizzes_taken_frame = CTkFrame(master=stats_frame, fg_color="#70179A", width=132, height=70, corner_radius=8)
quizzes_taken_frame.pack_propagate(0)
quizzes_taken_frame.pack(anchor="w", side="left", padx=(0, 20))

alpha_button = CTkButton(master=quizzes_taken_frame, text="Alfabe", font=("Arial Bold", 10), text_color="#F3D9FF", command=lambda: run_test("test_alfabe.py"), fg_color="#70179A")
alpha_button.pack(anchor="nw")
CTkLabel(master=quizzes_taken_frame, text="29", justify="left",  font=("Arial Bold", 25), text_color="#F3D9FF").pack(anchor="nw", padx=(14, 0))
correct_qs_frame = CTkFrame(master=stats_frame, fg_color="#146C63", width=132, height=70, corner_radius=8)
correct_qs_frame.pack_propagate(0)
correct_qs_frame.pack(anchor="w", side="left", padx=(0, 20))

kelimeler_button = CTkButton(master=correct_qs_frame, text="Kelimeler", font=("Arial Bold", 10), text_color="#D5FFFB",
                             command=open_category_window, fg_color="#146C63")
kelimeler_button.pack(anchor="nw")
CTkLabel(master=correct_qs_frame, text="100", justify="left",  font=("Arial Bold", 25), text_color="#D5FFFB").pack(anchor="nw", padx=(14, 0))
highest_score_frame = CTkFrame(master=stats_frame, fg_color="#9A1717", width=132, height=70, corner_radius=8)
highest_score_frame.pack_propagate(0)
highest_score_frame.pack(anchor="w", side="left", padx=(0, 20))
cümleler_button = CTkButton(master=highest_score_frame, text="Cümleler", font=("Arial Bold", 10), text_color="#FFCFCF",
  command=open_sentences_window, fg_color="#9A1717")
cümleler_button.pack(anchor="nw")
CTkLabel(master=highest_score_frame, text="0", justify="left",  font=("Arial Bold", 25), text_color="#FFCFCF").pack(anchor="nw", padx=(14, 0))

def on_image_click(image_name):
    return lambda event: handle_image_click(image_name)

CTkLabel(master=app, text="Dijital erişilebilirlik herkesin hakkı! Eşit şartlarda doğmasak da, eşit şartlarda yaşayabiliriz", font=("Arial Bold", 20), justify="left").pack(anchor="nw", side="top", padx=(56, 0), pady=(41, 0))
quizzes_frame = CTkFrame(master=app, fg_color="transparent")
quizzes_frame.pack(pady=(21, 0), padx=(50, 0), anchor="nw")

movies_img_data1 = Image.open("sports-quiz-bg.png")
movies_img1 = CTkImage(light_image=movies_img_data1, dark_image=movies_img_data1, size=(400, 300))
label1 = CTkLabel(master=quizzes_frame, text="", image=movies_img1, corner_radius=8, font=("Arial", 40))
label1.pack(side="left", padx=(0, 20))
label1.bind("<Button-1>", on_image_click("foto-5.png"))

movies_img_data2 = Image.open("sports-quiz-bg.png")
movies_img2 = CTkImage(light_image=movies_img_data2, dark_image=movies_img_data2, size=(400, 300))
label2 = CTkLabel(master=quizzes_frame, text="", image=movies_img2, corner_radius=8)
label2.pack(side="left")
label2.bind("<Button-1>", on_image_click("photo_1.png"))

app.mainloop()