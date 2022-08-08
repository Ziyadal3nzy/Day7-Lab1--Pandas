#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd


# In[39]:


index = [1, 2, 3]
names = ['Ziyad', 'Sami', 'Waleed']
s = pd.Series(names, index=index)
s


# In[41]:


s.index = [11, 12, 13]
s


# In[42]:


s


# In[43]:


s[0:1]


# In[44]:


s.drop_duplicates()


# In[52]:


s.drop_duplicates()


# In[54]:


data = {'ID': [111, 222, 333],
        'Names': ['Ziyad', 'Sami', 'Waleed']}


Students = pd.DataFrame(data, columns=['ID', 'Names'])
Students 


# In[57]:


edu = pd.read_csv('/Users/Ziyad/Desktop/educ_figdp_1_Data.csv')
edu


# In[58]:


edu.loc[90:94, ['INDIC_ED', 'Value']]


# In[62]:


edu['Value'][90] 
edu


# In[ ]:





# In[ ]:




