import customtkinter as ctk
import questions
import trainings

def questions_button(window):
        for menu_widget in window.winfo_children():
            menu_widget.destroy()

        questions.questions_menu(window)

def trainings_button(window):
        for menu_widget in window.winfo_children():
            menu_widget.destroy()

        trainings.trainings_menu(window)


def menu_choices(window):
    window.title('RoutineHub')
    window.geometry('900x900')

    ctk.CTkLabel(window, text='Escolha uma das opções abaixo:', font=('Arial', 20)).pack(pady=(300, 20))


    ctk.CTkButton(window, text='Questões', command=lambda: questions_button(window)).pack(pady=3)
    ctk.CTkButton(window, text='Treinos', command=lambda: trainings_button(window)).pack(pady=3)
    ctk.CTkButton(window, text='Fechar', command=window.destroy).pack(pady=3)
