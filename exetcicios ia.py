'''idade = int(input('Digite sua idade: '))
dias = idade * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print(f'\nvocê tem {idade} anos, sendo assim viveu aproximadamente: ')
print(f'{dias:,} dias'.replace(',', '.'))
print(f'{horas:,} horas'.replace(',', '.'))
print(f'{minutos:,} minutos'.replace(',', '.'))
print(f'{segundos:,} segundos'.replace(',', '.'))'''

'''nome = input('Digite seu nome: ').strip()
sobrenome = input('Digite seu sobrenome: ').strip()
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_de_nascimento
codigo = nome[:3].upper() + sobrenome[-2:].upper() + str(idade)
print(codigo)'''

'''preço1 = float(input('Digite o preço do produto: R$ '))
desconto1 = float(input('Digite a porcentagem de desconto: '))
valor_descontado1 = (preço1 * desconto1) / 100
valor_final1 = preço1 - valor_descontado1

preço2 = float(input('Digite o preço do produto: R$ '))
desconto2 = float(input('Digite a porcentagem de desconto: '))
valor_descontado2 = (preço2 * desconto2) / 100
valor_final2 = preço2 - valor_descontado2

print (f'Os valores com desconto são R$ R${valor_final1} e R${valor_final2}')'''

'''numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print (f'Soma: {numero1 + numero2} \nSubtração: {numero1 - numero2} \nMultiplicação: {numero1 * numero2} \nDivisão: {numero1 / numero2} \nResto:{numero1 % numero2} \nPotencia: {numero1 ** numero2} \nmédia geométrica: {(numero1 * numero2) ** 0.5} \nconcatenação: {str(numero1) + str(numero2)}')'''

salario = float(input('Digite seu salário atual: R$ '))
print('Informe seus gastos mensais em:')
moradia = float(input('Moradia R$ '))
alimentação = float(input('Alimentação R$ '))
transporte = float(input('Transporte R$ '))
lazer = float(input('Lazer R$ '))
outros = float(input('Outros R$ '))

gatos_toais = (moradia + alimentação + transporte + lazer + outros)
resto_salario = salario - gatos_toais
maior_gasto = max(moradia, alimentação, transporte, lazer, outros)

moradia_porcentagem = (moradia / salario) * 100
alimentação_porcentagem = (alimentação / salario) * 100
transporte_porcentagem = (transporte / salario) * 100
lazer_porcentagem = (lazer / salario) * 100
outros_porcentagem = (outros / salario) * 100

print ('--------------------------')
print ('Resumo Financeiro do Mês:')
print ('--------------------------\n')
print (f'Salário: R$ {salario:.2f}'
       f'\nTotal de gastos: R$ {gatos_toais:.2f}'
       f'\nSaldo restante: R$ {resto_salario:.2f}\n'
       )
print (f'Percentuais:'
       f'\n- Moradia: {moradia_porcentagem:.0f}%'
       f'\n- Alimentação: {alimentação_porcentagem:.0f}%'
       f'\n- Transporte: {transporte_porcentagem:.0f}%'
       f'\n- Lazer: {lazer_porcentagem:.0f}%'
       f'\n- Outros: {outros_porcentagem:.0f}%'
       )
print (f'\nMaior gasto do mês: {maior_gasto}')