"""
Exercício – Operações matemáticas básicas

Objetivo: Solicitar dois números inteiros e exibir diferentes operações
matemáticas entre eles, incluindo soma, subtração, multiplicação,
divisão, resto, potência, média geométrica e concatenação.
"""

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

print(
    f'Soma: {numero1 + numero2}\n'
    f'Subtração: {numero1 - numero2}\n'
    f'Multiplicação: {numero1 * numero2}\n'
    f'Divisão: {numero1 / numero2}\n'
    f'Resto: {numero1 % numero2}\n'
    f'Potência: {numero1 ** numero2}\n'
    f'Média geométrica: {(numero1 * numero2) ** 0.5}\n'
    f'Concatenação: {str(numero1) + str(numero2)}'
)