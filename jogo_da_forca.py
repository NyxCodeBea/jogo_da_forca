# --- 1. Configurações e Dados ---

banco_de_palavras = {
    1: "PYTHON",
    2: "DESAFIO",
    3: "ALGORITMO",
    4: "TECLADO",
    5: "INTERNET"
}

letra_digitada = []
palavra_secreta = None
letras_descobertas = []

# --- 1. Obter Dados com a Função def() ---

def obter_palavra_secreta():
    escolha = int(input("Escolha um número entre 1 e 5 para selecionar a palavra secreta: "))

    if escolha in banco_de_palavras:
        verificacao_escolha = banco_de_palavras.get(escolha)
        tamanho_palavra = len(verificacao_escolha)
        palavra_oculta = ["_"] * tamanho_palavra

        print("A palavra secreta tem", tamanho_palavra, "letras.")
        print(" ".join(palavra_oculta))
        return banco_de_palavras.get(escolha), palavra_oculta
    else:
        print("Número inválido. Por favor, escolha um número entre 1 e 5.")
        return None, None

def letras_usuario():
    letra = input("\n Digite uma letra: ").upper()
    return letra

# --- 3. Funções do Jogo com Menus interativos ---

print("\nBem-vindo ao Jogo da Forca!")

while True:
    
    verificacao = input("Digite I para iniciar o jogo ou S para sair: ").upper()

    if verificacao == "S":
        print("Obrigado encerrando! Até a próxima.")
        break
    elif verificacao == "I":
        while True:
            try:
                print("Menu: Escolher palavra secreta (1) ou Jogar (2) ou  Sair (3)?") 
                jogar = input("Escolha uma opção: ").upper()

                if jogar == "3":
                    print("Saindo do jogo da forca.")
                    break
                elif jogar == "1":
                    if palavra_secreta is not None:
                        print("Palavra secreta já escolhida.")
                    else: 
                        palavra_secreta,letras_descobertas = obter_palavra_secreta()
                        
                # --- 4. Jogo da Forca ---   
                elif jogar == "2": 
                    if palavra_secreta is None:
                        print("Por favor, escolha a palavra secreta primeiro (opção 1).")
                    else:
                        print("\nIniciando o jogo da forca...")
                        tentativas = 6
                        print(f"Você tem {tentativas} tentativas para descobrir a palavra secreta.")

                        while "_" in letras_descobertas:
                            print(" ".join(letras_descobertas))
                            letra_digitada = letras_usuario()

                            if letra_digitada in palavra_secreta:
                                print(f"Parabéns! A letra '{letra_digitada}' está na palavra secreta.")
                                for index, letra in enumerate(palavra_secreta):
                                    if letra == letra_digitada:
                                        letras_descobertas[index] = letra_digitada
                            else:
                                print(f"Que pena! A letra '{letra_digitada}' não está na palavra secreta.")
                                tentativas -= 1
                                if tentativas == 0:
                                    print("Você perdeu todas as suas tentativas! Fim de jogo.")
                                    print("A palavra secreta era:", palavra_secreta)
                                    break
                                else:
                                    print(f"Você tem {tentativas} tentativas restantes.")

                            if tentativas >= 1 and "_" not in letras_descobertas:
                                print("Parabéns! Você descobriu a palavra secreta:", palavra_secreta)    
                            palavra_secreta = None    
            except ValueError:
                print("Entrada inválida. Por favor, tente novamente.")                            
    else:
        print("Opção inválida. Por favor, digite S ou N.")