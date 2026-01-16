# 😵 Jogo da Forca

![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)

## 📝 Descrição

Este é um **Jogo da Forca** desenvolvido em **Python 3**, rodando diretamente no terminal. O projeto foi construído com foco em lógica de programação estruturada, modularização e tratamento de erros (blindagem contra entradas inválidas).

O diferencial desta versão é a implementação de uma **Máquina de Estados**, que impede o jogador de iniciar a partida sem antes selecionar uma palavra, garantindo o fluxo lógico correto.

## 🚀 Funcionalidades

- **Menu Interativo:** Sistema de navegação numérica (1. Escolher, 2. Jogar, 3. Sair).
- **Banco de Palavras:** Seleção de palavras ligadas a tecnologia (ex: PYTHON, ALGORITMO).
- **Validação de Entradas:**
  - Uso de `try/except` para capturar erros quando o usuário digita letras no lugar de números.
  - Verificação se o número escolhido existe no dicionário.
- **Sistema de Vidas:** O jogador começa com 6 tentativas.
- **Proteção de Fluxo:**
  - Bloqueia a opção "Jogar" se a palavra ainda não foi escolhida.
  - Bloqueia a opção "Escolher Palavra" se já existir uma palavra ativa.
- **Reset Automático:** Ao fim da partida (vitória ou derrota), o jogo reseta a palavra secreta para permitir uma nova rodada limpa.

## 💻 Tecnologias Utilizadas

- **Python 3**: Lógica completa do jogo.
- **Estruturas de Dados**: Listas (`list`) e Dicionários (`dict`).

## 📂 Como Executar o Projeto

### Pré-requisitos

Você precisa ter o **Python** instalado em sua máquina.

### Passo a passo

1. Clone este repositório:
```bash
git clone https://github.com/NyxCodeBea/jogo_da_forca.git/


```

2. Acesse a pasta do projeto e execute o arquivo:

```bash
python nome_do_arquivo.py

```

## 🎮 Como Jogar

1. Ao iniciar, digite **I** para entrar no menu principal.
2. Escolha a **Opção 1** e digite um número de 1 a 5 para carregar uma palavra secreta.
3. Escolha a **Opção 2** para começar a adivinhar.
4. Digite uma letra por vez. Se errar, perde uma vida. Se as vidas chegarem a 0, é Game Over!

---
