'''Python file for creating streamlit website'''

import streamlit as st
import pickle
import numpy as np
import sklearn

with open('diamond.pickle', mode='rb') as model_file:
    model = pickle.load(model_file)

def predict_price(carat, depth, table, x_length, y_length, z_length, cut, color, clarity):
    '''Function to predict price'''
    
    # CUT
    if cut == 'Fair':
        cut_fair = 1
        cut_good, cut_vgood, cut_premium, cut_ideal = 0,0,0,0
    elif cut == 'Good':
        cut_good = 1
        cut_fair, cut_vgood, cut_premium, cut_ideal = 0,0,0,0
    elif cut == 'Very Good':
        cut_vgood = 1
        cut_fair, cut_good, cut_premium, cut_ideal = 0,0,0,0
    elif cut == 'Premium':
        cut_premium = 1
        cut_fair, cut_good, cut_vgood, cut_ideal = 0,0,0,0
    elif cut == 'Ideal':
        cut_ideal = 1
        cut_fair, cut_good, cut_premium, cut_vgood = 0,0,0,0
        
    # COLOR
    if color == 'G':
        color_G = 1
        color_E, color_F, color_H, color_D, color_I, color_J = 0,0,0,0,0,0
    elif color == 'E':
        color_E = 1
        color_G, color_F, color_H, color_D, color_I, color_J = 0,0,0,0,0,0
    elif color == 'F':
        color_F = 1
        color_G, color_E, color_H, color_D, color_I, color_J = 0,0,0,0,0,0
    elif color == 'H':
        color_H = 1
        color_G, color_F, color_E, color_D, color_I, color_J = 0,0,0,0,0,0
    elif color == 'D':
        color_D = 1
        color_G, color_F, color_H, color_E, color_I, color_J = 0,0,0,0,0,0
    elif color == 'I':
        color_I = 1
        color_G, color_F, color_H, color_D, color_E, color_J = 0,0,0,0,0,0
    elif color == 'J':
        color_J = 1
        color_G, color_F, color_H, color_D, color_I, color_E = 0,0,0,0,0,0
        
    # CLARITY
    if clarity == 'SI1':
        clarity_SI1 = 1
        clarity_SI2, clarity_VS1, clarity_VS2, clarity_VVS1, clarity_VVS2, clarity_IF, clarity_I1 = 0,0,0,0,0,0,0
    elif clarity == 'SI2':
        clarity_SI2 = 1
        clarity_SI1, clarity_VS1, clarity_VS2, clarity_VVS1, clarity_VVS2, clarity_IF, clarity_I1 = 0,0,0,0,0,0,0
    elif clarity == 'VS1':
        clarity_VS1 = 1
        clarity_SI2, clarity_SI1, clarity_VS2, clarity_VVS1, clarity_VVS2, clarity_IF, clarity_I1 = 0,0,0,0,0,0,0
    elif clarity == 'VS2':
        clarity_VS2 = 1
        clarity_SI2, clarity_VS1, clarity_SI1, clarity_VVS1, clarity_VVS2, clarity_IF, clarity_I1 = 0,0,0,0,0,0,0
    elif clarity == 'VVS1':
        clarity_VVS1 = 1
        clarity_SI2, clarity_VS1, clarity_VS2, clarity_SI1, clarity_VVS2, clarity_IF, clarity_I1 = 0,0,0,0,0,0,0
    elif clarity == 'VVS2':
        clarity_VVS2 = 1
        clarity_SI2, clarity_VS1, clarity_VS2, clarity_VVS1, clarity_SI1, clarity_IF, clarity_I1 = 0,0,0,0,0,0,0
    elif clarity == 'IF':
        clarity_IF = 1
        clarity_SI2, clarity_VS1, clarity_VS2, clarity_VVS1, clarity_VVS2, clarity_SI1, clarity_I1 = 0,0,0,0,0,0,0
    elif clarity == 'I1':
        clarity_I1 = 1
        clarity_SI2, clarity_VS1, clarity_VS2, clarity_VVS1, clarity_VVS2, clarity_IF, clarity_SI1 = 0,0,0,0,0,0,0
    
    X_test = np.array([[carat, depth, table, x_length, y_length, z_length, cut_fair, cut_good, cut_vgood, cut_premium, cut_ideal, color_G, color_E, color_F, color_H, color_D, color_I, color_J, clarity_SI1, clarity_SI2, clarity_VS1, clarity_VS2, clarity_VVS1, clarity_VVS2, clarity_IF, clarity_I1]])
    
    y_predict = model.predict(X_test)
    
    return y_predict

st.title('Diamond Price Predictor')
st.write('An ML application to predict diamond prices. This is especially useful for customers and diamond dealers.')

# FORM
st.header('Fill in the form below')
st.write('Enter the characteristics of the diamond.')

# Form inputs
carat = st.number_input(label='Carat Weight:', min_value=0.1, max_value=10.0, value=1.0)

cut = st.selectbox(label='Cut Rating:', options=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])

color = st.selectbox(label='Color:', options=['G', 'E', 'F', 'H', 'D', 'I', 'J'])

clarity = st.selectbox(label='Clarity Rating:', options=['SI1', 'VS2', 'Si2', 'VS1', 'VVS2', 'VVS1', 'IF', 'I1'])

depth = st.number_input(label='Diamond Depth(%):', min_value=0.1, max_value=100.0, value=1.0)

table = st.number_input(label='Diamond Table(%):', min_value=0.1, max_value=100.0, value=1.0)

x_length = st.number_input(label='X Diamond Length(mm):', min_value=0.1, max_value=100.0, value=1.0)

y_length = st.number_input(label='Y Diamond Length(mm):', min_value=0.1, max_value=100.0, value=1.0)

z_length = st.number_input(label='Z Diamond Length(mm):', min_value=0.1, max_value=100.0, value=1.0)

# Button
if st.button(label='Predict Price'):
    price = predict_price(carat, depth, table, x_length, y_length, z_length, cut, color, clarity)
    
    st.success(f'Price of the diamond is ${price[0]:.2f}')


# Start app in command line
# streamlit run app.py