#Importação das bibliotecas 
import tkinter as tk 
import os
import yt_dlp
from itertools import count
from unidecode import unidecode
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
import platform
import subprocess

#Função para abrir a pasta downloads
def abrir_pasta_downloads():
    caminho = os.path.join(os.getcwd(), "downloads")

    # Garante que a pasta existe
    os.makedirs(caminho, exist_ok=True)

    sistema = platform.system()

    try:
        if sistema == "Windows":
            os.startfile(caminho)
        elif sistema == "Darwin":  # macOS
            subprocess.Popen(["open", caminho])
        else:  # Linux
            subprocess.Popen(["xdg-open", caminho])
    except Exception as e:
        print(f"Erro ao abrir a pasta: {e}")
     
#Função de tratativa do valor digitado
def download_tratativa():
    download = ent_musica.get()
    if download:
        baixa_musicas(download)
    else:
        messagebox.showerror("Erro", "Você não digitou nada!!!")

#Função de download das músicas
def baixa_musicas(musica):
    try:
        path_down = os.path.join(os.getcwd(), "downloads")
        os.makedirs(path_down, exist_ok=True)
        url = f"ytsearch1:{musica}"  
        options = {
            'format': 'bestaudio/best',
            'outtmpl': f'{path_down}/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'progress_hooks': [progresso_hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    except Exception:
        messagebox.ERROR("Erro ao executar o download!!!")

#Função de mostrador de progresso 
def progresso_hook(d):
    if d['status'] == 'downloading':
        lb_download.config(text=f"⬇️ Baixando: {d.get('filename', 'arquivo')} ")
        lb_download.update()
    #Caso o download tenha sido finalizado retorna o status no terminal
    elif d['status'] == 'finished':
        lb_download.config(text=f"✅ Download finalizado: {d['filename']}")
        lb_download.update()

#Função de responsividade da tela 
def ajustar_wraplength(event):
    largura = event.width
    lb_musica.config(wraplength=largura - 40)
    lb_download.config(wraplength=largura - 40)

#Página Home do app e suas definições
home = tk.Tk()
home.title("🎵 Olá, bem-vindo ao downTube!! 🎵")
home.geometry("800x400")
home.configure(bg="black")

# Torna colunas expansíveis
home.grid_columnconfigure(0, weight=1)
home.grid_columnconfigure(1, weight=1)
home.grid_rowconfigure(2, weight=1)

#Definição de customização da fonte
font_custom = tkFont.Font(family="Calibri", size=16, weight="bold")

#Label de instrução
lb_musica = tk.Label(
    home,
    text="Digite a música que você quer realizar o download:",
    bg="black",
    fg="white",
    font=font_custom,
    wraplength=800,
    justify="left"
)
lb_musica.grid(column=0, row=0, columnspan=2, padx=5, pady=55, sticky="ew")

#Entry que recebe a música
ent_musica = tk.Entry(home, font=font_custom)
ent_musica.grid(column=0, row=1, padx=20, pady=5)

#Botão de download
btn_download = tk.Button(home, text="Baixar", command=download_tratativa)
btn_download.grid(column=1, row=1, padx=20, pady=5)

#Label de status do download
lb_download = tk.Label(
    home,
    text="",
    bg="black",
    fg="white",
    font=font_custom,
    wraplength=800,
    justify="left"
)
lb_download.grid(column=0, row=2, columnspan=2, padx=5, pady=10, sticky="ew")

#Botão para abrir a pasta dos downloads
btn_pasta_download = tk.Button(home, text="Abrir pasta", command=abrir_pasta_downloads)
btn_pasta_download.grid(column=1, row=2, padx=20, pady=5)

# Atualiza o wraplength quando a janela é redimensionada
home.bind("<Configure>", ajustar_wraplength)

home.mainloop()
