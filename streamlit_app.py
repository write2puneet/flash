import streamlit as st
import time
from datetime import datetime

# --- CONFIGURATION & BIRTHDAY LOGIC ---
st.set_page_config(page_title="Aanya's Study Hub", page_icon="🎂")

# Birthday logic: Only shows until end of 23 April 2026
# (Note: Python uses YYYY, M, D)
target_date = datetime(2026, 4, 23, 23, 59)
is_birthday_period = datetime.now() <= target_date

if is_birthday_period:
    st.balloons()
    st.markdown("""
        <div style="background-color: #FFD700; padding: 25px; border-radius: 20px; text-align: center; border: 5px solid #FF69B4;">
            <h1 style="color: #FF1493; margin: 0;">🎉 Happy 13th Birthday, Aanya! 🎂</h1>
            <p style="font-size: 1.4rem; color: #333;">Welcome to the <b>Teen Club</b>! Good luck with your Grade 8 journey! ✨</p>
        </div>
    """, unsafe_allow_html=True)

# --- ACTUAL CONTENT DATASET ---
# I have started the first set for each. You can add more questions to the lists below.
subjects_data = {
    "Mathamatics": [
        {"q": "What is the square root of 144?", "a": "12"},
        {"q": "Simplify: 3x + 5x - 2x", "a": "6x"},
        {"q": "Calculate: -5 + (-8)", "a": "-13"},
        {"q": "What is the value of any number to the power of 0?", "a": "1"},
        {"q": "Solve for x: 2x = 20", "a": "x = 10"},
        {"q": "What is the HCF of 12 and 18?", "a": "6"},
        {"q": "What is 15% of 200?", "a": "30"},
        {"q": "Convert 3/4 to a percentage.", "a": "75%"},
        {"q": "What is the sum of angles in a triangle?", "a": "180 degrees"},
        {"q": "Find the area of a square with side 5cm.", "a": "25 cm²"}
        # ... Add 90 more questions here for Sets 2-10
    ],
    "Natural Sciences": [
        {"q": "What is the smallest unit of life?", "a": "The Cell"},
        {"q": "Which gas do plants absorb for photosynthesis?", "a": "Carbon Dioxide"},
        {"q": "What is the kinetic energy?", "a": "Energy of motion"},
        {"q": "Name the three states of matter.", "a": "Solid, Liquid, Gas"},
        {"q": "What part of the cell contains DNA?", "a": "The Nucleus"},
        {"q": "What is the pH of pure water?", "a": "7 (Neutral)"},
        {"q": "Which planet is known as the Red Planet?", "a": "Mars"},
        {"q": "What instrument measures atmospheric pressure?", "a": "Barometer"},
        {"q": "What is the process of a liquid turning into a gas?", "a": "Evaporation"},
        {"q": "What is the center of an atom called?", "a": "The Nucleus"}
    ],
    "Afrikaans": [
        {"q": "Vertaal: 'I am happy'", "a": "Ek is gelukkig"},
        {"q": "Wat is die meervoud van 'Kind'?", "a": "Kinders"},
        {"q": "Gee die verlede tyd: 'Ek eet 'n appel'", "a": "Ek het 'n appel geëet"},
        {"q": "Wat is 'n 'Sambreel' in Engels?", "a": "Umbrella"},
        {"q": "Wat is die teenoorgestelde van 'Groot'?", "a": "Klein"},
        {"q": "Vertaal: 'Yellow'", "a": "Geel"},
        {"q": "Noem 'n vrug wat rooi is.", "a": "Appel / Aarbei"},
        {"q": "Wat beteken 'Goeienaand'?", "a": "Good evening"},
        {"q": "Vertaal: 'School'", "a": "Skool"},
        {"q": "Wat is 'Maandag' in Engels?", "a": "Monday"}
    ],
    "English": [
        {"q": "What is a word that describes a noun?", "a": "Adjective"},
        {"q": "Identify the verb: 'The cat ran away.'", "a": "Ran"},
        {"q": "What is a synonym for 'Huge'?", "a": "Gigantic / Large"},
        {"q": "What is an antonym for 'Start'?", "a": "Finish / End"},
        {"q": "What punctuation mark is used for a pause?", "a": "Comma"},
        {"q": "Is 'and' a conjunction or a preposition?", "a": "Conjunction"},
        {"q": "What do you call a person who writes a book?", "a": "Author"},
        {"q": "What is a figure of speech that uses 'like' or 'as'?", "a": "Simile"},
        {"q": "Correct the spelling: 'Defenately'", "a": "Definitely"},
        {"q": "What is a group of lines in a poem called?", "a": "Stanza"}
    ],
    "EMS": [
        {"q": "What does EMS stand for?", "a": "Economic and Management Sciences"},
        {"q": "What is a formal business?", "a": "A business registered with the government"},
        {"q": "What is the medium of exchange in SA?", "a": "The Rand (ZAR)"},
        {"q": "What is a 'need'?", "a": "Something essential for survival"},
        {"q": "What is a 'want'?", "a": "Something we desire but can live without"},
        {"q": "Who is the owner of a business?", "a": "Entrepreneur"},
        {"q": "What is a budget?", "a": "A plan for income and spending"},
        {"q": "What is income?", "a": "Money received from work or investments"},
        {"q": "What is an expense?", "a": "Money spent on goods or services"},
        {"q": "What does VAT stand for?", "a": "Value Added Tax"}
    ],
    "Geography": [
        {"q": "Which continent is South Africa in?", "a": "Africa"},
        {"q": "What is the largest ocean in the world?", "a": "Pacific Ocean"},
        {"q": "What line divides the Earth into North and South?", "a": "The Equator"},
        {"q": "Name one of the three capital cities of SA.", "a": "Pretoria / Cape Town / Bloemfontein"},
        {"q": "What is a high, flat area of land called?", "a": "Plateau"},
        {"q": "What is the direction between North and East?", "a": "North-East"},
        {"q": "What is a map's 'key' used for?", "a": "To explain symbols"},
        {"q": "What is the capital of Gauteng?", "a": "Johannesburg"},
        {"q": "What do we call moving from one country to another?", "a": "Migration"},
        {"q": "What is the main river in South Africa?", "a": "Orange River"}
    ],
    "History": [
        {"q": "Who was the first black president of SA?", "a": "Nelson Mandela"},
        {"q": "In what year was the first democratic election in SA?", "a": "1994"},
        {"q": "What was the system of racial segregation in SA called?", "a": "Apartheid"},
        {"q": "Who is the 'Father of the Nation' in SA?", "a": "Nelson Mandela"},
        {"q": "What is a primary source in history?", "a": "An original object or document from the time"},
        {"q": "Which famous leader was imprisoned on Robben Island?", "a": "Nelson Mandela"},
        {"q": "What does the ANC stand for?", "a": "African National Congress"},
        {"q": "What happened on June 16, 1976?", "a": "Soweto Uprising"},
        {"q": "Who was the first European to sail around the Cape?", "a": "Bartholomeu Dias"},
        {"q": "What is a 'Heritage Site'?", "a": "A place of cultural or historical importance"}
    ],
    "Life Orientation": [
        {"q": "What is self-concept?", "a": "How you see yourself"},
        {"q": "What is a right in the Constitution?", "a": "Something you are allowed to be, do or have"},
        {"q": "What is a responsibility?", "a": "A duty to take care of something"},
        {"q": "Why is hygiene important?", "a": "To prevent the spread of germs and illness"},
        {"q": "What is empathy?", "a": "Understanding how someone else feels"},
        {"q": "Name a healthy way to deal with stress.", "a": "Exercise / Meditation / Talking to someone"},
        {"q": "What is bullying?", "a": "Repeatedly hurting someone on purpose"},
        {"q": "What is the legal age to vote in SA?", "a": "18"},
        {"q": "What does a balanced diet include?", "a": "Fruits, vegetables, protein, and grains"},
        {"q": "Why is teamwork important?", "a": "It helps achieve goals faster and better"}
    ],
    "Technology": [
        {"q": "What is a lever used for?", "a": "To lift heavy loads with less effort"},
        {"q": "What is the 'input' in a system?", "a": "What goes into the system"},
        {"q": "Name a natural material.", "a": "Wood / Cotton / Leather"},
        {"q": "What is a drawing called that shows 3D?", "a": "Isometric drawing"},
        {"q": "What is a bridge that can move called?", "a": "Drawbridge"},
        {"q": "What is an alloy?", "a": "A mixture of two or more metals"},
        {"q": "What is the purpose of a gears?", "a": "To change speed or direction of motion"},
        {"q": "What is a pneumatic system?", "a": "A system that uses compressed air"},
        {"q": "What do we call the rough sketch of a design?", "a": "Concept sketch"},
        {"q": "What is a pulley?", "a": "A wheel with a grooved rim for a rope"}
    ]
}

