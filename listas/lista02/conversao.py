#!/usr/bin/env python
# coding: utf-8

# In[5]:


from datetime import datetime


# In[4]:


def conversao(data):
    data = datetime.strptime(data, '%d/%m/%Y')
    data_convertida=data.strftime('%d')+" "+data.strftime('%B')+" "+data.strftime('%Y')
    print("Data convertida ----->  "+data_convertida)
    


# In[8]:


def mainconver():
    cont=0
    #data=str(input("Digite uma data no seguinte formato DD/MM/AAAA\n"))
    #conversao(data)
    while cont==0:
        data=str(input("Digite uma data no seguinte formato DD/MM/AAAA\n\n\n"))
        try:
            conversao(data)
            cont=1
        except:
            print("\n\n\n*****insira a data corretamente DD/MM/AAAA*****\n\n")


# In[7]:


main()

