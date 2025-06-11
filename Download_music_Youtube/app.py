#Bibliotecas importadas para o projeto
import os
import yt_dlp
from itertools import count
from unidecode import unidecode

# Mensagem inicial e implementação da lista de músicas
print("🎵 Olá, bem-vindo ao downTube!! 🎵")
lista_musicas = []

#Função que mostra o processo do download
def progresso_hook(d):
    #Condição If para mostrar o progresso do download da música retornando em um print no terminal
    if d['status'] == 'downloading':
        print(f"⬇️ Baixando: {d.get('filename', 'arquivo')} | Progresso: {d.get('downloaded_bytes', 0) / 1024:.2f} KB")
    #Caso o download tenha sido finalizado retorna o status no terminal
    elif d['status'] == 'finished':
        print(f"✅ Download finalizado: {d['filename']}")

#Função que adiciona as músicas a lista para o download
def adiciona_musica(quantidade):
    #Loop While de tratativa de resposta da pergunta
    while True:
        #Variável que define o tipo/qualidade da música, removendo todos os espaços e deixando tudo em minúsculo
        tipo = str(input("Deseja a música apenas de estudio? \n" 
                         "Sim ou Não \n")).strip().lower()
        
        #Condição de verificação do tipo para pegar a música apenas de estúdio ou se irá receber ao vivo também
        if unidecode(tipo) == "sim":
            tipo = "Lyrics"
            break

        #É utilizado unidecode para conversão no padrão ANCII e não gerar erros na resposta
        elif unidecode(tipo) == "nao":
            break

        #Caso seja uma resposta inválida o else mostra o print de notificação e retorna a execução até conseguir chegar 
        #em uma resposta válida para finalizar o Loop com o Break
        else:
            print("⚠️ Por favor digite uma opção válida!!! \n")      

    #Condição de verificação em caso seja mais de uma música para poder inserir uma lista completa. 
    if quantidade > 1:
        #Loop While de tratativa de resposta da pergunta
        while True:
            #Variável de verificação de recebimento de uma string com várias músicas ou uma inserção uma por uma.
            musica_lista_musicas = str(input("Deseja adicionar uma lista de músicas de uma vez ? \n" "Sim - Não: \n")).strip().lower()
            
            #Condição que recebe uma string com todas as músicas de uma vez.
            if musica_lista_musicas == 'sim':
                #Variável que recebe uma lista músicas em uma string sendo necessário obedecer o exemplo mostrado
                lista_varias_musicas = str(input("Digite a lista de músicas separando o artista da música com - e o próximo item com #. \n" 
                                                "Como no exemplo: Queen - We Are the Champions # Queen - We Will Rock You \n"  
                                                "Em caso de uma sintaxe diferente a busca não encontrará a música desejada!!!"))
                
                #Variável que separa as músicas em uma lista
                separa_itens = lista_varias_musicas.split("#")

                #Loop que separa os itens da lista de música em Artista e Música
                for x in separa_itens:
                    artista_musica_lista = str(x).split('-')
                    artista = artista_musica_lista[0]
                    musica = artista_musica_lista[1]
                    artista = artista.lstrip()
                    #Concatenação em uma string para busca com os dados de artista, música e tipo
                    artista_musica = artista + " - " + musica + " - " + tipo
                    #Adição dos dados na lista de downloads
                    lista_musicas.append(artista_musica)
                break

            #Condição onde o usuário terá que digitar artista e música de forma manual e  um de cada vez
            elif unidecode(musica_lista_musicas) == "nao":
                #Variáveis de recebimento dos dados
                artista = input(f"N°{quantidade} - Digite o nome de um artista válido: \n")
                musica = input(f"N°{quantidade} - Agora digite o nome de uma música que o artista possua: \n")
                #Concatenação em uma string para busca com os dados de artista, música e tipo
                artista_musica = artista + " - " + musica + " - " + tipo
                #Adição dos dados na lista de downloads
                lista_musicas.append(artista_musica)
                break

            #Caso seja uma resposta inválida o else mostra o print de notificação e retorna a execução até conseguir chegar 
            #Em uma resposta válida para finalizar o Loop com o Break
            else:
                print("⚠️ Por favor digite uma opção válida!!! \n")

    #Condição onde o usuário terá que digitar artista e música de forma manual e  um de cada vez
    else:
        #Variáveis de recebimento dos dados
        artista = input(f"N°{quantidade} - Digite o nome de um artista válido: \n")
        musica = input(f"N°{quantidade} - Agora digite o nome de uma música que o artista possua: \n")
        #Concatenação em uma string para busca com os dados de artista, música e tipo
        artista_musica = artista + " - " + musica + " - " + tipo
        #Adição dos dados na lista de downloads
        lista_musicas.append(artista_musica)

