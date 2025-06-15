import streamlit as st
from chain.agent import RNAMetadataAgent


if "metadata" not in st.session_state:
    st.session_state.metadata = {}
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = RNAMetadataAgent()

st.set_page_config(layout="wide")
st.title("RNA MetaWiz")

col1, col2 = st.columns([3, 1], gap="large")

with col1:
    with st.form("metadata_form"):
        st.subheader("Biological system")
        st.text_input("Organism", key="organism")
        st.text_input("Organism ID", key="organism_id")
        st.text_input("Tissue / Cell type", key="tissue_cell_type")
        st.text_input("Tissue / Cell type ID", key="tissue_cell_type_id")
        st.text_input("Qualifier", key="qualifier")
        st.text_input("Value", key="value")
        st.text_input("Source", key="source")
        
        if st.form_submit_button("Save"):
            st.session_state.metadata = {
                k: v for k, v in st.session_state.items()
                if k in (
                    "organism", "organism_id",
                    "tissue_cell_type", "tissue_cell_type_id",
                    "qualifier", "value", "source"
                ) and v
            }
            st.success("Context updated!")

with col2:
    st.subheader("Assistant")
    
    if st.session_state.metadata:
        with st.expander("Current Metadata", expanded=False):
            st.json(st.session_state.metadata)
    
    if prompt := st.chat_input("Ask for suggestions..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("Thinking..."):
            try:
                assistant_reply = st.session_state.agent.get_suggestion(
                    user_input=prompt,
                    current_metadata=st.session_state.metadata,
                    chat_history=st.session_state.messages[:-1]
                )
                
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": assistant_reply
                })
                
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": error_msg
                })
                st.error(f"Failed to get response: {str(e)}")

    with st.container(height=450, border=True):
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])
