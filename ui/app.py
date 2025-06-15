import json
import streamlit as st
from openai import OpenAI


client = OpenAI()


if "metadata" not in st.session_state:
    st.session_state.metadata = {}

if "messages" not in st.session_state:
    st.session_state.messages = []


st.set_page_config(layout="wide")
st.title("RNA MetaWiz")


col1, col2 = st.columns([3, 1], gap="large")


with col1:
    with st.form("metadata_form"):
        st.subheader("Biological system")

        st.text_input("Organism",
                      key="organism")
        st.text_input("Organism ID",
                      key="organism_id")
        st.text_input("Tissue / Cell type",
                      key="tissue_cell_type")
        st.text_input("Tissue / Cell type ID",
                      key="tissue_cell_type_id")
        st.text_input("Qualifier",
                      key="qualifier")
        st.text_input("Value",
                      key="value")
        st.text_input("Source",
                      key="source")

        if st.form_submit_button("Save"):
            st.session_state.metadata = {
                k: v for k, v in st.session_state.items()
                if k in (
                    "organism", "organism_id",
                    "tissue_cell_type", "tissue_cell_type_id",
                    "qualifier", "value", "source")
                and v
            }
            st.success("Context updated!")


with col2:
    st.subheader("Assistant")

    if prompt := st.chat_input("Ask for suggestions..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        system_context = {
            "role": "system",
            "content": (
                "You are an RNA-seq metadata assistant.\n"
                "These are the fields the user has filled so far:\n"
                f"{json.dumps(st.session_state.metadata, indent=2)}\n\n"
                "When you answer, suggest how to fill in the missing fields."
            )
        }

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[system_context] + st.session_state.messages,
            temperature=0.2,
        )
        assistant_reply = response.choices[0].message.content

        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_reply})

    with st.container(height=600, border=True):
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.markdown(m["content"])

