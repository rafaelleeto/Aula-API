import customtkinter as tk
from tkinter import messagebox
import requests





tk.set_appearance_mode("dark")  
tk.set_default_color_theme("blue")  


janela = tk.CTk()
janela.title("Cotação real")
janela.geometry("500x500")

moedas = ["USD","EUR","BTC"]

label = tk.CTkLabel(janela,text="Selecione Uma moeda que deseja ver a conversão")
label.pack()
combobox = tk.CTkComboBox(master=janela, values=moedas)
combobox.pack(padx=20, pady=20)

botao = tk.CTkButton(janela,text="Confirmar",command=lambda: enviar_moeda(combobox.get()))
botao.pack()

def enviar_moeda(variavel):
    dicionario = {"USD": "USD-BRL",
                  "EUR" : "EUR-BRL",
                  "BTC" : "BTC-BRL"
        }
    
    moeda = dicionario.get(variavel, "")
    
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
    nova_moeda = moeda.strip().replace("-","")
    cotacao = requests.get(url).json()
    subjanela = tk.CTkToplevel()
    subjanela.title("Cotação Atual")
    subjanela.geometry("200x200")
    subjanela.grab_set()
    
    
    label = tk.CTkLabel(master=subjanela,text=f"Conversão de {moeda} para BRL")
    label = tk.CTkLabel(master=subjanela,text=f"{cotacao[nova_moeda]["bid"]}")
    label.pack()
    
if __name__ == "__main__":
    janela.mainloop()
