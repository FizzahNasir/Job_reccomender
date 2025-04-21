import streamlit as st
import pandas as pd
import pickle

# Load data
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation logic
def recommendation(title):
    idx = df[df['Title'] == title].index[0]
    idx = df.index.get_loc(idx)
    distances = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)[1:11]
    
    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)
    return jobs

# --------------------------
# Streamlit UI starts here
# --------------------------
st.set_page_config(page_title="Job Recommender", layout="centered", page_icon="💼")

st.markdown("""
    <h1 style='text-align: center; color: #2E8B57;'>💼 Job Recommendation System</h1>
    <p style='text-align: center;'>Select a job title to discover similar opportunities</p>
    <hr>
""", unsafe_allow_html=True)

# Dropdown to select a job title
title = st.selectbox('🔍 Search job by title', df['Title'].sort_values())

# Button to trigger recommendations
if st.button("Show Recommendations"):
    jobs = recommendation(title)

    if jobs:
        st.success(f"Here are jobs similar to **{title}**:")
        for i, job in enumerate(jobs, 1):
            st.markdown(f"**{i}.** {job}")
    else:
        st.warning("No recommendations found.")
