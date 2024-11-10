jun_vic = 0
jun_fail = 0

import streamlit as st

increment = st.button('Increment')
if increment:
    jun_vic += 1

st.write('Count = ', jun_vic)
