pesos = input("¿Cuántos pesos dominicanos tienes? ")
pesos = float(pesos)
valor_dolar = 55.3
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")