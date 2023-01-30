import streamlit as st
import pickle
import pandas as pd
from PIL import Image

pipe = pickle.load(open('food.pkl', 'rb'))

st.title('   \n')
st.title(' \n')
st.title(' \n')
st.title(' \n')
st.title(' \n')
st.title('\n\n Food taste predictor ')

st.markdown(
    f"""
        <style>
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/d3/6d/46/d36d462db827833805497d9ea78a1343.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
    unsafe_allow_html=True
)

col3,col4,col5 = st.columns(3)

with col3:
    prep_time = st.number_input('Preparation Time')
with col4:
    cook_time = st.number_input('Cooking Time')
with col5:
    addition_time = st.number_input('Additional Time ')

total_time = prep_time + cook_time + addition_time

col1, col2 = st.columns(2)

with col1:
    servings = st.number_input('No. of people the dish is served ')
with col2:
    rating = st.number_input('Average rating')


col6,col7,col8,col9 = st.columns(4)
with col6:
    fat = st.number_input('Total fat')
with col7:
    carbs = st.number_input('Total carbs')
with col8:
    protine = st.number_input('Total Protein')
with col9:
    calories = st.number_input('Total calories')

if st.button('Get prediction about your dish'):


    input_df = pd.DataFrame(
     {'addition_time': [addition_time], 'servings': [servings],'prep_time': [prep_time], 'cook_time': [cook_time], 'total_time': [total_time],
      'calories': [calories], 'fat': [fat], 'carbs': [carbs], 'protine': [protine],'rating': [rating]})
    result = pipe.predict(input_df)
    if result==1:
        
        with col10:
            st.header("Your food is recommended")
        
    else:
       
        with col10:
            st.header("Your food is not recommended")
     
