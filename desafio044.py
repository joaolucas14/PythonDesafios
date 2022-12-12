preco = float(input('Informe o preço do produto:'))
pag = str(input('Informe a forma de pagamento:'))
des = preco * 0.05
if pag.lower() == 'dinheiro':
    print('O valor do produto sairá com 5% de desconto de R${:.2f} por R$ {:.2f}'.format(preco, preco - des))
else:
    parcelas = int(input('Informe quantas parcelas:'))
    if parcelas <= 2:
        print('O valor total do produto será de R${:.2f}'.format(preco))
    else:
        print('O valor total terá um juros de 5% saindo de R${:.2f} por R${:.2f}'.format(preco, preco + des))
