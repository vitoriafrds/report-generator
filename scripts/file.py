import sys
import mysql.connector 
from mysql.connector import Error
from mysql.connector import cursor
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def generateReport():
    file = open("relatorio_turma.txt", 'w')

    connection = mysql.connector.connect(host='localhost', database='mini_siga', user='root', password = 'thomaz080618')
    query = "SELECT * FROM RELACAO_FALTAS_TURMA"

    cursor = connection.cursor()
    cursor.execute(query)
        
    class_report = cursor.fetchall()

    file.write("\n")
    
    for report in class_report:
        file.write("\n")
        file.write("RA: " + str(report[0]) + " - " + "NOME: " + str(report[1]) + " - " + "DISCIPLINA: " + str(report[2]) + " - " + "DATA AULA: " + str(report[3]) + " - " + "PRESENCAS: " + str(report[4]) + " - " + "FALTAS: " + str(report[5]))
        file.write("\n")
    file.close()
    connection.close()


script=Tk()
script.title("PDF GENERATOR")
script.geometry("600x450")

button_generator = Button(script, text="Generate", command=generateReport)
button_generator.pack(side="left",padx=250)

script.mainloop()