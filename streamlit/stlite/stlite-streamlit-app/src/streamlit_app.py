import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit Example')
st.write('pandas version:', pd.__version__)

rnd_data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
st.line_chart(rnd_data)