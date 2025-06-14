import streamlit as st

st.set_page_config(layout="wide")

st.title("RNA MetaWiz")

col1, col2 = st.columns([3, 1], border=True)

with col1:
    with st.form("my_form", border=False):
        
        st.subheader("Biological System")

        st.text_input("Organism")
        
        st.text_input("Organism ID")
        
        st.text_input("Tissue Cell Type")
        
        st.text_input("Tissue Cell Type ID")
        
        st.text_input("Qualifier")
        
        st.text_input("Value")
        
        st.text_input("Source")

        submitted = st.form_submit_button("Submit")

with col2:
    st.subheader("Assistant")
    
    if prompt := st.chat_input("Ask for suggestions directly"):

        with st.chat_message("user"):
            st.markdown(prompt)
    
        with st.chat_message("assistant"):
            st.markdown("LLM suggestions here.")
    
