"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'
    if par_impar:
        par_impar_texto = 'par'
    print('O numero {} é {}'.format(numero_int, par_impar_texto))
else:
    print('Você não digitou um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Digite a hora em numeros inteiros: ')
try:
    hora = int(entrada)
    if (hora >= 0) and (hora <= 11):
        print('Bom dia')
    elif (hora >= 12) and (hora <= 17):
        print('Boa tarde')
    elif (hora >= 12) and (hora <= 23):
        print('Boa noite')
except:
    print('Digite um numero inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""