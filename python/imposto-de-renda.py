# -*- coding: utf-8 -*-

salario = float(input(""))

resultado_imposto_de_renda = 0
faixa_isenta = 2000
teto_um = 3000 
teto_dois = 4500
faixa_um = salario > faixa_isenta and salario <= teto_um
faixa_dois = salario > teto_um and salario <= teto_dois
faixa_tres = salario > teto_dois
taxa_faixa_um = 0.08
taxa_faixa_dois = 0.18
taxa_faixa_tres = 0.28
taxacao_faixa_um = (salario - faixa_isenta) * taxa_faixa_um 
taxacao_faixa_dois = 80 + (salario - teto_um) * taxa_faixa_dois
taxacao_faixa_tres = 350 + (salario - teto_dois) * taxa_faixa_tres

if faixa_um:
    resultado_imposto_de_renda = taxacao_faixa_um
    
if faixa_dois:
    resultado_imposto_de_renda = taxacao_faixa_dois
if faixa_tres:
    resultado_imposto_de_renda = taxacao_faixa_tres

if resultado_imposto_de_renda > 0:
    print(f"R$ {resultado_imposto_de_renda:.2f}")
else:
    print("Isento")