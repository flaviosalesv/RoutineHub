import customtkinter as ctk
import sqlite3

connection = sqlite3.connect('routinehub.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        date TEXT UNIQUE,
        number_of_questions INTEGER
    )
""")

connection.commit()

cursor.execute("SELECT * FROM questions")

results = cursor.fetchall()

print(results)


def questions_menu(window):
    window.title('RoutineHub')
    window.geometry('900x900')

    ctk.CTkLabel(window, text='Questões').pack()

    date_entry = ctk.CTkEntry(window, placeholder_text='Digite a data')
    date_entry.pack()

    questions_entry = ctk.CTkEntry(window, placeholder_text='Número de questões')
    questions_entry.pack()

    def save_questions():
        date = date_entry.get()
        number_of_questions = questions_entry.get()

        try:
            cursor.execute("""
                INSERT INTO questions (date, number_of_questions)
                VALUES (?, ?)
            """, (date, number_of_questions))

            connection.commit()

            date_entry.delete(0, 'end')
            questions_entry.delete(0, 'end')

        except:
            ctk.CTkLabel(window, text='Já existe um registro para essa data!').pack()

    ctk.CTkButton(window, text='Salvar', command=save_questions).pack()