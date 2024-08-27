import streamlit as st
from router_chain import RouteCOVEChain

# Display the title
st.title("Test")

# Add a text input box for the query
query = st.text_input("Enter your query:", "")

# Add a button that, when clicked, triggers the result generation
if st.button("Get Result"):
    # Use the RouteCOVEChain to get the result for the given query
    result = RouteCOVEChain(query)
    
    # Display the result
    st.write("Result:")
    st.write(result)
