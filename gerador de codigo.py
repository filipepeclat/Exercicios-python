"""
Exercício – Gerador de código pessoal

Objetivo: Solicitar nome, sobrenome, ano de nascimento e ano atual,
gerando um código baseado em partes do nome e na idade do usuário.
"""

nome = input('Digite seu nome: ').strip()
sobrenome = input('Digite seu sobrenome: ').strip()
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_de_nascimento
codigo = nome[:3].upper() + sobrenome[-2:].upper() + str(idade)
print(codigo)