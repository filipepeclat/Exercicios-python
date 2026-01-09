"""
Exercício – Resumo financeiro mensal

Objetivo: Solicitar o salário do usuário e seus gastos mensais,
calculando o total de despesas, saldo restante,
percentual de gastos por categoria e o maior gasto do mês.
"""

salario = float(input('Digite seu salário atual: R$ '))

print('Informe seus gastos mensais em:')
moradia = float(input('Moradia R$ '))
alimentacao = float(input('Alimentação R$ '))
transporte = float(input('Transporte R$ '))
lazer = float(input('Lazer R$ '))
outros = float(input('Outros R$ '))

gastos_totais = moradia + alimentacao + transporte + lazer + outros
saldo_restante = salario - gastos_totais
maior_gasto = max(moradia, alimentacao, transporte, lazer, outros)

moradia_pct = (moradia / salario) * 100
alimentacao_pct = (alimentacao / salario) * 100
transporte_pct = (transporte / salario) * 100
lazer_pct = (lazer / salario) * 100
outros_pct = (outros / salario) * 100

print('--------------------------')
print('Resumo Financeiro do Mês:')
print('--------------------------\n')

print(
    f'Salário: R$ {salario:.2f}\n'
    f'Total de gastos: R$ {gastos_totais:.2f}\n'
    f'Saldo restante: R$ {saldo_restante:.2f}\n'
)

print(
    f'Percentuais:\n'
    f'- Moradia: {moradia_pct:.0f}%\n'
    f'- Alimentação: {alimentacao_pct:.0f}%\n'
    f'- Transporte: {transporte_pct:.0f}%\n'
    f'- Lazer: {lazer_pct:.0f}%\n'
    f'- Outros: {outros_pct:.0f}%'
)

print(f'\nMaior gasto do mês: R$ {maior_gasto:.2f}')