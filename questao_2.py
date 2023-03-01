print('Bem vindo a lanchonete do Carlos Eduardo silva De Oliveira')
print(' ' *3 ,12 * '*',      'cardapio', '*' * 13)
print(' ' * 2, '|código|', ' ' * 2,  '  Descrição', ' ' * 5, '|valor|')
print(' ' * 2, '|  100 |', ' ' , 'cachorro quente',     '   |9,00 |')
print(' ' * 2, '|  101 |'' cachorro quente duplo|11,00|')
print(' ' * 2, '|  102 |','       X-Egg         |12,00|')
print(' ' * 2, '|  103 |','     X-Salada        |12,00|')
print(' ' * 2, '|  104 |','      X-Bacon        |14,00|')
print(' ' * 2, '|  105 |','      X-Tudo         |17,00|')
print(' ' * 2, '|  200 |',' Refrigerante Lata   |5,00 |')
print(' ' * 2, '|  201 |','    Chá Gelado       |4,00 |')
# looping infinito que é quebrado caso o usuario nao ponha um codigo valido
while True:
  pedido = int(input('Entre com o codigo desejado! '))
  if(pedido != 100)\
          and (pedido != 101)\
          and (pedido != 102)\
          and (pedido != 103)\
          and (pedido != 104)\
          and (pedido != 105)\
          and (pedido != 200)\
          and (pedido != 201):
    print('Digite um codigo valido!') #se nao digitar um codigo valido essa mensagem aparecerá
    continue # continue para voltar a pergunta de codigo desejado
  if(pedido == 100):
    pedido = 9 # aqui sao os valores de cada pedido correspondente a seu codigo no cardapio
    print('você pediu um Cachorro Quente no valor de 9.00R$')
  if (pedido == 101):
    pedido = 11
    print('você pediu um Cachorro Quente Duplo no valor de 11.00 R$')
  if (pedido == 102):
    pedido = 12
    print('você pediu um X-Egg no valor de 12.00 R$')
  if (pedido == 103):
    pedido = 12
    print('você pediu um X-Salada no valor de 12.00 R$')
  if (pedido == 104):
    pedido = 14
    print('você pediu um X-Bacon no valor de 14.00 R$')
  if (pedido == 105):
    pedido = 17
    print('você pediu um X-Tudo no valor de 17.00 R$')
  if (pedido == 200):
    pedido = 5
    print('você pediu um Refrigerante Lata no valor de 5.00 R$')
  if (pedido == 201):
    pedido = 4
    print('você pediu um Chá Gelado no valor de 4.00 R$')
  opcao2 = input('Você deseja pedir mais alguma coisa? (1 para sim ou 2 para nao)')
  if(opcao2 != '1') and (opcao2 != '2'):# se usuario nao digitar 1 ou 2, o programa faz a pergunta novamente
    print('digite uma opcao valida')
    continue
  if(opcao2 == '2') and (pedido == 9):
    print('total a pagar 9.00 R$')
    break
  elif(opcao2 == '2') and (pedido == 11):
    print('total a pagar 11.00 R$')
    break
  elif (opcao2 == '2') and (pedido == 12):
    print('total a pagar 12.00 R$')
    break
  elif (opcao2 == '2') and (pedido == 12):
    print('total a pagar 12.00 R$')
    break
  elif (opcao2 == '2') and (pedido ==  14):
    print('total a pagar 11.00 R$')
    break
  elif (opcao2 == '2') and (pedido == 17):
    print('total a pagar 17.00 R$')
    break
  elif (opcao2 == '2') and (pedido == 5):
    print('total a pagar 5.00 R$')
    break
  elif (opcao2 == '2') and (pedido == 4):
    print('total a pagar 4.00 R$')
    break
  if(opcao2 == '1'):
    pedido2 = int(input('Digite aqui o codigo do produto desejado! '))
    if (pedido2 != 100) \
            and (pedido2 != 101) \
            and (pedido2 != 102) \
            and (pedido2 != 103) \
            and (pedido2 != 104) \
            and (pedido2 != 105) \
            and (pedido2 != 200) \
            and (pedido2 != 201):
      print('Digite um codigo valido e peça novamente os dois produtos')
      continue
    if (pedido2 == 100):
      pedido2 = 9
      print('Você pediu um cachorro quente no valor de 9.00 R$')
      print(f'valor total a pagar: {pedido + pedido2}.00 R$')# aqui o programa faz a soma dos dois pedidos
      break
    elif(pedido2 == 101):
      pedido2 = 11
      print('Vocé pediu um Cachorro Quente Duplo no valor de 11.00 R$')
      print(f'Valor total a pagar: {pedido + pedido2}.00 R$')
      break
    elif (pedido2 == 102):
      pedido2 = 12
      print('Você pediu um X-Egg no valor de 12.00 R$')
      print(f'Valor total a pagar: {pedido + pedido2}.00 R$')
      break
    elif (pedido2 == 103):
      pedido2 = 12
      print('Vocé pediu um X-Salada no valor de 12.00 R$')
      print(f'Valor total a pagar: {pedido + pedido2}.00 R$')
      break
    elif (pedido2 == 104):
      pedido2 = 14
      print('Vocé pediu um X-Bacon no valor de 14.00 R$')
      print(f'Valor total a pagar: {pedido + pedido2}.00 R$')
      break
    elif (pedido2 == 105):
      pedido2 = 17
      print('Vocé pediu um X-Tudo no valor de 17.00 R$')
      print(f'Valor total a pagar: {pedido + pedido2}.00 R$')
      break
    elif (pedido2 == 200):
      pedido2 = 5
      print('Vocé pediu um Refrigerante Lata no valor de 5.00 R$')
      print(f'Valor total a pagar: {pedido + pedido2}.00 R$')
      break
    elif (pedido2 == 201):
      pedido2 = 4
      print('Vocé pediu um Chá Gelado no valor de 4.00 R$')
      print(f'Valor total a pagar: {pedido + pedido2}.00 R$')
      break





