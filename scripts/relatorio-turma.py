from fpdf import FPDF
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def generatePDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=8)

    pdf.cell(200, 10, txt="RELATORIO DE FALTAS DA TURMA", ln=1, align='C')
    pdf.cell(200, 10, txt="[FATEC ZONA LESTE] - RELATORIO DE FALTAS DA TURMA - SAO PAULO", ln=1, align='C')

    file = open("relatorio_turma.txt", 'r')

    for line in file:
        pdf.cell(200, 10, txt=line, ln=1, align='L')


    pdf.output("relatorio.pdf")



script=Tk()
script.title("PDF GENERATOR")
script.geometry("600x450")

button_generator = Button(script, text="Generate", command=generatePDF)
button_generator.pack(side="left",padx=250)

script.mainloop()