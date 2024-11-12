import streamlit as st
import os
import fnmatch


col1, col2 = st.columns(2)


col1.header("Player1")
Player1_= col1.selectbox('user1', ['mars','zangsu','𝟺𝚊𝚔𝚞𝚖𝚒𝟻'])
Player1_vic = col1.button('victory')


col2.header("Player2")

Player2_=col2.selectbox('user2', ['mars','zangsu','𝟺𝚊𝚔𝚞𝚖𝚒𝟻'])
Player2_vic = col2.button('victory ') 



if Player1_ == 'mars':
    player1_code = 1
elif Player1_ == 'zangsu':
    player1_code = 2
elif Player1_ == '𝟺𝚊𝚔𝚞𝚖𝚒𝟻':
    player1_code = 3


if Player2_ == 'mars':
    player2_code = 1
elif Player2_ == 'zangsu':
    player2_code = 2
elif Player2_ == '𝟺𝚊𝚔𝚞𝚖𝚒𝟻':
    player2_code = 3


# f = open("user//junbum.txt", 'r')

# f.close()

f = open("user//{}.txt".format(Player1_), 'r')
i = f.readline()
Player1 =i.split(",")
f.close() 
Player1 = [int (i) for i in Player1]


f = open("user//{}.txt".format(Player2_), 'r')
i = f.readline()
Player2 =i.split(",")
f.close() 
Player2 = [int (i) for i in Player2]

# for file1 in os.listdir('./user\\') :
#     f = open("./user\\{}".format(file1), 'r')
#     i = f.readline()
#     Player1 =i.split(",")
#     f.close() 
#     Player1 = [int (i) for i in Player1]
#     if(Player1[0])==player1_code:
#         break


# for file2 in os.listdir('./user\\') :
#     f = open("./user\\{}".format(file2), 'r')
#     i = f.readline()
#     Player2 =i.split(",")
#     f.close()
#     Player2 = [int (i) for i in Player2]
#     if(Player2[0])==player2_code:
#         break

if Player1_vic:
    Player1[int(Player2[0])]+=1
    f = open("user//{}.txt".format(Player1_), 'w')
    f.write("{},{},{},{}".format(Player1[0],Player1[1],Player1[2],Player1[3]))
    f.close()
    st.write("{} :   victory".format(Player1_))


if Player2_vic:
    Player2[int(Player1[0])]+=1
    f = open("user//{}.txt".format(Player2_), 'w')
    f.write("{},{},{},{}".format(Player2[0],Player2[1],Player2[2],Player2[3]))
    f.close()   
    st.write("{} :   victory".format(Player2_))

