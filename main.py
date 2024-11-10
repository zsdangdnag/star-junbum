import streamlit as st

st.title('준범이를 위한 스타전적 서버')

pg = st.navigation([st.Page("junbum.py"),st.Page("page_2.py")])
#human = st.selectbox('Pick user', ['준범','민규','환유'])

pg.run()
