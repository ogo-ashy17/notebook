# from openai import OpenAI
import streamlit as st


st.title('🥺Chatbot')
st.caption('This is a simple Streamlit app.')
if 'messaghes' not in st.session_state:
    st.session_state['messages'] = [{'role': 'assistant', 'content': 'How can I help you?'}]

# for msg in st.session_state.messages:
#     st.chat_message(msg['role']).write(msg['content'])

if prompt := st.chat_input():
    # if not openai_api_key:
    #     st.info('Please set your OpenAI API key in the sidebar.')
    #     st.stop()

    # client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)
    # response = client.chat.competions.create(model='gpt-3.5-tarbo', messages=st.session_state.messages)
    # msg = response.choices[0].message.content
    st.session_state.messages.append({'role': 'assistant',  'content': msg})
    st.chat_message('assistant').write(msg)