# --- NAVIGATION ---
st.sidebar.title("⭐ Aanya's Study Hub")
subj = st.sidebar.selectbox("Subject", list(subjects_data.keys()))

# Placeholder for Sets: Currently the 10 questions above are "Set 1"
# In a full app, you would add 10 questions for each set in the lists above.
set_num = st.sidebar.selectbox("Select Set", [f"Set {i+1}" for i in range(10)])

# --- SESSION STATE ---
if "card_idx" not in st.session_state:
    st.session_state.card_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "flipped" not in st.session_state:
    st.session_state.flipped = False

# Reset on change
if "last_nav" not in st.session_state or st.session_state.last_nav != (subj, set_num):
    st.session_state.card_idx = 0
    st.session_state.score = 0
    st.session_state.flipped = False
    st.session_state.last_nav = (subj, set_num)
    st.rerun()

# Load current card (Looping back to 0 if the list is shorter than 10)
all_subj_cards = subjects_data[subj]
current_card = all_subj_cards[st.session_state.card_idx % len(all_subj_cards)]

# --- UI ---
st.write(f"### {subj} | {set_num}")
st.metric("Set Score", f"{st.session_state.score}/10")
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
    st.write("---")
    st.write("Did you get it right?")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Yes"):
            st.session_state.score += 1
            st.session_state.card_idx += 1
            st.session_state.flipped = False
            st.rerun()
    with c2:
        if st.button("❌ No"):
            st.session_state.card_idx += 1
            st.session_state.flipped = False
            st.rerun()

# Sidebar Reset
if st.sidebar.button("Restart Level"):
    st.session_state.score = 0
    st.session_state.card_idx = 0
    st.session_state.flipped = False
    st.rerun()

# Refresh timer
time.sleep(1)
st.rerun()
