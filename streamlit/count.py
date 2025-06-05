import streamlit as st


st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0
st.write(f'Count: {st.session_state.count}')

increment = st.button('Increment')
if increment:
    st.session_state.count += 1
st.write(f'Count: {st.session_state.count}')
