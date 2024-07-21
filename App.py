#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import pickle as pk
import streamlit as st
import base64
import sklearn as sk
from streamlit.components.v1 import html

loaded_model = pk.load(open("C://Users//KRITHIKA//trained_model_lr.sav","rb"))
loaded_scaler= pk.load(open("C://Users//KRITHIKA//scaleddata.sav","rb"))



@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapercave.com/uwp/uwp4208901.jpeg");
background-size: 100%;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)











def input_converter(inp):
    vcl = ['Subcompact', 'Compact', 'Two-seater', 'Station wagon: Small',
       'Minicompact', 'Mid-size', 'Station wagon: Mid-size', 'Full-size',
       'Van: Cargo', 'Van: Passenger', 'Pickup truck: Standard',
       'Sport utility vehicle', 'Minivan', 'Pickup truck: Small',
       'Special purpose vehicle', 'Sport utility vehicle: Small',
       'Sport utility vehicle: Standard']
    trans = ['Automatic', 'Manual', 'Automatic with select shift', 'Continuously varible', 'Automated Manual']
    fuel = ['Regular gasoline', 'Premium gasoline', 'Diesel', 'Natural Gas', 'Ethanol(E85)']
    lst=[]
    for i in range(0,len(inp)):
        if (type(inp[i]) == str):
            if (inp[i] in vcl):
                lst.append(vcl.index(inp[i]))
            elif (inp[i] in trans):
                lst.append(trans.index(inp[i]))
            elif (inp[i] in fuel):
                if (fuel.index(inp[i]) == 0):
                    lst.extend([1, 0, 0, 0,0])
                    break
                elif (fuel.index(inp[i]) == 1):
                    lst.extend([0, 1, 0, 0,0])
                    break
                elif (fuel.index(inp[i]) == 2):
                    lst.extend([0, 0, 1, 0,0])
                    break
                elif (fuel.index(inp[i]) == 3):
                    lst.extend([0, 0, 0, 1,0])
                    break
                elif(fuel.index(trail_inputs[i]) == 4):
                    lst.extend([0,0,0,0,1])
                   

        else:
            lst.append(inp[i])

    arr = np.asarray(lst)
    arr = arr.reshape(1, -1)
    arr = loaded_scaler.transform(arr)
    prediction = loaded_model.predict(arr)

    return (f"The Fuel Consumption L/100km is {round(prediction[0], 2)}")

def main():
    
    #  title    
    
    st.markdown("<h1 style='text-align: center; color: white;'>Fuel Consumption Prediction</h1>", unsafe_allow_html=True)        
    # getting the input data from user    
    result = 0
    vehicle = [
    'Subcompact', 'Compact', 'Two-seater', 'Station wagon: Small',
    'Minicompact', 'Mid-size', 'Station wagon: Mid-size', 'Full-size',
    'Van: Cargo', 'Van: Passenger', 'Pickup truck: Standard',
    'Sport utility vehicle', 'Minivan', 'Pickup truck: Small',
    'Special purpose vehicle', 'Sport utility vehicle: Small',
    'Sport utility vehicle: Standard']


    transmission = ['Automatic', 'Manual', 'Automatic with select shift', 'Continuously varible', 'Automated Manual']
    fuel = ['Regular gasoline', 'Premium gasoline', 'Diesel', 'Natural Gas', 'Ethanol(E85)']
    lst=[]

    Vehicle_class = st.selectbox(label = "Enter Vehicle class",options = vehicle)
    
    css = """
        <style>
            .stSelectbox [data-testid='stMarkdownContainer'] {
                color: white;
            }
            
        </style>
    """

    st.write(css, unsafe_allow_html=True)
    
    
    Engine_size = st.selectbox("Select Engine Size (please enter value in this range[1-7])",options =[1,2,3,4,5,6,7])
    css = """
        <style>
           .stNumberInput [data-testid='stMarkdownContainer'] {
                color: white;
                
            }
            
        </style>
    """
    
    st.write(css, unsafe_allow_html=True)
    
    Cylinders = st.number_input("Enter number of Cylinders (please enter value in this range[1-16]",min_value = 1, max_value = 16)
    Transmission = st.selectbox("Select the Transmission",transmission)
    Co2_Rating = st.number_input("Enter CO2 Rating (please enter value in this range[1-10]",min_value = 1, max_value = 10)
    Fuel_type = st.selectbox("Select the Fuel type",fuel)

    # code for prediction

    # creating a button for prediction
    if st.button("Predict 🔍"):
        result = input_converter([Vehicle_class,Engine_size,Cylinders,Transmission,Co2_Rating,Fuel_type])
        markdown_text = f"<h2 style='color:white;'><b>{result}</b>!</h2>"
        st.markdown(markdown_text, unsafe_allow_html=True)

#     st.success(result)


if __name__ == "__main__":
    main()




