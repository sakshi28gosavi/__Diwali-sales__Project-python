#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv(r"C:\Users\gosav\Downloads\Python_Diwali_Sales_Analysis-main (1)\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv",encoding= 'unicode_escape')


# In[6]:


df


# In[7]:


df.shape


# In[8]:


df.head()


# In[65]:


df.info()


# In[63]:


df.drop(['Status'],axis=1,inplace=True)


# In[64]:


df


# In[66]:


df.isna().sum()


# In[67]:


df.shape


# In[14]:


df.dropna()


# In[15]:


df.shape


# In[16]:


df["Amount"].dtypes


# In[17]:


df.columns


# In[18]:


df


# In[19]:


# use describe for specific columns
df[['Age','Orders','Amount']].describe()


# In[20]:


df['Amount'].dtypes


# In[21]:


df.dropna()


# In[22]:


df.rename(columns={'Marital_Status':'Shaadi'})


# In[23]:


df.describe() #display all the numerical values coloumns


# # Explotatory Data Analysis

# Gender

# In[24]:


ax= sns.countplot(x = 'Gender',edgecolor=('Black'),data = df)

for bars in ax.containers:
    ax.bar_label(bars)
    


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# Age
# 

# In[26]:


df.columns


# In[33]:


A= sns.countplot(data=df,x='Age Group')


# In[28]:


#use o hue= to seperat female and male values
A= sns.countplot(data=df,x='Age Group',hue='Gender')


# In[36]:


sales_age= df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending= False)
A= sns.barplot(data=sales_age,x='Age Group',y ='Amount')


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# # State

# In[14]:


#use .head(5) = then show 5 state
sales_state= df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending= False).head(10)

sns.set(rc={'figure.figsize':(20,7)})

az=sns.barplot(data=sales_state,x='State',y='Orders')

for bars in az.containers:
    az.bar_label(bars)


# In[18]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# # Marital Status

# In[43]:


b = sns.countplot(data=df,x ='Marital_Status')
sns.set(rc={'figure.figsize':(7,5)})

for bars in b.containers:
    b.bar_label(bars)


# In[59]:


sales_marital = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
b = sns.barplot(data=sales_marital,x ='Marital_Status',y='Amount',hue='Gender',edgecolor='black')



# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# # Occupation

# In[80]:


o = sns.countplot(data=df,x='Occupation')

sns.set(rc={'figure.figsize':(25,5)})

for bars in o.containers:
    o.bar_label(bars)


# In[97]:


sales_occu=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by ='Amount',ascending=False).head(10)
o = sns.barplot(data=sales_occu,x='Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[96]:


sns.set(rc={'figure.figsize':(25,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[94]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[98]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[ ]:


# also wright in this way


# In[99]:


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:

# 
# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:




