"""
Exercício – Cálculo de desconto em produtos

Objetivo: Solicitar o preço e a porcentagem de desconto de dois produtos
e exibir os valores finais com desconto aplicado.
"""

preço1 = float(input('Digite o preço do produto: R$ '))
desconto1 = float(input('Digite a porcentagem de desconto: '))
valor_descontado1 = (preço1 * desconto1) / 100
valor_final1 = preço1 - valor_descontado1

preço2 = float(input('Digite o preço do produto: R$ '))
desconto2 = float(input('Digite a porcentagem de desconto: '))
valor_descontado2 = (preço2 * desconto2) / 100
valor_final2 = preço2 - valor_descontado2

print (f'Os valores com desconto são R$ R${valor_final1} e R${valor_final2}')
