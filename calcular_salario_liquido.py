'''
Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
Salário bruto
Quanto pagou ao INSS.
Quanto pagou ao sindicato.
O salário líquido.

Calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$
IR (11%) : R$
INSS (8%) : R$
Sindicato ( 5%) : R$
Salário Liquido : R$
'''



salario_hora = float(input("Quanto você ganha por hora? "))
qnt_hora_mes = int(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = salario_hora * qnt_hora_mes
ir = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - ir - inss - sindicato



print(f"Salário bruto: R$ {salario_bruto}")
print(f"IR: R$ {ir:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"Sindicato: R$ {sindicato:.2f}")
print(f"O salário líquido é de R$ {salario_liquido:.2f}")

