"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes

print(nome1)

nomes = ['Maria', 'Helena', 'Luiz']

nome1, *resto = nomes

print(nome1, resto)
