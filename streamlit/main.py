import pandas as pd
import streamlit as st

st.title('Hello World')
st.write('This is a simple Streamlit app.')

input_num = st.number_input('Enter a number:', value=0)

result = input_num * 2
st.write(f'The double of {input_num} is {result}.')

st.write(['apple', 'banana', 'cherry'])

df = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C']
})
st.write(df)
st.dataframe(df)

upload_file = st.file_uploader('Choose a file')
if upload_file is not None:
    st.write(upload_file)

if st.button('Say Hello'):
    st.write('Hello!')

if st.checkbox('まっくろくろすけ出ておいで〜'):
    st.write('はーい！まっくろくろすけです！')

option = st.radio(
    'Choose an option:',
    ('Option 1', 'Option 2', 'Option 3')
)

option = st.selectbox(
    'Choose an option:',
    ('Option 1', 'Option 2', 'Option 3')
)

options = st.multiselect(
    'Choose options:',
    ['Option 1', 'Option 2', 'Option 3'],
    ['Option 1', 'Option 2']
)