# Guess a number game
# Streamlit use 
import streamlit as st
# Random
import random

# Store the random number
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1,20)
if 'attempts' not in st.session_state:
    st.session_state.attempts =0


#Page configuration
st.set_page_config(page_title="Guess The Number Game :",page_icon="🚀",layout="centered")

#CSS Styling
st.markdown(
    """
    <style>
        body {
            background:liner-gradient(135deg, #ff9a9e, #fad0c4);
        }
        .stApp {
           background:liner-gradint(135deg, #8EC5FC, #E0C3FC);
           padding:20px;
           border-radius:15px;
        }
        .stTextInput, .stNumberInput {
           background: #fffff ! important;
           border-radius:10px;
        }
        .stButton>button {
           background:liner-gradint(135deg, #ff9a9e, #f67280);
           color:white;
        }
    </style>

""",
    unsafe_allow_html=True
 
)

# Header
st.markdown("<h1 style='text-align:center; color:#FF5733;'>🥨 Guess The Number game </h1>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #3498db;'>I have choosen a number between 1 to 20. Can you guess it?</h3>",unsafe_allow_html=True)


# User Input

user_guess = st.number_input("Enter your guess :", min_value=20,step=1)


# Button Check .
# use Conditions
if st.button("Check Guess"):
    st.session_state.attempts +=1
    if user_guess < st.session_state.random_number:
        st.warning("❌ Too Low ❗ Try Again🔰")
    elif user_guess > st.session_state.random_number:
        st.warning("❌ Too High ❗ Try Again🔰")
    else:
        st.success(f"🎈 Congratulation ! You Guess number:{st.session_state.attempts} attempts !🏀")

 # Reset Button restart Game

if st.button("🔆Restart Game"):
    st.session_state.random_number = random.randint(1,20)
    st.rerun()


# Footer

st.write("-------------------------------------")
st.write("Amzing Guessing Game enjoy it 🚀")
st.write("© Azeezullah Noohpoto")