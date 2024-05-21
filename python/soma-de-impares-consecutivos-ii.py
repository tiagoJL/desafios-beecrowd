quantidade_de_testes = int(input("Quantidade de testes: "))

for vezes in range(quantidade_de_testes):
    entrada = input("Digite dois inteiros: ")
    primeiro_numero = int(entrada.split(" ")[0])
    segundo_numero = int(entrada.split(" ")[1])
    maior_numero = primeiro_numero if (primeiro_numero > segundo_numero) else segundo_numero
    menor_numero = primeiro_numero if (primeiro_numero < segundo_numero) else segundo_numero
    soma = 0
    
    for numero in range(menor_numero+1, maior_numero):
        numero_eh_impar = numero % 2 != 0
        soma += numero if numero_eh_impar else 0
    
    print(soma)