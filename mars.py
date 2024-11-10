import streamlit as st

increment = st.button('줌범승')
if increment:
    f = open("junbum.txt", 'r')
    line = f.readline()
    line = int(line)+1
    f.close()

    f = open("junbum.txt", 'w')
    data = "%d" % line 
    f.write(data)
    f.close()

st.write('승리수 = ', line)
