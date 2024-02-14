import tkinter as tk
from tkinter import messagebox
import re

def lexical_analyzer(input_string):
    palabras_reservadas = set(['Area','base','altura'])
    
    patterns = {
        'PALABRA R': '|'.join(palabras_reservadas),
        'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'OPERADOR': r'[-+*/=]',
        'NUMERO': r'\d+',
        'SIMBOLO': r'[()]'
    }

    token_types = {key: set() for key in patterns.keys()}

    for key, pattern in patterns.items():
        matches = re.findall(pattern, input_string)
        for match in matches:
            token_types[key].add(match)

    palabras_reservadas_encontradas = token_types['PALABRA R']
    for key, pattern in patterns.items():
        if key != 'PALABRA R':
            token_types[key] = token_types[key].difference(palabras_reservadas_encontradas)

    return token_types

def display_table(token_types):
    result = ""
    result += '{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format('TOKEN', 'PALABRA R', 'IDENTIFICADOR', 'OPERADOR', 'NUMERO', 'SIMBOLO') + "\n"
    for token in set.union(*(token_types.values())):
        result += '{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format(
            token, 
            'X' if token in token_types['PALABRA R'] else '', 
            'X' if token in token_types['IDENTIFICADOR'] else '', 
            'X' if token in token_types['OPERADOR'] else '', 
            'X' if token in token_types['NUMERO'] else '', 
            'X' if token in token_types['SIMBOLO'] else ''
        ) + "\n"
    return result

def analyze_input():
    input_string = input_entry.get()
    if not input_string:
        messagebox.showerror("Error", "Por favor, ingresa una cadena válida.")
        return
    token_types = lexical_analyzer(input_string)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, display_table(token_types))

root = tk.Tk()
root.title("Analizador Léxico")

root.configure(background='#ADD8E6')

input_label = tk.Label(root, text="Ingrese la cadena a analizar:", bg="light blue")
input_label.pack()

input_entry = tk.Entry(root, width=50)
input_entry.pack()

analyze_button = tk.Button(root, text="Analizar", command=analyze_input, bg="light blue")
analyze_button.pack()

result_label = tk.Label(root, text="Resultados:", bg="light blue")
result_label.pack()

result_text = tk.Text(root, height=20, width=100)
result_text.pack()

# Ejecutar la interfaz
root.mainloop()
