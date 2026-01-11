#Exercícios básicos de condicionais (if / elif / else)

# =====================================================
# Exercício 1 — Verificar se um número é par ou ímpar
# =====================================================

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")


# =====================================================
# Exercício 2 — Classificação por idade
# =====================================================

idade = int(input("\nDigite sua idade: "))

if idade <= 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")


# =====================================================
# Exercício 3 — Verificação de senha
# =====================================================

import os

senha = int(input("\nCadastre uma senha: "))
print("Senha cadastrada com sucesso!")

input("\nPressione ENTER para continuar...")
os.system("cls")

senha_digitada = int(input("Digite sua senha: "))

if senha_digitada == senha:
    print("Acesso permitido")
else:
    print("Acesso negado")


# =====================================================
# Exercício 4 — Identificação de quadrante no plano cartesiano
# =====================================================

coordenada_x = float(input("\nDigite a coordenada X: "))
coordenada_y = float(input("Digite a coordenada Y: "))

if coordenada_x > 0 and coordenada_y > 0:
    print("Primeiro Quadrante")
elif coordenada_x < 0 and coordenada_y > 0:
    print("Segundo Quadrante")
elif coordenada_x < 0 and coordenada_y < 0:
    print("Terceiro Quadrante")
elif coordenada_x > 0 and coordenada_y < 0:
    print("Quarto Quadrante")
else:
    print("Origem")
