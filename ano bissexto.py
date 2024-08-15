ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:  '))
if ano % 4 and ano % 100 !=0 or ano % 400 == 0 :
    print(f'o ano {ano} é um ano bissexto.')
else:
    print(f'o ano {ano} NÃO é bissexto.')
