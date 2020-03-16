#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Necessary imports and file imports

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/Michele/Downloads/winwinewine/winemag-data-130k-v2.csv')
df.head()

# Some pre-processing and feature engineering will be required in order to make good predictions.
# What do we do with empty's or NaN's? I would rather not drop those wines entirely unless we have no price maybe?
# description should be dropped? Taster_twitter_handle drop?  
# Year of the wine is for sure an important aspect of the price because of the harvest. We should try to extract the year from the title?
# E.g. country,designation,province,region_1,region_2,taster_name, needs to be transformed 


# In[23]:


labels = list(df.columns.values)

for label in labels:
    print(df[label].value_counts())
    


# In[37]:


data = df[['price','title']]
#print(data)
  
df = pd.DataFrame(data,columns=['price','title'])
print (df.info)

#df.drop_duplicates()
#print('dataframe without duplicates: ',df.info)
# --> there are no duplicates

titles = df['title'][:100]
prices = df['price'][:100]


# In[39]:


# i only printed the first 100 prices and titles of wines, because we have 130k datapoints. We will need to aggregate
# / group somehow first before we can show something that makes sense :) 

plt.subplot()
plt.scatter(titles, prices)
plt.show()


# In[ ]:




