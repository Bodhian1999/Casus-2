#!/usr/bin/env python
# coding: utf-8

# In[40]:


#import kaggle
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
#import seaborn as sns
#import matplotlib.pyplot as plt


# In[41]:


#!kaggle datasets download -d rkiattisak/student-performance-in-mathematics
#!unzip student-performance-in-mathematics.zip


# In[42]:


df = pd.read_csv('Student performance in mathematics.csv')


# In[81]:


#df


# In[75]:


df.describe()


# In[45]:


df['Average score'] = ((df['Math score'] + df['Reading score'] + df['Writing score']) / 3).round(1)


# In[ ]:





# In[96]:


fig_1 = px.scatter(df,  x='Writing score', y='Reading score' ,color = 'Race/ethnicity', symbol='Gender', hover_name ='Student ID', hover_data=['Average score'])
fig_2 = px.scatter(df,  x='Reading score', y='Math score' ,color = 'Race/ethnicity', symbol='Gender', hover_name ='Student ID', hover_data=['Average score'])
fig_3 = px.scatter(df,  x='Writing score', y='Math score' ,color = 'Race/ethnicity', symbol='Gender', hover_name ='Student ID', hover_data=['Average score'])

#fig_1.show()
#fig_2.show()
#fig_3.show()


# In[101]:


#df.to_csv('Student performance in mathematics.csv')


# In[102]:


st.title("Student test scores per subject")


# In[103]:


st.text("This analysis will show us the correlations between all the different subjects and their results")


# In[104]:


#st.plotly_chart(fig_1)
#st.plotly_chart(fig_2)
#st.plotly_chart(fig_3)


# In[105]:


option = st.selectbox("Which Graph would you like to view?", ["Writing vs Reading","Math vs Reading","Writing vs Math"])

if "Writing vs Reading" in option: 
    writing_reading = st.plotly_chart(fig_1)
elif "Math vs Reading" in option:
    math_reading = st.plotly_chart(fig_2)
elif "Writing vs Math" in option:
    writing_math = st.plotly_chart(fig_3)


# In[107]:


fig_4 = px.histogram(df, x ='Average score', color='Gender')
fig_5 = px.histogram(df, x ='Average score', color='Lunch')
fig_6 = px.histogram(df, x ='Average score', color='Test preparation course')

#fig_4.show()
#fig_5.show()
#fig_6.show()


# In[86]:


#df


# In[ ]:


option_2 = st.selectbox("Comparing Average test scores to different personal factors", 
                        ["Average score by Gender","Average score by Lunch","Average score by Test Preperation"])

if "Average score by Gender" in option_2: 
    writing_reading = st.plotly_chart(fig_4)
elif "Average score by Lunch" in option_2:
    math_reading = st.plotly_chart(fig_5)
elif "Average score by Test Preperation" in option_2:
    writing_math = st.plotly_chart(fig_6)

