import customtkinter as ctk
from menu import menu_choices

window = ctk.CTk()

window.title('RoutineHub')
window.geometry('900x900')

ctk.CTkLabel(window, text='Welcome to RoutineHub!', font=('Arial', 20)).pack(pady=(300, 20))



user_entry = ctk.CTkEntry(window, placeholder_text='Username: ')
user_entry.pack(pady=3)

password_entry = ctk.CTkEntry(window, placeholder_text='Password: ')
password_entry.pack(pady=3)

def button_entry():
        if user_entry.get() == 'user' and password_entry.get() == '0':
            for widget in window.winfo_children():
                widget.destroy()

            menu_choices(window)
        else:
            ctk.CTkLabel(window, text='Usuário ou senha incorretos!').pack()


ctk.CTkButton(window, text='Login', command=button_entry).pack(pady=10)

window.mainloop()
