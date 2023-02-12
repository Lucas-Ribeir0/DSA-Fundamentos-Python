# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

def soma(x, y):
    print(f"A soma entre os números {x} e {y} é de {x + y}")


def subtracao(x, y):
    print(f"A subtração entre os números {x} e {y} é de {x - y}")


def multiplicacao(x, y):
    print(f"A multiplicação entre os números {x} e {y} é de {x * y}")


def divisao(x, y):
    print(f"A divisão entre os números {x} e {y} é de {x / y}")


print("\n******************* Calculadora em Python *******************")

escolha = int(input("Seja bem-vindo a calculadora básica em Python!\n\n Escolha o modo de cálculo: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n\n Faça sua escolha: "))

# if escolha == 1:
#     x = float(input("Digite o primeiro número: "))
#     y = float(input("Digite o segundo número: "))

#     soma(x, y)

# elif escolha == 2:
#     x = float(input("Digite o primeiro número: "))
#     y = float(input("Digite o segundo número: "))

#     subtracao(x, y)

# elif escolha == 3:
#     x = float(input("Digite o primeiro número: "))
#     y = float(input("Digite o segundo número: "))

#     multiplicacao(x, y)

# elif escolha == 4:
#     x = float(input("Digite o primeiro número: "))
#     y = float(input("Digite o segundo número: "))

#     divisao(x, y)

# else:
#     print("Opção inválida! Tente novamente!")

  match escolha:
       case 1:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))

            soma(x, y)

        case 2:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))

            subtracao(x, y)

        case 3:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))

            multiplicacao(x, y)

        case 4:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))

            divisao(x, y)

        case _:
            print("Opção inválida! Tente Novamente")
