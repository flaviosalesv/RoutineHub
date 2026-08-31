import customtkinter as ctk

def login_func(window):
    window.title('Login')
    window.geometry('900x900')

    ctk.CTkLabel(window, text='Welcome to RoutineHub!').pack()



    user_entry = ctk.CTkEntry(window, placeholder_text='Digite seu nome de usuário: ')
    user_entry.pack()

    password_entry = ctk.CTkEntry(window, placeholder_text='Digite sua senha: ')
    password_entry.pack()

    def button_entry():
        if user_entry.get() == 'usuario' and password_entry.get() == '000':
            print('OK')
        else:
            print('ERROR')


    ctk.CTkButton(window, text='Login', command=button_entry).pack()


