import random

cardapio = {
    "chocolate": 5.80,
    "baunilha": 4.50,
    "morango": 3.00,
    "flocos": 9.00
}

brindes = ["Canudo", "Copo Personalizado", "Gelo", "Badge"]

def mostrar_cardapio():
    print("-- CARDAPIO --")
    for sabor, preco in cardapio.items():
        