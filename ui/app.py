import streamlit as st

st.title("RNA MetaWiz")

with st.form("my_form"):
    
    st.subheader("1. Biological System, Samples and Experimental Variables")

    st.text_input("Organism")
    
    st.text_input("Organism ID")
    
    st.text_input("Tissue Cell Type")
    
    st.text_input("Tissue Cell Type ID")

    st.subheader("2. Sequence Read Data")

    st.subheader("3. Processed Data")

    st.subheader("5. General Information and Sample‑Data Relationships")

    st.subheader("5. Experimental and Data Processing Protocols")

    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    submitted = st.form_submit_button("Submit")
