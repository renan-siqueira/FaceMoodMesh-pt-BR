# Mood-Mesh-Viewer

Este projeto é uma ferramenta desenvolvida em Python, que combina tecnologias de visão computacional para exibir vídeos com a capacidade de identificar e anotar pontos faciais e emoções das faces presentes nos quadros.

Essa versão foi criada pensando na comunidade brasileira de desenvolvedores e por isso conta com toda a documentação em português.

*__[If you want to access English version, click here](https://github.com/renan-siqueira/Mood-Mesh-Viewer)__*

---

## Por que escolher o Mood-Mesh-Viewer?

Em uma era onde a tecnologia evolui rapidamente, ter ferramentas que são simultaneamente poderosas e amigáveis é um verdadeiro tesouro. 

__"Mood-Mesh-Viewer"__ é exatamente isso - um equilíbrio perfeito entre simplicidade e eficácia. 

Se você é um iniciante que deseja se aventurar no fascinante mundo da visão computacional, esta é a sua porta de entrada perfeita. 

Para os usuários avançados, é uma plataforma flexível que pode ser adaptada e ampliada de acordo com suas necessidades.

A capacidade de visualizar vídeos e, ao mesmo tempo, analisar emoções e pontos faciais pode ser transformadora em diversos campos, desde entretenimento até saúde mental. 

Além disso, com a natureza modular do __"Mood-Mesh-Viewer"__, o céu é o limite quando se trata de personalização e extensão.

Não se deixe enganar pela simplicidade de configuração e uso; sob esse exterior acessível encontra-se uma ferramenta robusta, capaz de fornecer insights valiosos e análises aprofundadas. 

Em resumo, o "Mood-Mesh-Viewer" é a combinação ideal para quem busca alcançar grandes feitos sem se perder em configurações complexas e códigos enigmáticos. 

__Dê o passo adiante e descubra por si mesmo!__

---

## Configuração Inicial

### 1. Criação do Virtual Environment:

Primeiramente, é altamente recomendado utilizar um virtual environment para isolar as dependências do projeto.

```bash
$ python -m venv mood_mesh_viewer_env
```

__Ative o virtual environment:__

_No Windows:_
```bash
$ mood_mesh_viewer_env\Scripts\activate
```

_No Linux/Mac:_
```bash
$ source mood_mesh_viewer_env/bin/activate
```

---

### 2. Instalação das Dependências:

Dentro do virtual environment, instale as bibliotecas necessárias:
```bash
$ pip install -r requirements.txt
```

---

### 3. Configuração do Projeto:

3.1. Clone ou faça o download do projeto para sua máquina local:

    3.1.1 Abra um terminal ou prompt de comando em seu computador.

    3.1.2 Navegue até o diretório onde deseja clonar o projeto usando o comando cd. Por exemplo:

    ```bash
    $ cd ~/Desktop
    ```

    3.1.3 Execute o comando `git clone` seguido do URL do projeto:

    ```bash
    $ git clone https://github.com/renan-siqueira/Mood-Mesh-Viewer-pt-BR.git
    ```

    3.1.4 Aguarde enquanto o Git clona o projeto em seu computador. Uma vez concluído, você verá uma nova pasta chamada "Mood-Mesh-Viewer" no diretório que escolheu.

    3.1.5 Navegue até a pasta do projeto clonado:

    ```bash
    $ cd Mood-Mesh-Viewer
    ```

    3.1.6 A partir daqui, você pode continuar com os passos de instalação e configuração conforme a documentação do projeto.

*__Lembre-se: você precisa ter o Git instalado em seu computador para executar esses comandos. Se ainda não tiver, pode baixá-lo e instalá-lo a partir do `[site oficial do Git](https://git-scm.com/)`.__*

3.2. Renomeie o arquivo `settings.example.py` para `settings.py`.

3.3. Atualize as variáveis no `settings.py`:

* `PATH_INPUT_DIR`: Especifique o diretório onde seu vídeo está armazenado.

* `VIDEO_NAME`: Especifique o nome do arquivo de vídeo (incluindo sua extensão).

* `PATH_MESSAGE_FILE`: Por padrão, ele está definido como 'messages.json'. Altere apenas se desejar usar um nome diferente.

* `PATH_EMOTION_TRANSLATION_FILE`: Por padrão, é 'emotion_translation.json'. Modifique se necessário.

* `DISPLAY_WIDTH` e `DISPLAY_HEIGHT`: Estes são os tamanhos da janela de exibição. Ajuste conforme a sua preferência.

3.4. Se desejar que as emoções sejam traduzidas para outro idioma, ajuste o arquivo `emotion_translation.json` de acordo.

3.5. Caso novas funcionalidades sejam implementadas ou se desejar modificar as teclas de atalho, atualize o arquivo `messages.json` para refletir essas mudanças.

---

### 4. Executando o Projeto:

Após ter configurado tudo corretamente, execute o arquivo `video_viewer.py`:

```bash
$ python video_viewer.py
```

Durante a execução, você pode:

Pressionar `H` para exibir/ocultar o menu de ajuda.
Pressionar `P` para pausar/reproduzir o vídeo.
Pressionar `Q` para fechar o vídeo.
Pressionar `K` para mostrar/ocultar pontos faciais.
Pressionar `E` para mostrar/ocultar emoções.

---

## Contribuições e Contato

__Mood-Mesh-Viewer__ é um projeto em evolução, e a sua contribuição pode ser essencial para torná-lo ainda melhor! 

Se você tiver ideias, correções ou novas funcionalidades que deseja adicionar, sinta-se à vontade para abrir um pull request ou registrar uma issue.

Se tiver dúvidas, sugestões ou quiser discutir mais sobre o projeto, entre em contato comigo através do meu __[linkedin](https://www.linkedin.com/in/renan-siqueira-antonio-9b587054/)__!

Acredito que, juntos, podemos melhorar e expandir a capacidade do __Mood-Mesh-Viewer__, tornando-o uma referência no campo da visão computacional. 

*__Seu feedback e expertise são inestimáveis para mim.__*
