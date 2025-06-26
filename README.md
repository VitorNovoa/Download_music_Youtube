<div align="center">

# 🤖 Dowtube

</div>

##  Sobre o Projeto🎵
Este projeto foi desenvolvido com o objetivo de simplificar o processo de download de músicas do YouTube, tornando essa tarefa mais intuitiva, didática e acessível para qualquer usuário. Ideal para quem deseja automatizar downloads de forma prática, utilizando ferramentas modernas e com instruções claras.

**Linguagem:** 🐍Python. <br>
<table style="border:1px solid white; border-collapse: collapse;">
  <tr>
    <th style="border:1px solid white; padding: 5px; text-align: center;">Ferramentas⚒️</th>
    <th style="border:1px solid white; padding: 5px; text-align: center;">Função</th>
  </tr>
  <tr>
    <td style="border:1px solid white; padding: 5px; text-align: center;">PATH ffmpeg</td>
    <td style="border:1px solid white; padding: 5px; text-align: center;">Para fazer download e conversão</td>
  </tr>
  <tr>
    <td style="border:1px solid white; padding: 5px; text-align: center;">Biblioteca python yt_dlp</td>
    <td style="border:1px solid white; padding: 5px; text-align: center;">Para pesquisar o nome, pegar o link e baixar</td>
  </tr>
</table>


**Autor do projeto:** Vitor Novoa ([Linkedin](https://www.linkedin.com/in/vitor--novoa/)) <br>
**Autora do readme e testes:** Jéssica Buzzo ([Linkedin](https://www.linkedin.com/in/j%C3%A9ssica-s-buzzo-8a0390194/) e [Github](https://github.com/JSBuzzo))<br>

---

### O que precisa para fazer funcionar?  <br>

-Instalar o PATH ffmpeg;  <br>
-Instalar a biblioteca python yt_dlp.  <br>

---

#### Como Instalar o PATH ffmpeg?  <br>
 
- Abrir o site https://ffmpeg.org/download.html;  <br>

<span style="color:salmon;"> Os seguintes passos serão diferentes caso seu sistema operacional não seja windows. <br>

- Terão duas opções windows, selecione gyan.dev;  <br>
- Selecione ffmpeg-release-essentials.7z;  <br>

---

Vai ser criada uma pasta zip:  <br>
- Descompacte essa pasta;  <br>
- Crie uma pasta ffmpeg;  <br>
- Colar o arquivo da pasta que você descompactou na pasta criada;<br>

---

No menu do computador:  <br>
- Pesquise por variáveis de ambiente e selecione "Editar as variáveis de ambiente do  sistema".  <br>
- Vai abrir uma tela, no canto inferior esquerdo selecione "variáveis de ambiente";  <br>

---

Em variáveis de sistema:  <br>
- Crie uma nova com o nome de ffmpeg;  <br>
- No valor selecione a pasta "Bin" (procure no diretório);  <br>
- Finalize e reinicie o computador.  <br>

---

#### Como Instalar a biblioteca python yt_dlp?<br>

<table style="border:1px solid white; border-collapse: collapse;">
  <tr>
    <th style="border:1px solid red; padding: 2px; text-align: center;color:red">Para o uso precisa ter o python instalado</th>
  </tr>
 </table> 

No editor da sua preferência (no caso desse projeto, VScode) abra o terminal;<br>

```
pip install yt_dlp
pip unidecode
```