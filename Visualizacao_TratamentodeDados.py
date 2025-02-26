#!/usr/bin/env python
# coding: utf-8

# ## Importando a biblioteca pandas

# In[1]:


get_ipython().system('pip install -q pandas==1.5.3 --user')


# In[2]:


import pandas as pd


# In[3]:


pd.__version__


# ## Abrindo o arquivo csv

# In[4]:


usinas_df = pd.read_csv("usina_termeletrica_tipo.csv")


# In[5]:


usinas_df.head()


# ## Exploração do arquivo

# In[6]:


# Tipo das variáveis em cada coluna
usinas_df.dtypes


# In[7]:


# Nome de cada coluna
usinas_df.columns


# In[8]:


# Valores vazios
usinas_df.isna().sum()


# In[9]:


# Formato
usinas_df.shape


# In[10]:


# Valores duplicados
usinas_df[usinas_df.duplicated()]


# ## Alterações

# In[11]:


# Renomeando as colunas
usinas_df.rename(columns = {'DatGeracaoConjuntoDados' : 'Data_Update',
                            'DscOrigem' : 'Origem',
                            'NomTipoUsina' : 'Segmento_Combustivel',
                            'NomSubTipoUsina': 'Combustivel',
                            'QtdUsinaTermeletrica' : 'Quantidade',
                            'MdaPotenciaInstaladaKW' : 'Potencia_KW',
                            'MesReferencia' : 'Mes',
                            'AnoReferencia' : 'Ano'}, 
                 inplace = True)


# In[12]:


usinas_df.head(1)


# In[13]:


import datetime as dt


# In[14]:


# Alterando o tipo da coluna para data
usinas_df['Data_Update'] = pd.to_datetime(usinas_df['Data_Update'], format= '%Y-%m-%d')


# In[15]:


usinas_df.dtypes


# In[16]:


# Verificando valores iguais digitados de forma diferente
for column in usinas_df:
    print(usinas_df[column].unique())


# In[17]:


# Uniformizando os valores nas colunas
usinas_df['Origem'] = usinas_df['Origem'].str.replace('Fossil', 'Fóssil')
usinas_df['Segmento_Combustivel'] = usinas_df['Segmento_Combustivel'].str.replace('Biocombustiveis Liquidos', 'Biocombustíveis líquidos')
usinas_df['Segmento_Combustivel'] = usinas_df['Segmento_Combustivel'].str.replace('Residuos animais', 'Resíduos animais')
usinas_df['Segmento_Combustivel'] = usinas_df['Segmento_Combustivel'].str.replace('Residuos solidos urbanos', 'Resíduos sólidos urbanos')
usinas_df['Segmento_Combustivel'] = usinas_df['Segmento_Combustivel'].str.replace('Gas Natural', 'Gás natural')
usinas_df['Segmento_Combustivel'] = usinas_df['Segmento_Combustivel'].str.replace('Outros fosseis', 'Outros Fósseis')
usinas_df['Segmento_Combustivel'] = usinas_df['Segmento_Combustivel'].str.replace('Petroleo', 'Petróleo')
usinas_df['Segmento_Combustivel'] = usinas_df['Segmento_Combustivel'].str.replace('Carvao mineral', 'Carvão mineral')
usinas_df['Combustivel'] = usinas_df['Combustivel'].str.replace('Biogás-AGR', 'Biogás - AGR')
usinas_df['Combustivel'] = usinas_df['Combustivel'].str.replace('Oleos Vegetais', 'Óleos Vegetais')
usinas_df['Combustivel'] = usinas_df['Combustivel'].str.replace('Óleos vegetais', 'Óleos Vegetais')
usinas_df.loc[(usinas_df['Segmento_Combustivel'] == 'Carvão mineral'), 'Origem'] = 'Fóssil'


# In[18]:


# Conferindo
for column in usinas_df:
    print(usinas_df[column].unique())


# In[19]:


# Versão final
usinas_df.head()


# In[20]:


# Salvando o arquivo csv no disco sem o index
usinas_df.to_csv(r'C:\Users\Usuario\CaminhodaPasta\usina_termeletrica_tipo2.csv', index = False)


# In[ ]:




