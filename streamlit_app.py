import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="Grade 8 Maths Flashcards 🇿🇦", page_icon="🔢")

# 100-Card Mathematics Dataset (CAPS Aligned)
data = {
    "Level 1: Foundation (34 Cards)": [
        {"q": "What are natural numbers?", "a": "1, 2, 3..."},
        {"q": "What are whole numbers?", "a": "0, 1, 2..."},
        {"q": "What is an integer?", "a": "Positive or negative whole number"},
        {"q": "What is a prime number?", "a": "Number with only two factors"},
        {"q": "What is the HCF of 12 and 18?", "a": "6"},
        {"q": "What is the LCM of 4 and 6?", "a": "12"},
        {"q": "Square root of 144?", "a": "12"},
        {"q": "Cube of 3?", "a": "27"},
        {"q": "Identity property of 0 in addition?", "a": "Number stays the same"},
        {"q": "Identity property of 1 in multiplication?", "a": "Number stays the same"},
        {"q": "What is a + b = b + a called?", "a": "Commutative Property"},
        {"q": "What is a(b + c) = ab + ac called?", "a": "Distributive Property"},
        {"q": "Sum of angles in a triangle?", "a": "180"},
        {"q": "Sum of angles in a quadrilateral?", "a": "360"},
        {"q": "An angle of 90 degrees is called?", "a": "Right angle"},
        {"q": "An angle less than 90 degrees is?", "a": "Acute angle"},
        {"q": "An angle between 90 and 180 degrees is?", "a": "Obtuse angle"},
        {"q": "An angle between 180 and 360 degrees is?", "a": "Reflex angle"},
        {"q": "Formula for Area of a Rectangle?", "a": "l x b"},
        {"q": "Formula for Perimeter of a Square?", "a": "4s"},
        {"q": "What is a variable?", "a": "A letter representing a value"},
        {"q": "Simplify: x + x", "a": "2x"},
        {"q": "Simplify: x * x", "a": "x^2"},
        {"q": "15% of 100?", "a": "15"},
        {"q": "1/2 as a percentage?", "a": "50%"},
        {"q": "0,75 as a fraction?", "a": "3/4"},
        {"q": "Reciprocal of 2/3?", "a": "3/2"},
        {"q": "Is 1 a prime number?", "a": "No"},
        {"q": "Additive inverse of -5?", "a": "5"},
        {"q": "Multiplicative inverse of 4?", "a": "1/4"},
        {"q": "Any number raised to power 0?", "a": "1"},
        {"q": "10 squared?", "a": "100"},
        {"q": "What is a ratio?", "a": "Comparison of quantities"},
        {"q": "Simplify 10:25", "a": "2:5"}
    ],
    "Level 2: Intermediate (33 Cards)": [
        {"q": "Solve for x: x + 5 = 12", "a": "7"},
        {"q": "Solve for x: 2x = 10", "a": "5"},
        {"q": "Simplify: 3x + 4x - 2x", "a": "5x"},
        {"q": "Calculate: -5 + (-3)", "a": "-8"},
        {"q": "Calculate: -10 - (-4)", "a": "-6"},
        {"q": "Calculate: (-2) * (-5)", "a": "10"},
        {"q": "20% of R250?", "a": "50"},
        {"q": "Increase R100 by 15%", "a": "115"},
        {"q": "Decrease 80 by 10%", "a": "72"},
        {"q": "Divide R120 in ratio 1:2 (Smaller Part)", "a": "40"},
        {"q": "Divide R120 in ratio 1:2 (Larger Part)", "a": "80"},
        {"q": "Missing value: 2/5 = x/20", "a": "8"},
        {"q": "Area of triangle: base 10, height 5", "a": "25"},
        {"q": "Perimeter of square with area 64", "a": "32"},
        {"q": "Simplify: (2^3)^2", "a": "64"},
        {"q": "Simplify: a^5 / a^2", "a": "a^3"},
        {"q": "Calculate: 3 + 2 * 5", "a": "13"},
        {"q": "Solve: 3x - 1 = 11", "a": "4"},
        {"q": "If a=2, b=3, find 2a + b", "a": "7"},
        {"q": "Supplement of 70 degrees?", "a": "110"},
        {"q": "Complement of 40 degrees?", "a": "50"},
        {"q": "Define equilateral triangle", "a": "All sides equal"},
        {"q": "Define isosceles triangle", "a": "Two sides equal"},
        {"q": "Third angle of triangle if others are 50 and 60?", "a": "70"},
        {"q": "Volume of cube with side 3cm?", "a": "27"},
        {"q": "Simplify: 2(x + 3)", "a": "2x + 6"},
        {"q": "Solve for x: x/4 = 3", "a": "12"},
        {"q": "Pattern: 2, 4, 8, 16...", "a": "32"},
        {"q": "Pattern: 1, 4, 9, 16...", "a": "25"},
        {"q": "0,005 in scientific notation?", "a": "5x10^-3"},
        {"q": "Square root of 0,25?", "a": "0,5"},
        {"q": "Calculate: 1/4 + 1/2", "a": "3/4"},
        {"q": "Calculate: 3/4 * 8", "a": "6"}
    ],
    "Level 3: Exam Prep (33 Cards)": [
        {"q": "Solve: 3(x - 2) = 9", "a": "5"},
        {"q": "Solve: 2x + 4 = x + 10", "a": "6"},
        {"q": "Simplify: (3x^2y)(2xy^3)", "a": "6x^3y^4"},
        {"q": "Simplify: 12a^3b^2 / 4ab", "a": "3a^2b"},
        {"q": "Hypotenuse of triangle with sides 3 and 4?", "a": "5"},
        {"q": "Pythagoras: x^2 = 5^2 + 12^2. Solve x.", "a": "13"},
        {"q": "Area of circle radius 7 (pi=22/7)", "a": "154"},
        {"q": "Circumference of circle diameter 14 (pi=22/7)", "a": "44"},
        {"q": "Shirt R200 excl 15% VAT. Total price?", "a": "230"},
        {"q": "Simple interest: R1000, 5% p.a., 3 years", "a": "150"},
        {"q": "Factorize: 3x + 9", "a": "3(x+3)"},
        {"q": "Simplify: -(2x - 5)", "a": "-2x+5"},
        {"q": "Solve for x: 2/x = 4/10", "a": "5"},
        {"q": "Median of: 2, 5, 7, 10, 11", "a": "7"},
        {"q": "Mean of: 10, 20, 30", "a": "20"},
        {"q": "Mode of: 1, 2, 2, 3, 4", "a": "2"},
        {"q": "Range of: 5, 12, 18, 2, 20", "a": "18"},
        {"q": "Prob of red ball (3 red, 2 blue)", "a": "3/5"},
        {"q": "Gradient of horizontal line?", "a": "0"},
        {"q": "In y = mx + c, what is c?", "a": "y-intercept"},
        {"q": "Simplify: sqrt(64 + 36)", "a": "10"},
        {"q": "Solve: x^2 = 49", "a": "7"},
        {"q": "Simplify: 2x^0 + 5", "a": "7"},
        {"q": "72 km/h to m/s?", "a": "20"},
        {"q": "Surface area of cube side 2cm?", "a": "24"},
        {"q": "Solve: 1/2x = 10", "a": "20"},
        {"q": "Exterior angle if interior opposites are 40 and 60?", "a": "100"},
        {"q": "Simplify: 3(x^2 - 1) - 2x^2", "a": "x^2-3"},
        {"q": "R90 after 10% discount. Original price?", "a": "100"},
        {"q": "3 men build wall in 4 days. 6 men?", "a": "2"},
        {"q": "Volume of cylinder: r=7, h=10 (pi=22/7)", "a": "1540"},
        {"q": "Solve: 5x - 2 = 3x + 8", "a": "5"},
        {"q": "Factorize: x^2 + 5x", "a": "x(x+5)"}
    ]
}

# Session State Initialization
if "card_idx" not in st.session_state:
    st.session_state.card_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "flipped" not in st.session_state:
    st.session_state.flipped = False

# Sidebar
st.sidebar.title("📚 Maths Prep")
level = st.sidebar.selectbox("Choose Level", list(data.keys()))

# Reset logic for level change
if "current_level" not in st.session_state or st.session_state.current_level != level:
    st.session_state.card_idx = 0
    st.session_state.score = 0
    st.session_state.current_level = level
    st.session_state.flipped = False
    st.session_state.start_time = time.time()

cards = data[level]
current_card = cards[st.session_state.card_idx]

# UI Header
st.title("🇿🇦 Grade 8 Maths Flashcards")
col_score, col_time = st.columns(2)
col_score.metric("Score", f"{st.session_state.score}/{len(cards)}")
elapsed = int(time.time() - st.session_state.start_time)
col_time.metric("Timer", f"{elapsed}s")

st.progress((st.session_state.card_idx + 1) / len(cards))

# Flashcard Area
st.markdown("---")
st.subheader(f"Question {st.session_state.card_idx + 1}:")
st.info(current_card["q"])

if not st.session_state.flipped:
    if st.button("🔍 SHOW ANSWER"):
        st.session_state.flipped = True
        st.rerun()
else:
    st.success(f"### Answer: {current_card['a']}")
    st.write("Did you get it right?")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Yes (Correct)"):
            st.session_state.score += 1
            st.session_state.card_idx = (st.session_state.card_idx + 1) % len(cards)
            st.session_state.flipped = False
            st.rerun()
    with c2:
        if st.button("❌ No (Incorrect)"):
            st.session_state.card_idx = (st.session_state.card_idx + 1) % len(cards)
            st.session_state.flipped = False
            st.rerun()

# Reset Option
if st.sidebar.button("Restart Level"):
    st.session_state.score = 0
    st.session_state.card_idx = 0
    st.session_state.start_time = time.time()
    st.session_state.flipped = False
    st.rerun()

# Refresh timer
time.sleep(1)
st.rerun()
