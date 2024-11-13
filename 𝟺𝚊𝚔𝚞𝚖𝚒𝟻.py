import streamlit as st
import numpy as np
import pandas as pd


user=['mars','zangsu','𝟺𝚊𝚔𝚞𝚖𝚒𝟻']



def txt(a):
    f = open("user//{}.txt".format(a), 'r')
    i = f.readline()
    a =i.split(",")
    f.close() 
    a = [int (i) for i in a]
    return a


def sum_(a):
    del a[a[0]]
    del a[0]
    return sum(a)

def losesum_(a,num):
    
    del a[num]
    b = a[0][num+1]+a[1][num+1]
    return b

def pers(a,b):
    return (a/b)*(100)


def write(num):
    st.header(user[num], divider="gray")
    player=[txt(user[0]),txt(user[1]),txt(user[2])]

    col1, col2, col3 = st.columns(3)

    Sum=sum_(player[num])
    Losesum=losesum_(player,num)
    

    col1.subheader("-----총전적-----", divider="gray")
    col1.write("| 총 승리수:{} |".format(Sum))
    col1.write("| 총 패배수:{} |".format(Losesum))
    col1.write("| 승률:{}% |".format(pers(Sum,Sum+Losesum)))


    player=[txt(user[0]),txt(user[1]),txt(user[2])]

    for i in player:
        if i[0]  != num+1:
            col2.subheader("-----{}-----".format(user[i[0]-1]), divider="gray")
            col2.write("|  승리수:{} |".format(player[num][i[0]]))
            col2.write("|  패배수:{} |".format(i[num+1]))
            
            victory = [player[num][i[0]]]
            fail = [i[num+1]]
            index = [user[i[0]-1]]
            df = pd.DataFrame({'victory': victory,
                               'fail': fail},
                                index=index)
            col3.bar_chart(df)




write(2)
