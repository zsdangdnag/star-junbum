import streamlit as st
import os
import fnmatch


col1, col2 = st.columns(2)


col1.header("Player1")
Player1_= col1.selectbox('user1', ['준범','민규','환유'])
Player1_vic = col1.button('victory')


col2.header("Player2")

Player2_=col2.selectbox('user2', ['준범','민규','환유'])
Player2_vic = col2.button('victory ') 



if Player1_ == '준범':
    player1_code = 0
elif Player1_ == '민규':
    player1_code = 1
elif Player1_ == '환유':
    player1_code = 2


if Player2_ == '준범':
    player2_code = 0
elif Player2_ == '민규':
    player2_code = 1
elif Player2_ == '환유':
    player2_code = 2


f = open("user//junbum.txt", 'r')

f.close()

for file1 in os.listdir('./user\\') :
    f = open("./user\\{}".format(file1), 'r')
    i = f.readline()
    Player1 =i.split(",")
    f.close() 
    Player1 = [int (i) for i in Player1]
    if(Player1[0])==player1_code:
        break


for file2 in os.listdir('./user\\') :
    f = open("./user\\{}".format(file2), 'r')
    i = f.readline()
    Player2 =i.split(",")
    f.close()
    Player2 = [int (i) for i in Player2]
    if(Player2[0])==player2_code:
        break

if Player1_vic:
    Player1[int(Player2[0])]+=1
    f = open("./user\\{}".format(file1), 'w')
    f.write("{},{},{},{}".format(Player1[0],Player1[1],Player1[2],Player1[3]))
    f.close()


if Player2_vic:
    Player1[int(Player2[0])]+=1
    f = open("./user\\{}".format(file2), 'w')
    f.write("{},{},{},{}".format(Player2[0],Player2[1],Player2[2],Player2[3]))
    f.close()   

