import random

cardapio = {
    "chocolate": 5.80,
    "baunilha": 4.50,
    "morango": 3.00,
    "flocos": 9.00
}

brindes = ["Canudo", "Copo Personalizado", "Gelo", "Badge"]

def mostrar_cardapio():
    print("-- CARDÁPIO --")
    for sabor, preco in cardapio.items():
        print(f"{sabor.title()}, R${preco}")

def fazer_pedido():
    total = 0
    pedido = []
    while True:
        sabor = input("\nEscolha o sabor: (Digite 'fechar' para sair)")
        if sabor == 'fechar':
            break
        elif sabor in cardapio:
            total += cardapio[sabor]
            pedido.append(sabor)
            print(f"{sabor} adicionado!")
        else:
            print("sabor não está no cardápio")

    return pedido, total