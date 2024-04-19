import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("final_data.csv")

# App title
st.title("Movie Subtitle Search Engine")

# User input for search query
user_input = st.text_input("Enter a search query related to movie subtitles")

# Button to trigger search
if st.button("Search"):
    # Filter results based on user input
    results = df[df['ncc'].str.contains(user_input, case=False)]['name'].tolist()
    
    # Display search results
    if len(results) == 0:
        st.warning("No matching results found.")
    else:
        st.success("Matching results:")
        # Display each result as a list item
        for result in results:
            st.write(result)
