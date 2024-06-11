#!/usr/bin/env python
# coding: utf-8

# In[3]:


from fastapi import FastAPI
from pydantic import BaseModel
import joblib


# In[4]:


class InputData(BaseModel):
    input1:float
    input2:float
model=joblib.load('LinearModel.pkl')


# In[7]:


app=FastAPI()
@app.post('/predict/')
def predict(data: InputData):
    input_values=[[data.input1, data.input2]]
    prediction=model.predict(input_values)[0]
    
    return {'prediction':prediction}


# In[ ]:




