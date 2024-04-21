import streamlit as st
import requests

# Inject custom CSS for Amazon-like customer support styling
st.markdown("""
<style>
body {
    font-family: "Amazon Ember", Arial, sans-serif;
    background-color: #FFFFFF;
    color: #0F1111;
}
.main {
    max-width: 800px;
    margin: auto;
}
.stTextInput>div>div>input, .stTextArea>div>div>textarea {
    color: #0F1111;
    border: 2px solid #CDD0D4;
    width: 100%;
}
.stButton>button {
    color: #FFFFFF;
    background-color: #FF9900;
    border-radius: 4px;
    border: none;
    padding: 10px 24px;
    font-size: 16px;
    font-weight: bold;
    width: 100%;
}
.stButton>button:hover {
    background-color: #F08804;
}
h1, h2, h3, h4, h5, h6 {
    color: #0F1111;
}
/* Custom class for the logo and title alignment */
.logo-and-title {
    display: flex;
    align-items: center;
}
.logo-img {
    margin-right: 10px; /* Space between logo and title */
}
</style>
""", unsafe_allow_html=True)

# Streamlit page configuration with logo and title side by side
col1, col2 = st.columns([1, 8])
with col1:
    st.image('amazon.png', width=80)  # Smaller logo image
with col2:
    st.markdown("#  Amazon Customer Support")

st.write("Welcome to Amazon Customer Support. Please enter your query here.")

# User input section
st.header("Submit Your Query")
user_input = st.text_area("Type your sentence here:", height=150, max_chars=500)

# Instructions
st.write("Hit the 'Submit Query' button below once you've entered your sentence.")

# Button to trigger prediction and display results
if st.button("Submit Query"):
    if user_input:
        url = "http://localhost:8000/predict/"  # Ensure this URL is correct
        response = requests.post(url, json={"text": user_input})
        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction']
            if prediction == "humorous":
                st.success("😄 Your sentence is humorous!")
            else:
                st.info("😐 Your sentence is not humorous.")
        else:
            st.error("Failed to get a response from the API. Please try again later.")
    else:
        st.warning("Please enter a sentence to analyze.")
