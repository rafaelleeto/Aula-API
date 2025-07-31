import customtkinter as tk
import requests
import pprint

tk.set_appearance_mode("dark")
key = "52e7a9f1afe947949c5175521253107"
url = " http://api.weatherapi.com/v1/current.json"



subjanela = tk.CTk()
subjanela.title("Cotação Atual")
subjanela.geometry("500x500")
subjanela.grab_set()
label = tk.CTkLabel(subjanela,text="Selecione Uma cidade que deseja ver a Temperatura")
label.pack()
opcoes = ["Curitiba","Rio De Janeiro","Pelotas"]
combobox = tk.CTkComboBox(master=subjanela, values=opcoes)
combobox.pack(padx=20, pady=20)

botao = tk.CTkButton(master=subjanela,text="Escolher",command=lambda:ver_temperatura(combobox.get()))
botao.pack()

def ver_temperatura(cidade_escolhida):
    subjanela = tk.CTkToplevel()
    subjanela.geometry("200x200")
    subjanela.grab_set()
    parametros = {
    "key" : key,
    "q" : cidade_escolhida,
    "lang" : "pt"
    }
    variavel = requests.get(url,params=parametros).json()
    label = tk.CTkLabel(subjanela,text=f"A temperatura de {cidade_escolhida} é de {variavel["current"]["temp_c"]}")
    label.pack()
    

    
    
    





if __name__ == "__main__":
    subjanela.mainloop()

        
