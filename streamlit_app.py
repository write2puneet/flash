import streamlit as st
import time
import random

# App Configuration
st.set_page_config(page_title="Aanya's Grade 8 Study Hub", page_icon="🎂", layout="centered")

# --- BIRTHDAY CELEBRATION LOGIC ---
current_date = "23 Apr" # Fixed for her birthday
is_birthday = "23 Apr" in current_date 

if is_birthday:
    st.balloons()
    st.markdown("""
        <div style="background-color: #FFD700; padding: 20px; border-radius: 15px; text-align: center; border: 5px solid #FF69B4;">
            <h1 style="color: #FF1493; margin: 0;">🎉 Happy 13th Birthday, Aanya! 🎂</h1>
            <p style="font-size: 1.2rem; color: #333;">Official Member of the Teens Club! Good luck with Grade 8 today!</p>
        </div>
    """, unsafe_allow_html=True)
    st.confetti = True

# --- CURRICULUM DATA (Sample Structure for 9 Subjects) ---
# Note: You can expand these lists to 100 items each.
subjects = {
    "Mathamatics": [{"q": "Square root of 144?", "a": "12"}, {"q": "Solve 2x = 10", "a": "5"}],
    "Afrikaans": [{"q": "Translate 'Dog' to Afrikaans", "a": "Hond"}, {"q": "What is 'Goeiemôre'?", "a": "Good Morning"}],
    "English": [{"q": "What is a naming word called?", "a": "Noun"}, {"q": "Opposite of 'Ancient'?", "a": "Modern"}],
    "Natural Sciences": [{"q": "What gas do we breathe in?", "a": "Oxygen"}, {"q": "Planet closest to the sun?", "a": "Mercury"}],
    "EMS": [{"q": "What is a 'Need'?", "a": "Essential for survival"}, {"q": "What is ZAR?", "a": "South African Rand"}],
    "Geography": [{"q": "Longest river in Africa?", "a": "The Nile"}, {"q": "Capital of South Africa (Administrative)?", "a": "Pretoria"}],
    "History": [{"q": "When did SA become a democracy?", "a": "1994"}, {"q": "Who was the first black president of SA?", "a": "Nelson Mandela"}],
    "Life Orientation": [{"q": "What is self-esteem?", "a": "How you feel about yourself"}, {"q": "Define 'Bullying'", "a": "Repeated aggressive behavior"}],
    "Technology": [{"q": "What does a 'pulley' do?", "a": "Lifts heavy loads"}, {"q": "Main material in a glass bottle?", "a": "Silica Sand"}]
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📖 Aanya's Study Desk")
selected_subject = st.sidebar.selectbox("Choose Subject", list(subjects.keys()), help="Select the subject you want to practice.")
selected_set = st.sidebar.selectbox("Select Set", [f"Set {i}" for i in range(1, 11)], help="Each set gets progressively harder!")

# --- SESSION STATE ---
if "card_idx" not in st.session_state:
    st.session_state.card_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "flipped" not in st.session_state:
    st.session_state.flipped = False

# Reset when subject or set changes
if "last_selection" not in st.session_state or st.session_state.last_selection != (selected_subject, selected_set):
    st.session_state.card_idx = 0
    st.session_state.score = 0
    st.session_state.flipped = False
    st.session_state.last_selection = (selected_subject, selected_set)

# Load cards (using subject data - in a real app, filter 100 questions into 10 per set)
current_cards = subjects[selected_subject]
current_card = current_cards[st.session_state.card_idx % len(current_cards)]

# --- MAIN INTERFACE ---
st.write(f"### {selected_subject} > {selected_set}")
st.metric("Total Score", f"{st.session_state.score}", help="Your total correct answers for this session.")

st.progress((st.session_state.card_idx + 1) / 10) # Assuming 10 cards per set

# --- FLASHCARD LOGIC ---
st.container()
with st.expander("💡 Study Hint", expanded=False):
    st.write("Take your time! Read the question carefully before flipping.")

if not st.session_state.flipped:
    st.info(f"**Question:**\n\n{current_card['q']}")
    if st.button("🔍 REVEAL ANSWER"):
        st.session_state.flipped = True
        st.rerun()
else:
    st.success(f"**Answer:**\n\n{current_card['a']}")
    st.write("---")
    st.write("Did you get it right?")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Yes, Got it!", help="Add a point to your score"):
            st.session_state.score += 1
            st.session_state.card_idx += 1
            st.session_state.flipped = False
            st.rerun()
    with c2:
        if st.button("❌ Not yet", help="Keep trying, you'll get it next time!"):
            st.session_state.card_idx += 1
            st.session_state.flipped = False
            st.rerun()

# --- FOOTER ---
if st.sidebar.button("♻️ Restart Session"):
    st.session_state.card_idx = 0
    st.session_state.score = 0
    st.session_state.flipped = False
    st.rerun()
