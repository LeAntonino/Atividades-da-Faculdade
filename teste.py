import main

listadenumeros = main.Lista()

# RETORNAR MEDIA
media = sum(listadenumeros)/len(listadenumeros)
media = round(media, 2)
print(f"Média: {media}")

# RETORNA O MAIOR VALOR

maior = max(listadenumeros)
print(f"Maior valor: {maior}")

# RETORNA O MENOR VALOR

menor = min(listadenumeros)
print(f"Menor valor: {menor}")

# RETORNA VALORES PARES

pares = [valor for valor in listadenumeros if  valor % 2 == 0]
pares = len(pares)
print(f"Quantidade de números pares: {pares}")


