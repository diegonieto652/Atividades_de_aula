# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def titulo(txt):
    print('*'*30)
    print(txt)
    print('*'*30)

def diferenca(a,b):
    s = (a - b)
    print(f'o preço aumentou R${s:.2f}')


titulo('''Frutas disponíveis
Banana
Melancia''')

fruta = input('digite a fruta: ')

if fruta == 'Banana':
    print('fruta na lista')
    prec_ant = float(input('digite o preço anterior: '))
    prec_atual = float(input('digite o preço atual: '))

    if prec_atual > prec_ant:
        diferenca(prec_atual, prec_ant)
    elif prec_ant > prec_atual:
        diferenca(prec_ant, prec_atual)
    else:
        print("valores iguais")

elif fruta == 'Melancia':
    print('fruta na lista')
    prec_ant = float(input('digite o preço anterior: '))
    prec_atual = float(input('digite o preço atual: '))

    if prec_atual > prec_ant:
        diferenca(prec_atual,prec_ant)
    elif prec_ant > prec_atual:
        diferenca(prec_ant,prec_atual)
    else:
        print("valores iguais")


else:
    print('fruta fora da lista')


