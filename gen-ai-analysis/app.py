from openai import OpenAI
import streamlit as st
import pandas as pd
import os

# Sidebar for API key and file upload
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

st.title("💬 Finance Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI, with CSV capabilities")

# Load CSV file into session state for memory across user interactions
if uploaded_file is not None:
    st.session_state["dataframe"] = pd.read_csv(uploaded_file)
    st.write("CSV file uploaded successfully. You can now ask questions about it.")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input(placeholder="Ask a question, or inquire about the uploaded data."):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Check if DataFrame exists and integrate it into the assistant's response
    if "dataframe" in st.session_state:
        # Convert the DataFrame to a string format to pass it as context for smaller data
        data_str = st.session_state["dataframe"].to_string()
        
        # Formulate the prompt to include the data context
        full_prompt = f"""
        Here is the content of the CSV file:\n{data_str}\n\n
        Based on this data, answer the following question:\n{prompt}
        """
    else:
        full_prompt = prompt

    # Generate response using OpenAI's chat model
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages + [{"role": "user", "content": full_prompt}])
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
