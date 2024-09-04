from tkinter import *
from tkinter import ttk


def open_admin_login():
    admin_window = Toplevel(root)
    admin_window.title("Вхід для Адміна")
    admin_window.geometry("500x500")
    admin_window.resizable(False, False)

    Label(admin_window, text="Логін Адміна:", font=("Helvetica", 14)).pack(pady=10)
    Entry(admin_window, font=("Helvetica", 12)).pack(pady=5)
    Label(admin_window, text="Пароль Адміна:", font=("Helvetica", 14)).pack(pady=10)
    Entry(admin_window, font=("Helvetica", 12), show="*").pack(pady=5)
    Button(admin_window, text="Увійти", font=("Helvetica", 12)).pack(pady=20)


def open_subscriber_login():
    #for commit
    subscriber_window = Toplevel(root)
    subscriber_window.title("Вхід для Абонента")
    subscriber_window.geometry("500x500")
    subscriber_window.resizable(False, False)

    Label(subscriber_window, text="Логін Абонента:", font=("Helvetica", 14)).pack(pady=10)
    Entry(subscriber_window, font=("Helvetica", 12)).pack(pady=5)
    Label(subscriber_window, text="Пароль Абонента:", font=("Helvetica", 14)).pack(pady=10)
    Entry(subscriber_window, font=("Helvetica", 12), show="*").pack(pady=5)
    Button(subscriber_window, text="Увійти", font=("Helvetica", 12)).pack(pady=20)


root = Tk()
root.title("Керування провайдингом інтернету")
root.geometry("500x500")
root.resizable(False, False)

# Створення стилю для кнопок
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 14),
                padding=10,
                foreground="#01579B",
                background="#B3E5FC")

# Створення контейнера для кнопок
button_frame = Frame(root)
button_frame.pack(expand=True)

# Створення кнопок з використанням стилю
admin_sign_in_btn = ttk.Button(button_frame, text="Адмін", style="TButton", command=open_admin_login)
abonent_sign_in_btn = ttk.Button(button_frame, text="Абонент", style="TButton", command=open_subscriber_login)

# Розміщення кнопок поруч
admin_sign_in_btn.pack(side=LEFT, padx=20, pady=10)
abonent_sign_in_btn.pack(side=LEFT, padx=20, pady=10)

# Основний цикл програми
root.mainloop()
