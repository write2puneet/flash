import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="Grade 8 Maths Challenge", page_icon="🇿🇦")

# Mathematics Data (Truncated for display - keep your 100 cards here)
data = {
    "Level 1: Foundation": [
        {"q": "What is the square root of 144?", "a": "12"},
        {"q": "What is the HCF of 12 and 18?", "a": "6"},
        # ... include all other cards from previous list here ...
    ],
    "Level 2: Intermediate": [
        {"q": "Solve for x: 2x = 10", "a": "x = 5"},
        {"q": "What is 20% of R250?", "a": "R50"},
    ],
    "Level 3: Exam Prep": [
        {"q": "Solve for x: 3(x - 2) = 9", "a": "x = 5"},
        {"q": "Calculate the hypotenuse: sides 3cm and 4cm.", "a": "5cm"},
    ]
}

# Initialize session state for scoring and timing
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "flipped" not in st.session_state:
    st.session_state.flipped = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# Sidebar Settings
st.sidebar.title("🎮 Game Controls")
level_key = st.sidebar.selectbox("Select Study Level", list(data.keys()))

# Reset everything if level changes
if "last_level" not in st.session_state or st.session_state.last_level != level_key:
    st.session_state.card_index = 0
    st.session_state.score = 0
    st.session_state.flipped = False
    st.session_state.last_level = level_key
    st.session_state.start_time = time.time()

cards = data[level_key]
current_card = cards[st.session_state.card_index]

# Main UI
st.title("🇿🇦 Grade 8 Maths Challenge")

# Top Row: Score and Timer
col_s, col_t = st.columns(2)
with col_s:
    st.metric("Current Score", f"{st.session_state.score}/{len(cards)}")
with col_t:
    elapsed_time = int(time.time() - st.session_state.start_time)
    st.metric("Time Elapsed", f"{elapsed_time}s")

st.progress((st.session_state.card_index + 1) / len(cards))

# Flashcard Area
st.markdown("---")
if not st.session_state.flipped:
    st.info(f"### Question {st.session_state.card_index + 1}:\n{current_card['q']}")
    if st.button("🔍 SHOW ANSWER"):
        st.session_state.flipped = True
        st.rerun()
else:
    st.success(f"### Answer:\n{current_card['a']}")
    
    st.write("Did you get it right?")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Yes (Add Point)"):
            st.session_state.score += 1
            st.session_state.card_index = (st.session_state.card_index + 1) % len(cards)
            st.session_state.flipped = False
            st.rerun()
    with c2:
        if st.button("❌ No (Next Card)"):
            st.session_state.card_index = (st.session_state.card_index + 1) % len(cards)
            st.session_state.flipped = False
            st.rerun()

# Reset Button
if st.sidebar.button("♻️ Reset Score & Timer"):
    st.session_state.score = 0
    st.session_state.card_index = 0
    st.session_state.start_time = time.time()
    st.rerun()

# Auto-refresh helper for the timer
time.sleep(1)
st.rerun()
