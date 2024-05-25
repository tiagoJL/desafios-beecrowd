def convertar_itens_da_lista_em_irracionais(
        entrada: list[str]) -> list[float]:
    
    return list(map(float, entrada))

entrada: list[str] = input().split()
todos: list[float] = convertar_itens_da_lista_em_irracionais(entrada)
A, B, C = sorted(todos)[::-1]

NAO_FORMA_TRIANGULO = A >= B+C
EH_TRIANGULO_RETANGULO = A**2 == (B**2 + C**2)
EH_TRIANGULO_OBTUSANGULO = A**2 > (B**2 + C**2)
EH_TRIANGULO_ACUTANGULO = A**2 < (B**2 + C**2)
EH_TRIANGULO_EQUILATERO = (A, A) == (B, C) 
EH_TRIANGULO_ISOSCELES =  not EH_TRIANGULO_EQUILATERO and len(set(todos)) == 2

if NAO_FORMA_TRIANGULO or EH_TRIANGULO_RETANGULO:
    print("NAO FORMA TRIANGULO") if NAO_FORMA_TRIANGULO else None
    print("TRIANGULO RETANGULO") if EH_TRIANGULO_RETANGULO else None
else:
    print("TRIANGULO OBTUSANGULO") if EH_TRIANGULO_OBTUSANGULO else None
    print("TRIANGULO ACUTANGULO") if EH_TRIANGULO_ACUTANGULO else None
    print("TRIANGULO EQUILATERO") if EH_TRIANGULO_EQUILATERO else None
    print("TRIANGULO ISOSCELES") if EH_TRIANGULO_ISOSCELES else None