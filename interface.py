import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib as plt

# streamlit run interface.py
# ------------------------------------
# Section that prints various objects
# st.text("New inputs")
# a = 2
# st.write(a)
# ------------------------------------

st.title("Competitors Analysis Project")


img = Image.open('images.png')
resized_img = img.resize((200, 200)) 
st.image(resized_img, caption="Resized Image")



store_df = pd.read_csv('store.csv')
# st.table(store_df.head())

train_df = pd.read_csv('train.csv')

df = pd.merge(train_df, store_df, on='Store', how = 'left')

# Your data processing
salesbystoretype = df.groupby("StoreType")['Sales'].sum()

st.bar_chart(salesbystoretype)

# ------------------------------------
# Create the figure
# fig, ax = plt.subplots()
# ax.bar(salesbystoretype.index, salesbystoretype.values)
# ax.set_xlabel("Store type")
# ax.set_ylabel("Sales amount")
# ax.set_title("Sales by store type")

# # Display in Streamlit
# st.pyplot(fig)
# ------------------------------------

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()

sales_by_year = df.groupby('Year')['Sales'].sum()
st.bar_chart(sales_by_year)