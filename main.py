import streamlit as st
import subprocess


def start_tic_tac_toe():
    """Launch the Tkinter-based Tic-Tac-Toe game."""
    # Change the path as per your script location.
    subprocess.Popen(['python', 'C:/Users/DELL/OneDrive/Desktop/AI-Games/tic-tac-toe.py'])

def start_rock_paper_scissor():
    """Launch the Tkinter-based Rock-paper-scissor game."""
    subprocess.Popen(['python', 'C:/Users/DELL/OneDrive/Desktop/AI-Games/rock-paper-scissor.py'])    

st.balloons()
# Streamlit Dashboard
st.title("Alpha Gaming Dashboard")

st.sidebar.title("Login")
st.sidebar.title("Signup")
# Add game images and buttons

col1, col2 = st.columns(2)

# First game: Tic-Tac-Toe
with col1:
    st.image("tic-tac-toe.jpg", caption="Tic-Tac-Toe", use_container_width=True)
    if st.button("Play Tic-Tac-Toe"):
        start_tic_tac_toe()

# Second game: Rock-Paper-Scissor
with col2:
    st.image("rock-paper-scissor.jpg", caption="Rock-Paper-Scissor", use_container_width=True)
    if st.button("Play Rock-Paper-Scissor"):
        start_rock_paper_scissor()