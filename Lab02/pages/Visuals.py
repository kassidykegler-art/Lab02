# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")


try:
    csv_df = pd.read_csv("data.csv")
    csv_df["Value"] = pd.to_numeric(csv_df["Value"], errors="coerce")
    st.success("CSV data loaded successfully!")
except FileNotFoundError:
    st.warning("'data.csv' not found. Creating an empty DataFrame instead.")
    csv_df = pd.DataFrame(columns=["Category", "Value"])

try:
    with open("data.json", "r") as f:
        json_data = json.load(f)
    st.success("JSON data loaded successfully!")
except FileNotFoundError:
    st.warning("'data.json' not found. Creating an empty dictionary instead.")
    json_data = {}

st.info("TODO: Add your data loading logic here.")


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Classes and Credit Hours") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
if not csv_df.empty:
    st.bar_chart(data=csv_df, x="Category", y="Value") #NEW
    st.write("**Description:**   This bar chart shows the amount of hours studied for each class.")
else:
    st.warning("No data available in 'data.csv' to display the chart.")

# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Classes and Credit Hours Greater Than or Equal to 3") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.
option = st.selectbox("Only show numbers greater than 3", ["Yes", "No"])
st.session_state["filter_option"] = option
if not csv_df.empty:
    if option == "Yes":
        filtered_df = csv_df[csv_df["Value"] > 3]
    else:
        filtered_df = csv_df
    st.line_chart(data=filtered_df, x="Category", y="Value") #NEW
    st.write("**Description:**   This line chart shows the amount of hours studied for each class.")
else:
    st.warning("No data available in 'data.csv' to display the chart.")
    

# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Classes and Recommended Study Time") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        json_data = json.load(f)
        data_points = json_data.get("data_points", [])
        json_df = pd.DataFrame(data_points)
        json_df = json_df.rename(columns={"label": "Class", "value": "RecommendedHours"})
        json_df["RecommendedHours"] = pd.to_numeric(json_df["RecommendedHours"], errors="coerce")
else:
    st.warning("No data.json file found — please upload one.")
    json_df = pd.DataFrame(columns=["Class", "RecommendedHours"])
option2 = st.radio("Do you want to only show classes that should be studied for 10 or more hours?", ["Yes", "No"])
st.session_state["study_filter"] = option2
if not json_df.empty:
    if option2 == "Yes":
        filtered_json = json_df[json_df["RecommendedHours"] >= 10]
    else:
        filtered_json = json_df
    st.scatter_chart(data=filtered_json, x="Class", y="RecommendedHours") #NEW
    st.write("**Description:** This chart displays the recommended study hours for each class. ""Use the radio button above to show only classes with 10 or more study hours. ")
else:
    st.warning("No data available in 'data.json' to display the chart.")
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.

