#!/usr/bin/env python
# coding: utf-8

# ## Importando bibliotecas úteis

# In[1]:


import pandas as pd
from sqlalchemy import create_engine
import sqlite3


# ## Abrindo o arquivo CSV em um DataFrame Pandas

# In[2]:


# Atribuindo o arquivo csv a um DataFrame
usinas_df1 = pd.read_csv("usina_termeletrica_tipo2.csv")
usinas_df1.head()


# ## Criando um BD sqlite

# In[3]:


# Criando o BD sqlite com uma conexão de database
con = sqlite3.connect("usinas.db")


# In[4]:


# Encerrando a Conexão
con.close()


# ## Criando uma Engine sqlalchemy

# In[5]:


usinas_engine = create_engine("sqlite:///usinas.db")


# ## Armazenando os dados do Dataframe no BD

# In[6]:


# Cria um tabela com nome 'usinas' usando a engine como conexão ao BD e sem carregar o índice do DataFrame
usinas_df1.to_sql('usinas', con=usinas_engine, if_exists = 'replace', index=False)


# ## Consulta

# In[7]:


# Conexão
con1 = sqlite3.connect("usinas.db")


# In[8]:


# Database cursor
cursor1 = con1.cursor()


# In[9]:


# Comando de pesquisa SQL, retorna todo o conteúdo da tabela
query1 = 'SELECT * FROM usinas'


# In[10]:


cursor1.execute(query1)


# In[11]:


# Atribuíndo o resultado da query a uma variável
dados_usinas = cursor1.fetchall()


# In[12]:


print(dados_usinas)


# ## Tranformando os dados para o DataFrame Pandas

# In[13]:


usinas_df1.columns


# In[14]:


# Transformando a variável em DataFrame, necessário especificar o nome das colunas, pois a query retorna apenas o conteúdo da tabela
df_query1 = pd.DataFrame(dados_usinas, columns = ['Data_Update', 'Origem', 'Segmento_Combustivel', 'Combustivel',
       'Quantidade', 'Potencia_KW', 'Mes', 'Ano'])


# In[15]:


df_query1.head(1)


# In[16]:


# Fechando o cursor e a conexão ao BD
cursor1.close()
con1.close()


# In[ ]:




