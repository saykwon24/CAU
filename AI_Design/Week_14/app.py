"""
Exercises
    1) use "anaconda prompt"
    2) copy the address of 'app.py' and enter "cd address" in command line
    3) enter "streamlit run add.py" in command line
    
    "Ctrl + C" to stop the running of app.py
"""


import streamlit as st

st.title("AID Streamlit Practice")
st.write("This is my new app")
button1 = st.button("Click Me")
if button1:
    st.write("This is some text.")

#################### above is basic code ####################

#1) Radio Button: streamlit.radio()
st.header("Start of the Radio Button Section")
animal = st.radio("What animal is your favorite?", ('Lion', 'Tiger', 'Bear'))
button2 = st.button("Submit Animal")
if button2:
    st.write(animal)
    if animal == "Lion": st.write("ROAR!")
    elif animal == "Tiger": st.write("GRRR!")
    else: st.write("URRRR!")

#2) Text Input: streamlit.text_input()
st.header("Start of the Text Input Section")
user_text = st.text_input("What's your favorite movie?", "Interstellar")
if st.button("Text Button"):
    st.write(user_text)
