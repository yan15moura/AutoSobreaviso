#!/usr/bin/env python
# coding: utf-8

# In[22]:


import calendar
from datetime import date
import holidays
import pandas as pd


# In[14]:


def troca(lista):
    temp = lista[0]
    lista[0] = lista[1]
    lista[1] = temp
    temp = lista[2]
    lista[2] = lista[3]
    lista[3] = temp
    return lista


# In[15]:


func = ['Jeffrey','Yan','Luiz','Bruna']


# In[19]:


func = troca(func)


# In[20]:


print(func)


# In[9]:


feriados = holidays.Brazil()


# In[12]:


for feriado in feriados['2022-01-01': '2022-12-31'] :
    print(feriado)


# In[36]:





# In[39]:





# In[38]:


calendar.weekday(2022,6,10)


# In[40]:





# In[60]:


from datetime import datetime, timedelta, date

dt_inicio =  date.today()
dt_fim =  datetime.strptime('21/12/2023 00:00', "%d/%m/%Y %H:%M").date()
dt = dt_inicio
while dt <= dt_fim:
    ano = int(dt.strftime("%Y"))
    mes = int(dt.strftime("%m"))
    dia = int(dt.strftime("%d"))
    d = datetime(ano, mes, dia);
    if dt.strftime("%d/%m/%Y")
    if d.weekday() > 4:
        print('Given date is weekend.')
    else:
        print ('Given data is weekday.')
    dt += timedelta(days=1)


# In[57]:


from datetime import datetime
d = datetime(2020, 12, 25);
if d.weekday() > 4:
    print('Given date is weekend.')
else:
    print ('Given data is weekday.')


# In[47]:





# In[66]:


if feriados.get('2014-01-03')
    print("é falso")
else:
    print(1)


# In[ ]:




