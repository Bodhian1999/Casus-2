#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[ ]:


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


# In[ ]:


st.title('Welcome to our App 👋')


# In[ ]:


st.sidebar.success("Select a page above.")


# In[3]:


st.markdown(
"""
Welcome to our Application on the dataset consisting of the test score of different students on different subjects.

The Following subjects where tested: Mathematics, Reading and Writing.

**The dataset used in this project was retrieved from kaggle using the API. using the following code;**

!kaggle datasets download -d rkiattisak/student-performance-in-mathematics

!unzip student-performance-in-mathematics.zip
""")


# In[ ]:


st.write("### We hope you enjoy the application!")

