import streamlit as st
st.write('Hello World')
import streamlit as st

option = st.selectbox(
    'Was wünschst du dir zu Weihnachten?',
    ('Frieden', 'Geld', 'Zeit', 'Konzertkarten'))

st.write('You selected:', option)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
