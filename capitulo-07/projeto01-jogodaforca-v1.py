# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows
    if name == 'nt':
      _  = system('cls')

    # Mac ou Linux
    else:
      _  = system('clear')


# Função
def game():
   
    limpa_tela()
    print("\nBem vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")
    import random
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolhe aleatoriamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []

    while chances > 0:
      
        # Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras Erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()


        # Condicional
        if tentativa in palavra and tentativa not in letras_descobertas:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        elif tentativa in letras_descobertas or tentativa in letras_erradas:
            print("\nLetra já digitada! Digite outra.")
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)
    
# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns, você está aprendendo programação Python pela DSA.")
    