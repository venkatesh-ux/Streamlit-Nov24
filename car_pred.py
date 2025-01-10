import streamlit as st
import pandas as pd
import os
print(os.getcwd())
import pickle

# load the model from disk.
with open('car_pred_model', 'rb') as f:
    model = pickle.load(f)


cars_df = pd.read_csv("./cars24-car-price.csv")

st.title("Cars resale price pred!")
st.header("Powered by ch.venkatesh",divider="rainbow")

st.dataframe(cars_df.head())

col1, col2, col3 = st.columns(3)

fuel_type = col1.selectbox("Select the fuel type",
                           ["Diesel","Petrol","CNG","LPG", "Electric"])

engine = col1.slider("Select the engine power",
                            500,5000,step=100)


transmission_type = col2.selectbox("Select the transmission type",
                                   ["Manual","Automatic"])

seats = col2.selectbox("Enter the no.of sears",
                       [4,5,7,9,11])


#encode data
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

if st.button("Get price"):

    encode_fuel_type = encode_dict['fuel_type'][fuel_type]
    encode_transmission_type = encode_dict['transmission_type'][transmission_type]

    input_data = [2012.0,2,120000,encode_fuel_type,encode_transmission_type,19.7,engine,46.3,seats]
    pred = model.predict([input_data])[0]

    st.write(round(pred,2))


