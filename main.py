import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
# Trend of baby names in the United States(1880 - 2020)
""")

df = pd.read_csv("names_ranks_counts.csv")

baby_name = st.text_input("Baby name", placeholder="Enter a baby name")
gender = st.radio("Gender of the baby", ("M", "F"))
baby_name = baby_name.strip()

if baby_name != "":
    name_df = df[(df.name == baby_name) & (df.sex == gender)]
    name_df = name_df.sort_values("year")

    fig = plt.figure(figsize = (15, 10))
    plt.plot(name_df['year'], name_df['count'])
    plt.xlabel("Years")
    plt.ylabel("No. of babies")
    plt.title(f"Trend of the name {baby_name} in USA from 1880 to 2020")

    st.pyplot(fig)
