from math import sqrt

def calcular_bhaskara(a: float, b: float, c: float) -> str:
    delta = (b**2 - 4 * a * c)
    delta_positivo_ou_neutro = delta >= 0
    variavel_a_eh_zero = a == 0
    if not delta_positivo_ou_neutro or variavel_a_eh_zero:
        return "Impossivel calcular"
        
    r1 = (-b + sqrt(delta)) / (2 * a)
    r2 = (-b - sqrt(delta)) / (2 * a)
    
    return f"R1 = {r1:.5f}\nR2 = {r2:.5f}"
    
    
a, b, c = input("").split(" ")
resultado = calcular_bhaskara(float(a), float(b), float(c))
print(resultado)