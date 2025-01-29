import streamlit as st
import pickle 
import pandas as pd

st.title('Housing Price Prediction for the California Region for XYZ Brokerage')
#st displays all we want
st.write('This web app predicts *House Price* in the california Region for XYZ Brokerage')

#to read the model from the pickle file
model=pickle.load(open('model_lr.pkl','rb'))

#get the input from the users
med_inc=st.number_input('Median Income')
house_age=st.number_input('House Age')
ave_rooms=st.number_input('Ave Rooms')
ave_bedrms=st.number_input('Ave Bedrooms')
population=st.number_input('Population')
ave_occup=st.number_input('Ave Occupancy')
latitude=st.number_input('Latitude')
longitude=st.number_input('Longitude')

#with this code we can request the input but we need to convert those inputs into dataframes
#to do that we would need to use pandas

#convert the user input to a dataframe
user_data=pd.DataFrame({'MedInc':med_inc,
    'HouseAge':house_age,
    'AveRooms':ave_rooms,
    'AveBedrms':ave_bedrms,
    'Population':population,
    'AveOccup':ave_occup,
    'Latitude':latitude,
    'Longitude':longitude},index=[0])
#Keys should be the same as column names and also the sequence should be the same

#Predict the house price
prediction=model.predict(user_data)

#display the result
if st.button('Predict'):
    st.write(f'The predicted house price is {prediction[0]*1000000}')