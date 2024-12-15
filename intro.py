import streamlit as st

st.title(":blue[my web app]")
st.header(":red[This venkatesh's app]")


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None
   
)

st.write("You selected:", genre)