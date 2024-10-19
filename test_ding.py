#import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(r'avocado.csv')

df = get_data()

# dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# top-level filters
job_filter = st.selectbox("Select the Job", pd.unique(df["region"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["region"] == job_filter]

# near real-time / live feed simulation
for seconds in range(200):

    df["AveragePrice"] = df["AveragePrice"] * np.random.choice(range(1, 5))
    df["Total Volume"] = df["Total Volume"] * np.random.choice(range(1, 5))

    # creating KPIs
    avg_age = np.mean(df["AveragePrice"])


    #balance = np.mean(df["type"])

    with placeholder.container():

        # create three columns
       # kpi1= st.columns()

        # fill in those three columns with respective metrics or KPIs
        #kpi1.metric(
          #  label="averageprice ⏳",
           # value=round(avg_age),
            #delta=round(avg_age) - 10,
        #)
        
        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
                data_frame=df, y="region", x="AveragePrice"
            )
            st.write(fig)
            
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="Total Bags")
            st.write(fig2)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
       # time.sleep(1)
