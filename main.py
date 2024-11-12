import streamlit as st

st.title('준범이를 위한 스타전적 서버')

#st.subheader('----------------------------------------------------------------------------')
st.subheader('__________________________________________________')

pg = st.navigation([st.Page("전적.py"),
                    st.Page("mars.py"),
                    st.Page("zangsu.py"),
                    st.Page("han.py")])
#human = st.selectbox('Pick user', ['준범','민규','환유'])

pg.run()
