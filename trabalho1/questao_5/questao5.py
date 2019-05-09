#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:09:13 2019

@author: thiagoalmeida
"""

import pylab as pl
import numpy as np
#%%

#Função de quarta ordem dada
def fa(p_n, p_n1, p_n2, p_n3, a):
    p_n4 = np.cos(p_n3 + p_n2 + p_n1 - p_n) + a
    return p_n4

#Equação relacionada
def fb(p_n, p_n1, p_n2, a):
    p_n4 = np.cos(p_n2 + p_n1 - p_n) + a
    return p_n4


#%%
    
precisao = np.float64

#Condições iniciais
condicoes_iniciais = np.array([-6.0, 1.0, 2.5, -3.0], precisao)

#Valores de a
valores_a = np.array([-2,-1,0,1,2], precisao)


#%%

#Configuração de execução do problema para a pergunta 1
n_steps = 200
a = 2.0

#Array de resultados (função de quarta ordem)
p = np.zeros([n_steps - len(condicoes_iniciais)], precisao)

#Array de resultados (equação relacionada)
q = np.zeros([n_steps - len(condicoes_iniciais)], precisao)

#preenche com condições iniciais
p = np.insert(p, 0, condicoes_iniciais)
q = np.insert(q, 0, condicoes_iniciais)
    
#iterador
for n in range(n_steps-4):
    p[n+4] = fa(p[n], p[n+1], p[n+2], p[n+3], a)
    q[n+4] = fb(q[n], q[n+1], q[n+2], a)


#plota resultados (função de quarta ordem)  
pl.figure(figsize=(8,5))
pl.plot(p, 'ro-', label='a = '+str(a))
pl.xlabel("$n$")
pl.ylabel("$p_n$")
pl.title(u"Função de Quarta Ordem")
pl.legend()
pl.savefig('q5_pergunta1_f4.png', dpi=100)
pl.show()


#plota resultados (equação relacionada)  
pl.figure(figsize=(8,5))
pl.plot(q, 'go-', label='a = '+str(a))
pl.xlabel("$n$")
pl.ylabel("$p_n$")
pl.title(u"Equação relacionada")
pl.legend()
pl.savefig('q5_pergunta1_er.png', dpi=100)
pl.show()


#%%

#Configuração de execução do problema para a pergunta 2
n_steps = 200

#listas que armazenam os arrays de resultados pra cada valor de a
p_list = []
q_list = []

#cria os arrays de resultados já com as condições iniciais e coloca
#eles na lista de armazenamento
for i in range(len(valores_a)):
    x = np.zeros([n_steps - len(condicoes_iniciais)], precisao)
    x = np.insert(x, 0, condicoes_iniciais)
    p_list.append(x)
    q_list.append(np.copy(x))
    
#percorre os valores de a
for i in range(len(valores_a)):
    #transfere o array da lista pra variavel local
    p = p_list[i]
    q = q_list[i]
    
    #transfere o valor de a pra variavel local
    a = valores_a[i]

    #iterador
    for n in range(n_steps-4):
        p[n+4] = fa(p[n], p[n+1], p[n+2], p[n+3], a)
        q[n+4] = fb(q[n], q[n+1], q[n+2], a)
        
    #plota resultados (função de quarta ordem)  
    pl.figure(figsize=(8,5))
    pl.plot(p, 'ro-', label='a = '+str(a))
    pl.xlabel("$n$")
    pl.ylabel("$p_n$")
    pl.title(u"Função de Quarta Ordem")
    pl.legend()
    pl.savefig('q5_pergunta2_f4_a='+str(a)+'_.png', dpi=100)
    pl.show()
    
    #plota resultados (equação relacionada)  
    pl.figure(figsize=(8,5))
    pl.plot(q, 'go-', label='a = '+str(a))
    pl.xlabel("$n$")
    pl.ylabel("$p_n$")
    pl.title(u"Equação relacionada")
    pl.legend()
    pl.savefig('q5_pergunta2_er_a='+str(a)+'_.png', dpi=100)
    pl.show()
        

#print(p_list)  