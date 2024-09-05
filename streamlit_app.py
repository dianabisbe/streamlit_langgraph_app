"""Module providing the UI for the LangGraph AI Agent using Streamlit."""

import streamlit as st
import requests

st.title('LangGraph AI Agent')

PROMPT_INPUT = '''Pregúntame sobre artículos de wikipedia
                y tus documentos de runiones'''
user_input = st.text_input(PROMPT_INPUT, "")

if 'history' not in st.session_state:
    st.session_state['history'] = []

for message in st.session_state['history']:
    st.write(f"You: {message['user']}")
    st.write(f"Agent: {message['agent']}")

if user_input:
    with st.spinner("Pensando..."):
        response = requests.post("https://my-app-1001072323049.us-central1.run.app/invoke",
                         json={"query": user_input},
                         timeout=10)

        agent_response = response.json()['response']

        st.session_state['history'].append({"user": user_input, "agent": agent_response})

        st.write(f"You: {user_input}")
        st.write(f"Agent: {agent_response}")
