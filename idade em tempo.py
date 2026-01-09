"""
Exercício – Conversão de idade em tempo

Objetivo: Solicitar a idade do usuário e calcular aproximadamente
quantos dias, horas, minutos e segundos ele já viveu.
"""

idade = int(input('Digite sua idade: '))
dias = idade * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print(f'\nvocê tem {idade} anos, sendo assim viveu aproximadamente: ')
print(f'{dias:,} dias'.replace(',', '.'))
print(f'{horas:,} horas'.replace(',', '.'))
print(f'{minutos:,} minutos'.replace(',', '.'))
print(f'{segundos:,} segundos'.replace(',', '.'))