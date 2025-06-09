import os
import yt_dlp
from unidecode import unidecode

print("🎵 Olá, bem-vindo ao downTube!! 🎵")
lista_musicas = []

def progresso_hook(d):
    if d['status'] == 'downloading':
        print(f"⬇️ Baixando: {d.get('filename', 'arquivo')} | Progresso: {d.get('downloaded_bytes', 0) / 1024:.2f} KB")
    elif d['status'] == 'finished':
        print(f"✅ Download finalizado: {d['filename']}")

def adiciona_musica(quantidade):
    quant = quantidade + 1
    artista = input(f"N°{quant} - Digite o nome de um artista válido: \n")
    musica = input(f"N°{quant} - Agora digite o nome de uma música que o artista possua: \n")
    while True:
        tipo = str(input("Deseja a música apenas de estudio? \n Sim ou Não \n")).strip().lower()
        if unidecode(tipo) == "sim":
            tipo = "Lyrics"
        else:
            tipo = ""
        break
    artista_musica = unidecode(artista) + " - " + unidecode(musica) + " " + tipo
    lista_musicas.append(artista_musica)

def monta_lista_musica():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de músicas que você quer inserir na lista de downloads (apenas números): "))
            for q in range(quantidade):
                adiciona_musica(q)
            print("\n🎵 Sua lista de downloads atual:")
            for i, item in enumerate(lista_musicas, start=1):
                print(f"{i}. {item}")
            break
        except ValueError:
            print("⚠️ Entrada inválida! Por favor digite apenas números.\n")

def baixa_musicas(musica):
    path_down = os.path.join(os.getcwd(), "downloads")
    os.makedirs(path_down, exist_ok=True)

    url = f"ytsearch1:{musica}"  

    options = {
        'format': 'bestaudio/best',
        'outtmpl': f'{path_down}/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,  # silencia mensagens internas
        'progress_hooks': [progresso_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

while True:
    monta_lista_musica()

    while True:
        opcao_add = input("Deseja inserir mais alguma música à lista de download? (Sim ou Não): ").strip().lower()
        if unidecode(opcao_add) in ["sim", "nao"]:
            break
        else:
            print("⚠️ Opção inválida! Por favor digite Sim ou Não.\n")

    if unidecode(opcao_add) == "sim":
        continue  # volta para adicionar mais músicas
    
    print("Baixando as músicas, porfavor aguarde!!!")
    # Faz os downloads
    for musica in lista_musicas:
        baixa_musicas(musica)

    print("✅ Músicas abaixo baixadas com sucesso na pasta 'downloads'!\n")
    for i, item in enumerate(lista_musicas, start=1):
        print(f"{i}. {item}")

    while True:
        encerrar = input('Deseja baixar mais músicas ou encerrar o programa? (Baixar/Encerrar): ').strip().lower()
        if encerrar in ["baixar", "encerrar"]:
            break
        else:
            print("⚠️ Opção inválida! Por favor digite uma das opções válidas - Baixar ou Encerrar")

    if encerrar == "encerrar":
        print("👋 Encerrando o programa. Até a próxima!")
        break
    else:
        lista_musicas = []  # limpa lista para próxima rodada
