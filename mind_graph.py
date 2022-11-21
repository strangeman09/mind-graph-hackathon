import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data 
import seaborn as sns

# read csv from a URL
# dataset_url ='https://github.com/strangeman09/mind-graph-hackathon/blob/main/final_merged.csv'
# @st.experimental_memo
# def get_data() -> pd.DataFrame:

#     return pd.read_csv(dataset_url)

df = pd.read_csv('final_merged.csv')
st.set_page_config(
    page_title="mind_graph_hackathon",
    page_icon="✅",
    layout="wide",
)
st.title("increasing participation in club events")
# filter1= st.selectbox("Select the club name", pd.unique(df['Club_Name']))
# df = df[df["Club_Name"] == filter1]
# filter2= st.selectbox("Select the club name", pd.unique(df['Fest_Name']))
# df = df[df["Fest_Name"] == filter2]
filter1=st.selectbox("Select the club name", pd.unique(df.columns))
filter2= st.selectbox("Select the club name", pd.unique(df[filter1]))
df = df[df[filter1] == filter2]
st.dataframe(df)


filter3=st.selectbox("Select the  name for filter 1", pd.unique(df.columns))
filter4= st.selectbox("Select the name for filter 2", pd.unique(df.columns))
# fig_col1, fig_col2 = st.columns(2)


# with fig_col1:
#     st.markdown("### First Chart")
#     fig = sns.countplot(data_frame=df,x='Club_Name')
#     st.write(fig)
   
# with fig_col2:
#     st.markdown("### Second Chart")
#     # fig2 = px.histogram(data_frame=df, x=filter3)
#     fig2 = px.histogram(data_frame=df, x='Fest_name')

#     st.write(fig2)