#Função que monta a lista de músicas
def monta_lista_musica():
    #Loop While de tratativa de resposta da pergunta
    while True:
        #Try de tratativa de dados 
        try:
            #Variável que recebe a quantidade de músicas a serem baixadas
            quantidade = int(input("Digite a quantidade de músicas que você quer inserir na lista de downloads (apenas números): \n"))
            
            #Condição que o usuário irá digitar um número válido
            if quantidade < 1:
                print("⚠️ Por favor digite uma opção válida!!! \n")
                continue

            #Chamada da função de adição das músicas nas listas
            adiciona_musica(quantidade)
            #Print de apresentação das músicas adicionadas para verificação 
            print("🎵 Sua lista de downloads atual: \n")
            #Loop de apresentação da lista de músicas com uma formatação dos dados
            for i, item in enumerate(lista_musicas, start=1):
                print(f"{i}. {item}")
            break
        #Exeção em caso seja digitado um dado diferente de um número
        except ValueError:
            print("⚠️ Entrada inválida! Por favor digite apenas números.\n")

#Função de download das músicas
def baixa_musicas(musica):
    #Variáveis de definição da pasta e criação da mesma caso ela não exista
    path_down = os.path.join(os.getcwd(), "downloads")
    os.makedirs(path_down, exist_ok=True)
    #Variável de concatenação dos dados da música com os parâmetros de pesquisa
    url = f"ytsearch1:{musica}"  
    #Definição dos parâmetros da pesquisa para download pela biblioteca
    options = {
        'format': 'bestaudio/best', #Formato do áudio
        'outtmpl': f'{path_down}/%(title)s.%(ext)s', #Caminho e nome do arquivo após o download
        'noplaylist': True, #Remove os vídeos de playlist
        'quiet': True,  #Silencia mensagens internas
        'progress_hooks': [progresso_hook], #Pega os parâmetros de download para mostrar o progresso
        #Define o formato e como será convertido o áudio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    #Chamada da biblioteca passando os parâmetros para download
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

#Loop de execução do programa
while True:
    #Chamada da função para montar a lista de músicas para downloads
    monta_lista_musica()
    #Loop While de tratativa de resposta da pergunta
    while True:
        #Variável de verificação se caso o usuário queira adicionar mais músicas
        opcao_add = input("Deseja inserir mais alguma música à lista de download? (Sim ou Não): \n").strip().lower()
        #Condição de verificação da resposta
        if unidecode(opcao_add) in ["sim", "nao"]:
            break
        #Tratativa em caso a resposta seja inválida
        else:
            print("⚠️ Opção inválida! Por favor digite Sim ou Não.\n")

    #Condição que finaliza o processo do loop para retornar ao processo de adição de músicas
    if unidecode(opcao_add) == "sim":
        continue  #Volta para adicionar mais músicas
    
    print("Baixando as músicas, porfavor aguarde!!!")
    #Loop de realização dos downloads
    for musica in lista_musicas:
        #Chamada da função de download dos arquivos 
        baixa_musicas(musica)

    print("✅ Músicas abaixo baixadas com sucesso na pasta 'downloads'!\n")
    #Loop de apresentação da lista de músicas baixadas
    for i, item in enumerate(lista_musicas, start=1):
        print(f"{i}. {item}")

    #Loop While de tratativa de resposta da pergunta 
    while True:
        #Variável de condição de finalização do programa
        encerrar = input('Deseja baixar mais músicas ou encerrar o programa? (Baixar/Encerrar): ').strip().lower()
        
        #Condição para finalização do programa ou continuação de mais um processo de download
        if encerrar in ["baixar", "encerrar"]:
            break
        #Tratativa em caso a resposta seja inválida
        else:
            print("⚠️ Opção inválida! Por favor digite uma das opções válidas - Baixar ou Encerrar")

    #Condição para finalização do programa
    if encerrar == "encerrar":
        print("👋 Encerrando o programa. Até a próxima!")
        break
    #Caso não deseje finalizar o programa
    else:
        lista_musicas = []  #Limpa lista para próxima rodada