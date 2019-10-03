#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[64]:


def retangulo(linhas,colunas):
    colunass=int(round(linhas/2))-1
    linhass=int(round(colunas/2))+1
    matrix=np.zeros((linhas,colunas), dtype=np.unicode_)
    for i in range(0,linhas):
        for y in range(0,colunas):
            matrix[i][y]=" "
            matrix[i][0]="|"
            matrix[i][colunas-1]="|"
            matrix[0][y]="-"
            matrix[linhas-1][y]="_"
    
    
    #print("Escrever------>  "+str(linhass))
    #print("Escrever------>  "+str(colunass))
    
    matrix[colunass][linhass-3]="O"
    matrix[colunass][linhass-2]="I"
    matrix[colunass][linhass-1]=" "
    matrix[colunass][linhass]="R"
    matrix[colunass][linhass+1]="s"
    
    print(matrix)        
        


# In[2]:


def maindes():
    try:
        linhas=int(input("Digite a largura do retângulo\n"))
        colunas=int(input("Digite a altura do retângulo\n\n"))

        if linhas > 20:
            linhas=20
            print("A quantidade de linhas foi alterada para 20 pos o valor máximo foi atingido!\n\n")
        elif linhas<1:
            linhas=1
            print("A quantidade de linhas foi alterada para 1 pos o valor mínimo não foi atingido!\n\n")

        if colunas > 20:
            colunas=20
            print("A quantidade de linhas foi alterada para 20 pos o valor máximo foi atingido!\n\n")
        elif colunas<1:
            colunas=1
            print("A quantidade de linhas foi alterada para 1 pos o valor mínimo não foi atingido!\n\n")

        retangulo(linhas,colunas)
    except:
        print("Digita direito ae porra!")

