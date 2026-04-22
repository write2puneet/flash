import streamlit as st
import time
from datetime import datetime

# --- CONFIGURATION & BIRTHDAY LOGIC ---
st.set_page_config(page_title="Aanya's Study Hub", page_icon="🎂")

# Birthday logic: Only shows until end of 23 April 2026
target_date = datetime(2026, 4, 23)
is_birthday_period = datetime.now() <= target_date

if is_birthday_period:
    st.balloons()
    st.markdown("""
        <div style="background-color: #FFD700; padding: 25px; border-radius: 20px; text-align: center; border: 5px solid #FF69B4; box-shadow: 10px 10px 5px #ccc;">
            <h1 style="color: #FF1493; margin: 0; font-family: 'Comic Sans MS';">🎉 Happy 13th Birthday, Aanya! 🎂</h1>
            <p style="font-size: 1.4rem; color: #333;">Welcome to the official <b>Teen Club</b>! You're officially an amazing 13-year-old now! 🎈✨</p>
        </div>
    """, unsafe_allow_html=True)

# --- EXPANDED DATASET (9 Subjects, 10 Sets each, 10 Questions each) ---
# Note: Sample logic provided for structure. You can fill the lists to reach 100 per subject.
subjects_data = {
    "Mathamatics": [
        {"q": f"Math Set {s+1} - Q{i+1}: Basic Algebra", "a": "Answer"} for s in range(10) for i in range(10)
    ],
    "Afrikaans": [
        {"q": f"Afrikaans Set {s+1} - Q{i+1}: Vocabulary", "a": "Antwoord"} for s in range(10) for i in range(10)
    ],
    "EMS": [
        {"q": f"EMS Set {s+1} - Q{i+1}: Economics", "a": "Answer"} for s in range(10) for i in range(10)
    ],
    "English": [
        {"q": f"English Set {s+1} - Q{i+1}: Grammar", "a": "Answer"} for s in range(10) for i in range(10)
    ],
    "Geography": [
        {"q": f"Geography Set {s+1} - Q{i+1}: Mapwork", "a": "Answer"} for s in range(10) for i in range(10)
    ],
    "History": [
        {"q": f"History Set {s+1} - Q{i+1}: SA History", "a": "Answer"} for s in range(10) for i in range(10)
    ],
    "Life Orientation": [
        {"q": f"L.O. Set {s+1} - Q{i+1}: Self Development", "a": "Answer"} for s in range(10) for i in range(10)
    ],
    "Natural Sciences": [
        {"q": f"N.S. Set {s+1} - Q{i+1}: Biology/Physics", "a": "Answer"} for s in range(10) for i in range(10)
    ],
    "Technology": [
        {"q": f"Tech Set {s+1} - Q{i+1}: Structures", "a": "Answer"} for s in range(10) for i in range(10)
    ]
}

# --- NAVIGATION ---
st.sidebar.title("⭐ Aanya's Study Zone")
subj = st.sidebar.selectbox("Subject", list(subjects_data.keys()), help="Choose a subject to study.")
set_num = st.sidebar.selectbox("Select Set (10 Questions Each)", [f"Set {i+1}" for i in range(10)], help="Sets get harder as you go!")

# --- SESSION STATE ---
if "card_idx" not in st.session_state:
    st.session_state.card_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "flipped" not in st.session_state:
    st.session_state.flipped = False

# Reset on change
current_set_id = int(set_num.split()[-1]) - 1
if "last_nav" not in st.session_state or st.session_state.last_nav != (subj, set_num):
    st.session_state.card_idx = 0
    st.session_state.score = 0
    st.session_state.flipped = False
    st.session_state.last_nav = (subj, set_num)

# Slice the 100 questions to get the 10 for this set
all_subj_cards = subjects_data[subj]
set_cards = all_subj_cards[current_set_id*10 : (current_set_id+1)*10]
current_card = set_cards[st.session_state.card_idx % 10]

# --- UI ---
st.write(f"### {subj} | {set_num}")
st.metric("Session Score", f"{st.session_state.score}/10", help="Correct answers in this set.")
st.progress((st.session_state.card_idx + 1) / 10)

st.markdown("---")
st.subheader(f"Question {st.session_state.card_idx + 1}:")
st.info(current_card["q"])

if not st.session_state.flipped:
    if st.button("🔍 SHOW ANSWER"):
        st.session_state.flipped = True
        st.rerun()
else:
    st.success(f"**Answer:** {current_card['a']}")
    st.write("Did you get it right?")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Yes", help="Click if you knew the answer!"):
            st.session_state.score += 1
            st.session_state.card_idx = (st.session_state.card_idx + 1) % 10
            st.session_state.flipped = False
            st.rerun()
    with c2:
        if st.button("❌ No", help="Click if you need more practice on this."):
            st.session_state.card_idx = (st.session_state.card_idx + 1) % 10
            st.session_state.flipped = False
            st.rerun()

# Timer for focus
if st.sidebar.button("Restart Timer"):
    st.session_state.start_time = time.time()
    st.rerun()

# Auto-refresh timer logic
time.sleep(1)
st.rerun()
