#!/usr/bin/env python
# coding: utf-8

# ### Comandos condicionais

# In[1]:


nome = input ("Digite seu nome de usuario : ")
senha = int(input("Digite sua senha para continuar : "))

if (senha == 12345):
    print ("Seja bem vindo", nome)
elif (senha == 0):
    print ("Ola ", nome, "foi enviado um email para você redefinir sua senha")
else:
    print ("Desculpe você digitou a senha errada, tente novamente")


# ### Comandos de iteração
# 

# In[2]:


i = 0
while (i< 5):
    print (i)
    i+=1

for i in range(5):
    print (i)


# ### Q1
# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.

# In[3]:


num1 = int(input("Digite o primeiro número (maior número): "))
num2 = int(input("Digite o segundo número  (menor número) : "))

while (num1 % num2 != 0) :
    num1, num2 = num2, num1 % num2

print ("Máximo divisor comum é:", num2)



# ### Q2
# 
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

# ### Q3
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
# 
# Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# 
# a. + Salário Bruto : R$
# 
# b. - IR (11%) : R$
# 
# c. - INSS (8%) : R$
# 
# d. - Sindicato ( 5%) : R$
# 
# e. = Salário Liquido : R$

# ### Q4
# Essa questão será colocada a resolução durante a semana
# 
# A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores Ex: F1= 1, F2 = 1, F3 = 2
# 
# F3 = F2 + F1. 
# 
# Faça um algoritmo que leia um número inteiro, calcule o seu número de Fibonacci.

# Próximos assuntos:
# 
# * Funções de strings
# * Funções
# * Variaveis locais e globais
# * Random
# * Arquivos
# * Leitura de arquivos
# * Objetos
# * Pandas

# In[ ]:




