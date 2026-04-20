import streamlit as st

# App Configuration
st.set_page_config(page_title="Grade 8 SA Flashcards", page_icon="🇿🇦")

# Curriculum Data
data = {
    "Level 1 (Foundation)": [
        {"q": "What is the capital city of Gauteng?", "a": "Johannesburg"},
        {"q": "In EMS, what does 'VAT' stand for?", "a": "Value Added Tax"},
        {"q": "Which ocean is on the east coast of South Africa?", "a": "The Indian Ocean"}
    ],
    "Level 2 (Intermediate)": [
        {"q": "Who was the first democratically elected president of SA?", "a": "Nelson Mandela"},
        {"q": "What is the boiling point of pure water at sea level?", "a": "100 Degrees Celsius"},
        {"q": "True or False: A 'Need' is something you must have to survive.", "a": "True"}
    ],
    "Level 3 (Exam Prep)": [
        {"q": "Explain the law of demand in Economics.", "a": "As price increases, quantity demanded decreases."},
        {"q": "What are the three branches of the SA government?", "a": "Legislative, Executive, and Judicial"},
        {"q": "What is the chemical symbol for Gold?", "a": "Au"}
    ]
}

# Sidebar for Level Selection
st.sidebar.title("📚 Study Settings")
level = st.sidebar.selectbox("Choose Your Level", list(data.keys()))

# Initialize session state for tracking
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "flipped" not in st.session_state:
    st.session_state.flipped = False

# Load cards for selected level
cards = data[level]

# UI Layout
st.title(f"🇿🇦 Grade 8 Study: {level}")
st.progress((st.session_state.card_index + 1) / len(cards))

current_card = cards[st.session_state.card_index]

# Flashcard Display
st.markdown("---")
if not st.session_state.flipped:
    st.subheader("Question:")
    st.info(current_card["q"])
    if st.button("🔍 Flip to see Answer"):
        st.session_state.flipped = True
        st.rerun()
else:
    st.subheader("Answer:")
    st.success(current_card["a"])
    if st.button("⬅️ Back to Question"):
        st.session_state.flipped = False
        st.rerun()
st.markdown("---")

# Navigation
col1, col2 = st.columns(2)
with col1:
    st.write(f"Card {st.session_state.card_index + 1} of {len(cards)}")
with col2:
    if st.button("Next Card ➡️"):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(cards)
        st.session_state.flipped = False
        st.rerun()
