import customtkinter as ctk

def menu_choices(window):
    window.title('RoutineHub')
    window.geometry('900x900')

    ctk.CTkLabel(window, text='Escolha uma das opções abaixo:').pack()

    ctk.CTkButton(window, text='Questões').pack()
    ctk.CTkButton(window, text='Treinos').pack()
    ctk.CTkButton(window, text='Fechar').pack()