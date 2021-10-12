#!/usr/bin/env python
# coding: utf-8

# Import Liberie e import dataset 

# In[115]:


import pandas as pd
import numpy as np
import os
    


# In[116]:


dati_ambientali = pd.read_csv('nuovoETSDBv38.csv',sep =";")
# guardo la coda 
dati_ambientali.tail()


# Basic Structure of DataFrame

# In[117]:


dati_ambientali.info()
#inzio ad inoltrarmi nel DataFrame per riconoscere qualche quali colonne ci sono, di che tipo sono e in che quantità


# In[183]:





# In[ ]:


#dalla tail precedente mi sono accorto che ho degli intervalli di anni.
#elimino  i periodi che sono soltanto una somma di tutti gli anni presenti nell'intervallo.

df = df.drop(df[df.year == 'Total 1st trading period (05-07)'].index)
df = df.drop(df[df.year == 'Total 2nd trading period (08-12)'].index)
df = df.drop(df[df.year == 'Total 3rd trading period (13-20)'].index)

#trasformo l'anno in un intero 

df['year'].astype(str).astype(int)


# In[185]:


#selezione per ispezionare meglio i dati 
dati_ambientali[['country','main activity sector name','value']]
#nella tabella sono presenti quindi il paese , il modo in cui viene prodotta la CO2 e quante tonnellate in quel settore vengono registrate.


# In[130]:


#filtraggio
df = dati_ambientali

dati_belgio = df.loc[((df.country == 'Belgium') & (df.value > 900000))]
dati_belgio.info()
dati_belgio.head(10)

#un pò di informazioni sulla tabella ricavata dal filtraggio  dove il paese è il Belgio e il valore delle tonnellate di CO2 supera le 900000 tonnellate


# In[175]:


# tutte i valori di value sono tutti in Tonnellate di CO2
df_new.unit.value_counts()


# STATISTICHE NUMERICHE :
# Media / Mediana / diffusione e disperisione dati / 
# Range / Percentile /Varianza
# 

# In[131]:


df.describe()
#ci dà una descrizione veloce del dataFrame con le varie statisticeh riassuntive


# In[132]:


print("la media è : {0} ".format(df.value.mean()))
print("la mediaana è : {0} ".format(df.value.median()))


# In[133]:


print("Il range è : {0} ".format(df.value.max() - df.value.min()))
print("25 percentile : {0} ".format(df.value.quantile(.25)))
print("50 percentile : {0} ".format(df.value.quantile(.50)))
print("75 percentile : {0} ".format(df.value.quantile(.75)))
print("La deviazione standard è : {0} ".format(df.value.std()))
print("La varianza è : {0} ".format(df.value.var()))



# Visualizzazione delle statistiche.

# In[135]:


df.value.plot(kind='box')


# STATISTICHEPER LE CATEGORIE: 
# 

# In[136]:


df.describe(include = 'all')
# count conteggio, unique conteggio unico ,top la maggior parte di quello che è stato usato,


# In[137]:


#df["ETS information"].value_counts()

#oppure per la proporzione eseguire 

df["ETS information"].value_counts(normalize=True)

df['year'].value_counts(normalize=True)


# In[138]:


df["ETS information"].value_counts().plot(kind='bar',title='Utilizzo classi ETS information',color = 'c')


# RAGGRUPPAMENTO : 
#     HIST / 
#     KDE / 
#     SCATTER PLOT / 

# In[252]:


df.year.plot(kind='hist',title="Istogramma per gli anni", color = "b",xlim=[2008,2020],edgecolor='black',linewidth=1.2)

#df.value.plot(kind='hist',title="Istogramma per i valori", color = "b",xlim = [-10000000000000000,10000000000000000],edgecolor='black',linewidth=1.2)


# In[140]:


new_df = pd.qcut(df.value, 5 , labels=['very_low','low','medium','high','very_high']).value_counts().plot(kind='bar',color='c',rot = 0);
#ho discretizzato per avere un idea migliore  

#insomma la fascia in cui ci sono più valori è 'very_low' forse perchè c'è una grande presenza di 0 e quindi di valori esterni


# In[141]:


df.plot.scatter(x="value",y="ETS information",color = "c",title="scatter plot valore paesi",alpha=0.5)


# RAGGRUPPAMENTO O AGGREGAZIONE
#     

# In[142]:


df.groupby(['country'])['value'].mean()


# CROSS TAB / PIVOTING

# In[143]:


pd.crosstab(df["ETS information"],df["country"])


# In[144]:


pd.crosstab(df["ETS information"],df["country"]).plot(kind="bar")


# In[145]:


# tabella pivot 
df.pivot_table(index='country', columns='ETS information', values='value',aggfunc='median')


# DATA MUNGING : LAVORARE CON I DATI MANCANTI
# 

# In[146]:


df.info()


# In[147]:


#abbiamo valore mancanti in value prima di tutto estraiamo le righe con i valori mancanti
df[df.value.isnull()]


# In[148]:


df["value"].value_counts()


# In[149]:


df["value"].fillna(df['value'].mean(),inplace=True)


# In[150]:


df[df['value'].isnull()]


# In[151]:


df.info()
##abbiamo risolto il problema dei valori mancanti grazie a fillna


# FUTURE ENGINEERING

# In[152]:


df['year'].value_counts()


# In[153]:





# In[154]:


df.info()

#questo è il dataset pulito dai periodi 


# In[159]:


df['year']=df['year'].astype(str).astype(int)
df.info()


# FEATURE ENGINEERING 

# In[160]:


df['yearState'] = np.where(df['year'] >= 2011, '1','2')


# In[161]:


df['yearState'].value_counts()


# In[165]:


pd.crosstab(df['main activity sector name'], df['yearState'])


# In[169]:


#creo un nuovo df con la codifica della variabile categorica ETS information 

df_new = pd.get_dummies(df,columns =['ETS information'])


# ESEMPI DI VISUALIZZAZIONE

# In[179]:


import matplotlib.pyplot as plt
plt.hist(df.value,bins=20,color='c')
plt.title("Value Histogram")
plt.xlabel('bins')
plt.ylabel('value')
plt.show()


# In[181]:


f,(ax1,ax2 ) = plt.subplots(1,2,figsize=(14,3))

ax1.hist(df.value,bins=20,color='c')
ax1.set_title('Histogram : value')

ax2.hist(df.year,bins=10,color='tomato')
ax2.set_title('Histogram : year')


plt.show()


# In[ ]:




