notas_validas = []

while len(notas_validas) < 2:
    nota = float(input())
    nota_valida = nota >= 0 and nota <= 10
    notas_validas.append(nota) if nota_valida else None
    print("nota invalida") if not nota_valida else None

media = sum(notas_validas) / len(notas_validas)

print(f'media = {media}')