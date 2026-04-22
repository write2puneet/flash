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
        # SET 1: Whole Numbers & Integers
        {"q": "What is the HCF of 12 and 18?", "a": "6"},
        {"q": "What is the LCM of 4 and 6?", "a": "12"},
        {"q": "Calculate: -5 + (-8)", "a": "-13"},
        {"q": "Calculate: -10 - (-4)", "a": "-6"},
        {"q": "What is the product of -3 and -4?", "a": "12"},
        {"q": "What is a prime number?", "a": "A number with exactly two factors (1 and itself)"},
        {"q": "Is 1 a prime number?", "a": "No"},
        {"q": "List the first three prime numbers.", "a": "2, 3, 5"},
        {"q": "What is the square of 9?", "a": "81"},
        {"q": "What is the square root of 144?", "a": "12"},

        # SET 2: Exponents & Roots
        {"q": "What is the value of any non-zero number to the power of 0?", "a": "1"},
        {"q": "Simplify: x³ × x⁴", "a": "x⁷"},
        {"q": "Simplify: (y²)³", "a": "y⁶"},
        {"q": "Simplify: a⁵ ÷ a²", "a": "a³"},
        {"q": "What is the cube of 3?", "a": "27"},
        {"q": "What is the cube root of 64?", "a": "4"},
        {"q": "Calculate: √100 - √36", "a": "4 (10 - 6)"},
        {"q": "What is 10 to the power of 4?", "a": "10 000"},
        {"q": "Write 0,005 in scientific notation.", "a": "5 × 10⁻³"},
        {"q": "Calculate: (-2)³", "a": "-8"},

        # SET 3: Fractions & Decimals
        {"q": "Convert 3/4 to a percentage.", "a": "75%"},
        {"q": "Convert 0,125 to a common fraction.", "a": "1/8"},
        {"q": "Calculate: 1/2 + 1/3", "a": "5/6"},
        {"q": "Calculate: 3/4 × 8", "a": "6"},
        {"q": "What is the reciprocal of 2/5?", "a": "5/2"},
        {"q": "Calculate: 10% of R250.", "a": "R25"},
        {"q": "Convert 0,7 to a percentage.", "a": "70%"},
        {"q": "Increase 80 by 25%.", "a": "100"},
        {"q": "Decrease R120 by 10%.", "a": "R108"},
        {"q": "What is 1/3 of 90?", "a": "30"},

        # SET 4: Ratios & Finance
        {"q": "Simplify the ratio 10:25.", "a": "2:5"},
        {"q": "Divide R120 in the ratio 1:2.", "a": "R40 and R80"},
        {"q": "If 3 apples cost R15, how much for 5?", "a": "R25"},
        {"q": "What does ZAR stand for?", "a": "South African Rand"},
        {"q": "What is VAT in South Africa?", "a": "15%"},
        {"q": "Calculate the VAT on a R100 item.", "a": "R15"},
        {"q": "If a shirt costs R230 including 15% VAT, what was the price before VAT?", "a": "R200"},
        {"q": "Calculate simple interest on R1000 at 10% for 2 years.", "a": "R200"},
        {"q": "What is profit?", "a": "Income minus Expenses"},
        {"q": "What is a budget?", "a": "A plan for income and spending"},

        # SET 5: Numeric & Geometric Patterns
        {"q": "Complete the pattern: 2; 4; 6; 8; ...", "a": "10"},
        {"q": "Complete the pattern: 1; 4; 9; 16; ...", "a": "25 (Square numbers)"},
        {"q": "Complete the pattern: 3; 9; 27; ...", "a": "81 (Multiply by 3)"},
        {"q": "In the pattern Tn = 2n + 1, find T5.", "a": "11"},
        {"q": "What is a constant difference?", "a": "When the same number is added each time"},
        {"q": "Find the general rule (Tn) for: 5; 10; 15; 20...", "a": "Tn = 5n"},
        {"q": "What is the next term: 100; 90; 80; ...", "a": "70"},
        {"q": "Complete the pattern: 1; 8; 27; 64; ...", "a": "125 (Cube numbers)"},
        {"q": "If Tn = n², find T12.", "a": "144"},
        {"q": "Find the 10th term in the sequence: 2; 4; 6...", "a": "20"},

        # SET 6: Algebraic Expressions
        {"q": "What is a variable?", "a": "A letter representing an unknown value"},
        {"q": "Identify the coefficient in 5x².", "a": "5"},
        {"q": "Identify the exponent in 3y⁴.", "a": "4"},
        {"q": "Simplify: 2a + 3b + 4a - b", "a": "6a + 2b"},
        {"q": "Simplify: 2(x + 3)", "a": "2x + 6"},
        {"q": "Find the value of 3x - 2 if x = 4.", "a": "10"},
        {"q": "Simplify: -(x - 5)", "a": "-x + 5"},
        {"q": "Expand: (x + 2)(x + 3)", "a": "x² + 5x + 6"},
        {"q": "Simplify: 10x² ÷ 2x", "a": "5x"},
        {"q": "What is a binomial?", "a": "An algebraic expression with two terms"},

        # SET 7: Algebraic Equations
        {"q": "Solve for x: x + 7 = 15", "a": "x = 8"},
        {"q": "Solve for x: 3x = 21", "a": "x = 7"},
        {"q": "Solve for x: x/2 = 10", "a": "x = 20"},
        {"q": "Solve for x: 2x - 4 = 10", "a": "x = 7"},
        {"q": "Solve for x: 5x + 2 = 3x + 8", "a": "x = 3"},
        {"q": "Solve for x: 2(x - 1) = 8", "a": "x = 5"},
        {"q": "Solve for x: x² = 49", "a": "x = 7 or -7"},
        {"q": "Solve for x: 10 - x = 4", "a": "x = 6"},
        {"q": "Solve for x: 3x + 5 = 20", "a": "x = 5"},
        {"q": "What is an equation?", "a": "A mathematical statement that two things are equal"},

        # SET 8: Geometry (Lines & Angles)
        {"q": "What is the sum of angles on a straight line?", "a": "180°"},
        {"q": "What are vertically opposite angles?", "a": "Angles opposite each other when two lines cross (they are equal)"},
        {"q": "What is the sum of angles around a point?", "a": "360°"},
        {"q": "What do we call angles that add up to 90°?", "a": "Complementary angles"},
        {"q": "What do we call angles that add up to 180°?", "a": "Supplementary angles"},
        {"q": "In parallel lines, which angles form an 'F' shape?", "a": "Corresponding angles"},
        {"q": "In parallel lines, which angles form a 'Z' shape?", "a": "Alternate angles"},
        {"q": "In parallel lines, which angles form a 'U' shape?", "a": "Co-interior angles"},
        {"q": "What is the sum of interior angles of a triangle?", "a": "180°"},
        {"q": "Find the third angle if two angles are 50° and 60°.", "a": "70°"},

        # SET 9: Geometry (2D Shapes & Pythagoras)
        {"q": "What is an equilateral triangle?", "a": "A triangle with all sides and angles (60°) equal"},
        {"q": "What is an isosceles triangle?", "a": "A triangle with two equal sides and two equal angles"},
        {"q": "What is the theorem of Pythagoras?", "a": "a² + b² = c²"},
        {"q": "Find the hypotenuse if the other sides are 3 and 4.", "a": "5"},
        {"q": "What is a quadrilateral?", "a": "A 4-sided polygon"},
        {"q": "Name a quadrilateral with all sides equal but no right angles.", "a": "Rhombus"},
        {"q": "What is the area of a triangle?", "a": "1/2 × base × height"},
        {"q": "What is the perimeter of a circle called?", "a": "Circumference"},
        {"q": "Calculate the area of a circle with radius 7 (π=22/7).", "a": "154 units²"},
        {"q": "What is the sum of interior angles in a quadrilateral?", "a": "360°"},

        # SET 10: Data Handling & 3D Shapes
        {"q": "What is the mean?", "a": "The average (sum ÷ count)"},
        {"q": "What is the median?", "a": "The middle value in an ordered list"},
        {"q": "What is the mode?", "a": "The value that appears most often"},
        {"q": "What is the range?", "a": "Difference between highest and lowest values"},
        {"q": "What is probability?", "a": "The chance of an event happening"},
        {"q": "What is the probability of flipping heads on a coin?", "a": "1/2 or 0,5"},
        {"q": "How many faces does a cube have?", "a": "6"},
        {"q": "What is the formula for the volume of a rectangular prism?", "a": "L × B × H"},
        {"q": "If a cube has a side of 2cm, what is its volume?", "a": "8 cm³"},
        {"q": "What is a tally?", "a": "A mark used to count frequency"}
    ],
    "Natural Sciences": [
        # SET 1: Photosynthesis & Respiration
        {"q": "What gas do plants absorb during photosynthesis?", "a": "Carbon Dioxide"},
        {"q": "What gas is produced as a byproduct of photosynthesis?", "a": "Oxygen"},
        {"q": "In which part of the plant cell does photosynthesis occur?", "a": "Chloroplasts"},
        {"q": "What is the green pigment that traps sunlight?", "a": "Chlorophyll"},
        {"q": "What form of energy is stored in glucose?", "a": "Chemical Potential Energy"},
        {"q": "What is the primary purpose of cellular respiration?", "a": "To release energy from food"},
        {"q": "Where in the cell does respiration happen?", "a": "Mitochondria"},
        {"q": "What is the sugar produced during photosynthesis called?", "a": "Glucose"},
        {"q": "Do plants respire only at night?", "a": "No, they respire all the time"},
        {"q": "Write the word equation for respiration.", "a": "Glucose + Oxygen -> Carbon Dioxide + Water + Energy"},

        # SET 2: Interactions in Ecosystems
        {"q": "What do we call a living thing in an ecosystem?", "a": "Biotic factor"},
        {"q": "What do we call non-living parts of an ecosystem (like soil)?", "a": "Abiotic factor"},
        {"q": "What is a 'Producer'?", "a": "An organism that makes its own food (plants)"},
        {"q": "What is a 'Decomposer'?", "a": "Organisms that break down dead matter (fungi/bacteria)"},
        {"q": "What do we call an animal that eats only plants?", "a": "Herbivore"},
        {"q": "What do we call an animal that eats only meat?", "a": "Carnivore"},
        {"q": "What is a 'Consumer'?", "a": "An organism that eats other organisms for energy"},
        {"q": "What is a 'Scavenger'?", "a": "An animal that eats already dead animals"},
        {"q": "What is a food web?", "a": "Interconnected food chains in an ecosystem"},
        {"q": "What happens to energy as it moves up a food chain?", "a": "Most is lost (only 10% is passed on)"},

        # SET 3: Atoms and Elements
        {"q": "What is the smallest building block of matter?", "a": "The Atom"},
        {"q": "Name the three sub-atomic particles.", "a": "Protons, Neutrons, Electrons"},
        {"q": "What is the charge of a Proton?", "a": "Positive (+)"},
        {"q": "What is the charge of an Electron?", "a": "Negative (-)"},
        {"q": "What is the charge of a Neutron?", "a": "Neutral (0)"},
        {"q": "Where are protons and neutrons located?", "a": "In the Nucleus"},
        {"q": "What is an 'Element'?", "a": "A pure substance made of only one type of atom"},
        {"q": "What is the chemical symbol for Gold?", "a": "Au"},
        {"q": "What is the chemical symbol for Iron?", "a": "Fe"},
        {"q": "How are elements organized in Science?", "a": "On the Periodic Table"},

        # SET 4: The Periodic Table
        {"q": "What is the atomic number of an element?", "a": "The number of protons in its nucleus"},
        {"q": "What is the symbol for Hydrogen?", "a": "H"},
        {"q": "What is the symbol for Oxygen?", "a": "O"},
        {"q": "What are the horizontal rows on the Periodic Table called?", "a": "Periods"},
        {"q": "What are the vertical columns on the Periodic Table called?", "a": "Groups"},
        {"q": "Which group contains the Noble Gases?", "a": "Group 18"},
        {"q": "Name the element with the symbol Na.", "a": "Sodium"},
        {"q": "Name the element with the symbol C.", "a": "Carbon"},
        {"q": "Where are metals found on the Periodic Table?", "a": "The left and center"},
        {"q": "Where are non-metals found on the Periodic Table?", "a": "The far right"},

        # SET 5: Particle Model of Matter
        {"q": "What are the three states of matter?", "a": "Solid, Liquid, Gas"},
        {"q": "In which state are particles packed most tightly?", "a": "Solid"},
        {"q": "In which state do particles move most freely?", "a": "Gas"},
        {"q": "What is the process of a solid turning into a liquid?", "a": "Melting"},
        {"q": "What is the process of a liquid turning into a gas?", "a": "Evaporation / Boiling"},
        {"q": "What is the process of a gas turning into a liquid?", "a": "Condensation"},
        {"q": "What is the process of a liquid turning into a solid?", "a": "Freezing / Solidification"},
        {"q": "What is 'Diffusion'?", "a": "Movement of particles from high to low concentration"},
        {"q": "Why can gases be compressed?", "a": "There are large spaces between the particles"},
        {"q": "What happens to particles when they are heated?", "a": "They gain kinetic energy and move faster"},

        # SET 6: Chemical Reactions
        {"q": "What is a 'Compound'?", "a": "Two or more different elements chemically bonded"},
        {"q": "What is the chemical formula for Water?", "a": "H2O"},
        {"q": "What is the chemical formula for Carbon Dioxide?", "a": "CO2"},
        {"q": "In a chemical equation, what do we call the starting substances?", "a": "Reactants"},
        {"q": "In a chemical equation, what do we call the ending substances?", "a": "Products"},
        {"q": "What is a 'Mixture'?", "a": "Substances physically mixed but not chemically bonded"},
        {"q": "What is the chemical formula for Table Salt?", "a": "NaCl"},
        {"q": "Can a compound be separated by physical means (like filtering)?", "a": "No, only by chemical reactions"},
        {"q": "What does a subscript (the small number) in a formula tell us?", "a": "The number of atoms of that element"},
        {"q": "What is the name for CO?", "a": "Carbon Monoxide"},

        # SET 7: Static Electricity
        {"q": "What is static electricity?", "a": "The build-up of electric charge on a surface"},
        {"q": "What happens when two like charges (e.g., + and +) meet?", "a": "They repel each other"},
        {"q": "What happens when two opposite charges meet?", "a": "They attract each other"},
        {"q": "How can an object become negatively charged?", "a": "By gaining electrons"},
        {"q": "What do we call a material that does NOT allow electricity to flow?", "a": "Insulator"},
        {"q": "Name a common insulator.", "a": "Plastic, rubber, or glass"},
        {"q": "What do we call a material that allows electricity to flow easily?", "a": "Conductor"},
        {"q": "Why does your hair stand up after rubbing a balloon on it?", "a": "Static discharge / Repelling like charges"},
        {"q": "What is a massive natural example of static discharge?", "a": "Lightning"},
        {"q": "True or False: Only electrons can move between atoms during friction.", "a": "True"},

        # SET 8: Energy and Circuits
        {"q": "What is 'Current'?", "a": "The rate of flow of charge"},
        {"q": "What is the unit of measurement for Current?", "a": "Amperes (A)"},
        {"q": "What instrument measures current?", "a": "Ammeter"},
        {"q": "What is 'Potential Difference'?", "a": "The work done per unit charge (Voltage)"},
        {"q": "What is the unit for Potential Difference?", "a": "Volts (V)"},
        {"q": "What instrument measures voltage?", "a": "Voltmeter"},
        {"q": "What is 'Resistance'?", "a": "A material's opposition to the flow of current"},
        {"q": "What is the unit for Resistance?", "a": "Ohms (Ω)"},
        {"q": "What is the purpose of a resistor in a circuit?", "a": "To control/reduce the flow of current"},
        {"q": "What is an LED?", "a": "Light Emitting Diode"},

        # SET 9: Series and Parallel Circuits
        {"q": "How many paths for current are there in a series circuit?", "a": "One single path"},
        {"q": "In a series circuit, if one bulb breaks, what happens to the others?", "a": "They all go out"},
        {"q": "What is a parallel circuit?", "a": "A circuit with more than one path for current"},
        {"q": "Where are parallel circuits used in everyday life?", "a": "In houses / buildings"},
        {"q": "In a series circuit, does the current stay the same everywhere?", "a": "Yes"},
        {"q": "In a parallel circuit, does the voltage stay the same across all branches?", "a": "Yes"},
        {"q": "What is a 'Short Circuit'?", "a": "A low-resistance path that bypasses the load"},
        {"q": "What is the purpose of a fuse?", "a": "To break the circuit if the current gets too high"},
        {"q": "What is a circuit breaker?", "a": "An automatic switch that stops current during an overload"},
        {"q": "Name a source of energy for a circuit.", "a": "Cell or Battery"},

        # SET 10: Visible Light and Solar System
        {"q": "Does light travel in straight lines?", "a": "Yes"},
        {"q": "What is the speed of light?", "a": "Approximately 300,000 km per second"},
        {"q": "What is 'Refraction'?", "a": "The bending of light as it enters a different medium"},
        {"q": "What is 'Reflection'?", "a": "Light bouncing off a surface"},
        {"q": "Which color of light is refracted the most in a prism?", "a": "Violet"},
        {"q": "Name the 8 planets in order from the sun.", "a": "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune"},
        {"q": "Which is the largest planet?", "a": "Jupiter"},
        {"q": "What is a 'Luminous' object?", "a": "An object that gives off its own light (like the Sun)"},
        {"q": "What do we call the path a planet takes around the sun?", "a": "Orbit"},
        {"q": "How long does it take for Earth to complete one orbit?", "a": "365 and a quarter days"}
    ],
    "Afrikaans": [
        # SET 1: Basiese Woordeskat (Basic Vocabulary)
        {"q": "Vertaal: 'I am happy'", "a": "Ek is gelukkig"},
        {"q": "Wat is die Afrikaanse woord vir 'Teacher'?", "a": "Onderwyser (man) / Onderwyseres (vrou)"},
        {"q": "Vertaal: 'Yellow'", "a": "Geel"},
        {"q": "Wat is 'Monday' in Afrikaans?", "a": "Maandag"},
        {"q": "Vertaal: 'Library'", "a": "Biblioteek"},
        {"q": "Wat is 'n 'Sambreel'?", "a": "An umbrella"},
        {"q": "Vertaal: 'Kitchen'", "a": "Kombuis"},
        {"q": "Wat noem ons 'n 'Friend'?", "a": "Vriend (man) / Vriendin (vrou)"},
        {"q": "Vertaal: 'Bread'", "a": "Brood"},
        {"q": "Wat is 'n 'Lughawe'?", "a": "An airport"},

        # SET 2: Meervoude (Plurals)
        {"q": "Wat is die meervoud van 'Kind'?", "a": "Kinders"},
        {"q": "Wat is die meervoud van 'Hond'?", "a": "Honde"},
        {"q": "Wat is die meervoud van 'Boek'?", "a": "Boeke"},
        {"q": "Wat is die meervoud van 'Vlieg'?", "a": "Vlieë"},
        {"q": "Wat is die meervoud van 'Oog'?", "a": "Oë"},
        {"q": "Wat is die meervoud van 'Man'?", "a": "Mans"},
        {"q": "Wat is die meervoud van 'Brief'?", "a": "Briewe"},
        {"q": "Wat is die meervoud van 'Stad'?", "a": "Stede"},
        {"q": "Wat is die meervoud van 'Heer'?", "a": "Here"},
        {"q": "Wat is die meervoud van 'Ma'?", "a": "Ma's"},

        # SET 3: Verkleinwoorde (Diminutives)
        {"q": "Wat is die verkleinwoord van 'Hond'?", "a": "Hondjie"},
        {"q": "Wat is die verkleinwoord van 'Kat'?", "a": "Katjie"},
        {"q": "Wat is die verkleinwoord van 'Boom'?", "a": "Boompie"},
        {"q": "Wat is die verkleinwoord van 'Stoel'?", "a": "Stoeltjie"},
        {"q": "Wat is die verkleinwoord van 'Man'?", "a": "Mannetjie"},
        {"q": "Wat is die verkleinwoord van 'Vinger'?", "a": "Vingertjie"},
        {"q": "Wat is die verkleinwoord van 'Huis'?", "a": "Huisie"},
        {"q": "Wat is die verkleinwoord van 'Blom'?", "a": "Blommetjie"},
        {"q": "Wat is die verkleinwoord van 'Brief'?", "a": "Briefie"},
        {"q": "Wat is die verkleinwoord van 'Koning'?", "a": "Koninkie"},

        # SET 4: Teenoorgesteldes (Antonyms)
        {"q": "Wat is die teenoorgestelde van 'Groot'?", "a": "Klein"},
        {"q": "Wat is die teenoorgestelde van 'Warm'?", "a": "Koud"},
        {"q": "Wat is die teenoorgestelde van 'Mooi'?", "a": "Lelik"},
        {"q": "Wat is die teenoorgestelde van 'Vinnig'?", "a": "Stadig"},
        {"q": "Wat is die teenoorgestelde van 'Arm'?", "a": "Ryk"},
        {"q": "Wat is die teenoorgestelde van 'Vroeg'?", "a": "Laat"},
        {"q": "Wat is die teenoorgestelde van 'Droog'?", "a": "Nat"},
        {"q": "Wat is die teenoorgestelde van 'Wild'?", "a": "Tam"},
        {"q": "Wat is die teenoorgestelde van 'Dood'?", "a": "Lewendig"},
        {"q": "Wat is die teenoorgestelde van 'Maklik'?", "a": "Moeilik"},

        # SET 5: Tye (Tenses - Verlede Tyd)
        {"q": "Verlede tyd: 'Ek eet 'n appel'", "a": "Ek het 'n appel geëet"},
        {"q": "Verlede tyd: 'Sy koop 'n rok'", "a": "Sy het 'n rok gekoop"},
        {"q": "Verlede tyd: 'Ons speel tennis'", "a": "Ons het tennis gespeel"},
        {"q": "Verlede tyd: 'Die kind huil'", "a": "Die kind het gehuil"},
        {"q": "Verlede tyd: 'Pa lees die koerant'", "a": "Pa het die koerant gelees"},
        {"q": "Wat gebeur met 'is' in die verlede tyd?", "a": "Dit word 'was'"},
        {"q": "Verlede tyd: 'Dit is koud'", "a": "Dit was koud"},
        {"q": "Wat gebeur met 'kan' in die verlede tyd?", "a": "Dit word 'kon'"},
        {"q": "Wat gebeur met 'moet' in die verlede tyd?", "a": "Dit word 'moes'"},
        {"q": "Waar staan die 'het' gewoonlik?", "a": "In die plek van die eerste werkwoord (V1)"},

        # SET 6: Tye (Tenses - Toekomende Tyd)
        {"q": "Toekomende tyd: 'Ek gaan huis toe'", "a": "Ek sal huis toe gaan"},
        {"q": "Toekomende tyd: 'Hulle swem in die see'", "a": "Hulle sal in die see swem"},
        {"q": "Toekomende tyd: 'Ons leer vir die toets'", "a": "Ons sal vir die toets leer"},
        {"q": "Toekomende tyd: 'Sy bak 'n koek'", "a": "Sy sal 'n koek bak"},
        {"q": "Toekomende tyd: 'Jy help vir ma'", "a": "Jy sal vir ma help"},
        {"q": "Waarheen skuif die werkwoord in die toekomende tyd?", "a": "Na die einde van die sin"},
        {"q": "Toekomende tyd: 'Dit reën vandag'", "a": "Dit sal vandag reën"},
        {"q": "Wat is die helpwerkwoord vir die toekomende tyd?", "a": "Sal"},
        {"q": "Toekomende tyd: 'Ek is moeg'", "a": "Ek sal moeg wees"},
        {"q": "Toekomende tyd: 'Hy het 'n hond'", "a": "Hy sal 'n hond hê"},

        # SET 7: STOMPI Reëls (Sentence Structure)
        {"q": "Waarvoor staan die 'S' in STOMPI?", "a": "Subjek (Onderwerp)"},
        {"q": "Waarvoor staan die 'T' in STOMPI?", "a": "Tyd (Time)"},
        {"q": "Waarvoor staan die 'O' in STOMPI?", "a": "Objek (Voorwerp)"},
        {"q": "Waarvoor staan die 'M' in STOMPI?", "a": "Manier (Manner)"},
        {"q": "Waarvoor staan die 'P' in STOMPI?", "a": "Plek (Place)"},
        {"q": "Waar staan die eerste werkwoord (V1)?", "a": "Na die Subjek"},
        {"q": "Waar staan die tweede werkwoord (V2)?", "a": "Aan die einde van die sin"},
        {"q": "Waarvoor staan die 'I' aan die einde?", "a": "Infinitief (om te...)"},
        {"q": "Skryf reg: 'Ek (speel) môre rugby'", "a": "Ek speel môre rugby"},
        {"q": "Skryf reg: 'Sy (gaan) vinnig nou winkel toe'", "a": "Sy gaan nou vinnig winkel toe"},

        # SET 8: Voornaamwoorde (Pronouns)
        {"q": "Besitlike voornaamwoord: 'Dit is (ek) boek'", "a": "My"},
        {"q": "Besitlike voornaamwoord: 'Dit is (jy) pen'", "a": "Jou"},
        {"q": "Besitlike voornaamwoord: 'Dit is (hy) hond'", "a": "Sy"},
        {"q": "Besitlike voornaamwoord: 'Dit is (sy) kat'", "a": "Haar"},
        {"q": "Besitlike voornaamwoord: 'Dit is (ons) huis'", "a": "Ons"},
        {"q": "Besitlike voornaamwoord: 'Dit is (hulle) skool'", "a": "Hulle"},
        {"q": "Voornaamwoord: 'Hy kyk na (ek)'", "a": "My"},
        {"q": "Voornaamwoord: 'Ons kyk na (hulle)'", "a": "Hulle"},
        {"q": "Voornaamwoord: 'Sy kyk na (hy)'", "a": "Hom"},
        {"q": "Voornaamwoord: 'Ek kyk na (sy)'", "a": "Haar"},

        # SET 9: Voegwoorde (Conjunctions)
        {"q": "Verbind: 'Ek is siek. Ek bly in die bed.' (want)", "a": "Ek is siek want ek bly in die bed"},
        {"q": "Verbind: 'Hy leer hard. Hy wil slaag.' (omdat)", "a": "Hy leer hard omdat hy wil slaag"},
        {"q": "Wat gebeur met die werkwoord na 'omdat'?", "a": "Dit skuif na die einde"},
        {"q": "Wat gebeur met die werkwoord na 'want'?", "a": "Niks nie (Groep 1 voegwoord)"},
        {"q": "Verbind: 'Dit reën. Ons speel binne.' (daarom)", "a": "Dit reën, daarom speel ons binne"},
        {"q": "Verbind: 'Ek is moeg. Ek gaan slaap.' (dus)", "a": "Ek is moeg, dus gaan ek slaap"},
        {"q": "Wat is die groep 1 voegwoorde? (onthou FANBOYS)", "a": "Maar, en, want, dog, of"},
        {"q": "Wat gebeur met die werkwoord na 'dat'?", "a": "Dit skuif na die einde"},
        {"q": "Verbind: 'Sy sê. Sy is moeg.' (dat)", "a": "Sy sê dat sy moeg is"},
        {"q": "Verbind: 'Hulle vra. Wie kom?' (of)", "a": "Hulle vra of wie kom"},

        # SET 10: Algemene Reëls (General Rules)
        {"q": "Wat is die 'Negatiewe vorm' (Ontkenning)?", "a": "Nie...nie"},
        {"q": "Ontkenning: 'Ek loop huis toe'", "a": "Ek loop nie huis toe nie"},
        {"q": "Ontkenning: 'Het jy die kos geëet?'", "a": "Nee, ek het nie die kos geëet nie"},
        {"q": "Wat word 'iemand' in die ontkenning?", "a": "Niemand"},
        {"q": "Wat word 'iets' in die ontkenning?", "a": "Niks"},
        {"q": "Wat word 'altyd' in die ontkenning?", "a": "Nooit"},
        {"q": "Wat word 'êrens' in die ontkenning?", "a": "Nêrens"},
        {"q": "Trappe van vergelyking: Groot, groter, ...", "a": "Grootste"},
        {"q": "Trappe van vergelyking: Goed, beter, ...", "a": "Beste"},
        {"q": "Trappe van vergelyking: Lank, langer, ...", "a": "Lankste"}
    ],
    "English": [
        # SET 1: Parts of Speech (The Basics)
        {"q": "What do you call a word that names a person, place, or thing?", "a": "A Noun"},
        {"q": "What is a 'Proper Noun'?", "a": "A specific name for a person or place (starts with a Capital Letter)"},
        {"q": "Which part of speech describes an action or state of being?", "a": "A Verb"},
        {"q": "What is an 'Adjective'?", "a": "A word that describes or modifies a Noun"},
        {"q": "What part of speech describes how, when, or where an action happens?", "a": "An Adverb"},
        {"q": "Give an example of a 'Pronoun'.", "a": "He, She, It, They, or We"},
        {"q": "What is a 'Preposition'?", "a": "A word showing the relationship or position (e.g., on, under, between)"},
        {"q": "What is a 'Conjunction'?", "a": "A joining word (e.g., and, but, because)"},
        {"q": "What is a 'Collective Noun'?", "a": "A word for a group (e.g., a 'pride' of lions)"},
        {"q": "What is an 'Abstract Noun'?", "a": "A noun for something you cannot touch (e.g., love, courage, time)"},

        # SET 2: Punctuation & Sentences
        {"q": "What punctuation mark is used to show belonging or possession?", "a": "The Apostrophe"},
        {"q": "When do you use a 'Comma'?", "a": "To show a pause or to separate items in a list"},
        {"q": "What is the purpose of 'Inverted Commas'?", "a": "To indicate direct speech or a quote"},
        {"q": "What do we call a sentence that asks a question?", "a": "An Interrogative sentence"},
        {"q": "What is a 'Statement' called in grammar?", "a": "A Declarative sentence"},
        {"q": "What punctuation follows an 'Exclamatory' sentence?", "a": "An Exclamation mark (!)"},
        {"q": "What is a 'Prefix'?", "a": "A group of letters added to the START of a word (e.g., UN-happy)"},
        {"q": "What is a 'Suffix'?", "a": "A group of letters added to the END of a word (e.g., quick-LY)"},
        {"q": "What is a 'Simple Sentence'?", "a": "A sentence with one independent clause (one subject and one verb)"},
        {"q": "What do we call two simple sentences joined by a conjunction?", "a": "A Compound Sentence"},

        # SET 3: Figures of Speech (Imagery)
        {"q": "What is a 'Simile'?", "a": "A comparison using the words 'like' or 'as'"},
        {"q": "What is a 'Metaphor'?", "a": "A direct comparison NOT using 'like' or 'as' (e.g., 'He is a lion')"},
        {"q": "Define 'Personification'.", "a": "Giving human qualities to non-human things"},
        {"q": "What is 'Alliteration'?", "a": "The repetition of consonant sounds at the start of words"},
        {"q": "What is 'Onomatopoeia'?", "a": "Words that imitate sounds (e.g., Bang, Hiss, Pop)"},
        {"q": "What is an 'Hyperbole'?", "a": "An extreme exaggeration (e.g., 'I've told you a thousand times')"},
        {"q": "Define 'Assonance'.", "a": "The repetition of vowel sounds within words"},
        {"q": "What is an 'Oxymoron'?", "a": "Two opposite words placed side-by-side (e.g., 'Bitter-sweet')"},
        {"q": "What is 'Irony'?", "a": "When the opposite of what is expected happens"},
        {"q": "What is 'Sarcasm'?", "a": "Using irony to mock or convey contempt"},

        # SET 4: Tenses & Verbs
        {"q": "What is the 'Past Tense' of 'Go'?", "a": "Went"},
        {"q": "What is the 'Future Tense' of 'I study'?", "a": "I will study"},
        {"q": "What is a 'Finite Verb'?", "a": "A verb that has a subject and shows tense"},
        {"q": "What is an 'Auxiliary Verb'?", "a": "A helping verb (e.g., is, am, are, was, were)"},
        {"q": "What is the 'Continuous Tense' usually marked by?", "a": "The suffix -ING (e.g., running)"},
        {"q": "Change to Past Tense: 'She sings beautifully.'", "a": "She sang beautifully"},
        {"q": "What is a 'Subject' in a sentence?", "a": "The person or thing performing the action"},
        {"q": "What is an 'Object' in a sentence?", "a": "The person or thing receiving the action"},
        {"q": "What is a 'Transitive Verb'?", "a": "A verb that requires an object to make sense"},
        {"q": "What is an 'Intransitive Verb'?", "a": "A verb that does not need an object (e.g., 'He laughed')"},

        # SET 5: Vocabulary & Spelling
        {"q": "What is a 'Synonym'?", "a": "A word with the same or similar meaning"},
        {"q": "What is an 'Antonym'?", "a": "A word with the opposite meaning"},
        {"q": "What are 'Homophones'?", "a": "Words that sound the same but have different spellings/meanings (e.g., see/sea)"},
        {"q": "What are 'Homonyms'?", "a": "Words spelled the same but with different meanings (e.g., 'bat' animal / 'bat' sports)"},
        {"q": "Give a synonym for 'Fragile'.", "a": "Delicate / Breakable"},
        {"q": "Give an antonym for 'Permanent'.", "a": "Temporary"},
        {"q": "Correct the spelling: 'Accomodation'", "a": "Accommodation (double 'c' and double 'm')"},
        {"q": "What is a 'Literal' meaning?", "a": "The actual, factual meaning of a word"},
        {"q": "What is a 'Figurative' meaning?", "a": "A metaphorical or symbolic meaning"},
        {"q": "What is 'Ambiguity'?", "a": "When a sentence has more than one possible meaning"},

        # SET 6: Active and Passive Voice
        {"q": "In which voice is the subject performing the action?", "a": "Active Voice"},
        {"q": "In which voice is the action being done TO the subject?", "a": "Passive Voice"},
        {"q": "Change to Passive: 'The boy kicked the ball.'", "a": "The ball was kicked by the boy"},
        {"q": "Change to Active: 'The cake was eaten by the dog.'", "a": "The dog ate the cake"},
        {"q": "Identify the voice: 'I wrote the essay.'", "a": "Active Voice"},
        {"q": "Identify the voice: 'The window was broken.'", "a": "Passive Voice"},
        {"q": "Which word is often used in Passive voice to show who did the action?", "a": "The word 'by'"},
        {"q": "Change to Passive: 'The chef prepares the meal.'", "a": "The meal is prepared by the chef"},
        {"q": "Change to Active: 'A song is being sung by Aanya.'", "a": "Aanya is singing a song"},
        {"q": "Why do we use Passive voice?", "a": "To focus on the action or the object rather than the person doing it"},

        # SET 7: Direct and Indirect Speech
        {"q": "What is another name for 'Indirect Speech'?", "a": "Reported Speech"},
        {"q": "In Direct Speech, where do the commas and full stops go?", "a": "Inside the quotation marks"},
        {"q": "Change to Indirect: He said, 'I am tired.'", "a": "He said that he was tired"},
        {"q": "What usually happens to the tense in Reported Speech?", "a": "It moves one step back into the past"},
        {"q": "In Reported Speech, what does 'today' become?", "a": "That day"},
        {"q": "In Reported Speech, what does 'tomorrow' become?", "a": "The following day / The next day"},
        {"q": "Change to Direct: She said that she loved music.", "a": "She said, 'I love music.'"},
        {"q": "In Reported Speech, what does 'here' become?", "a": "There"},
        {"q": "What word is often used to join the speaker to the report in Indirect speech?", "a": "The word 'that'"},
        {"q": "Change to Indirect: 'Close the door!' the teacher said.", "a": "The teacher told us to close the door"},

        # SET 8: Poetry Terminology
        {"q": "What is a 'Stanza'?", "a": "A group of lines in a poem (like a paragraph)"},
        {"q": "What is a 'Rhyme Scheme'?", "a": "The pattern of rhymes at the end of lines (e.g., AABB or ABAB)"},
        {"q": "What do we call a poem that does not rhyme?", "a": "Free Verse"},
        {"q": "What is the 'Tone' of a poem?", "a": "The poet's attitude or feeling towards the subject"},
        {"q": "What is the 'Mood' of a poem?", "a": "The atmosphere or feeling created for the reader"},
        {"q": "What is a 'Theme'?", "a": "The central message or idea of a poem"},
        {"q": "What is 'Enjambment'?", "a": "When a line of poetry runs over into the next line without punctuation"},
        {"q": "What is a 'Couplet'?", "a": "Two consecutive lines of poetry that rhyme"},
        {"q": "What is 'Imagery'?", "a": "Words that create a picture in the reader's mind"},
        {"q": "What is a 'Rhythm'?", "a": "The beat or pace of the poem"},

        # SET 9: Visual Literacy & Advertising
        {"q": "What is a 'Slogan'?", "a": "A short, catchy phrase used in advertising"},
        {"q": "What is a 'Logo'?", "a": "A symbol or design that identifies a brand"},
        {"q": "In an advert, what does 'AIDA' stand for?", "a": "Attention, Interest, Desire, Action"},
        {"q": "What is a 'Target Audience'?", "a": "The specific group of people an advert is aimed at"},
        {"q": "What is 'Bias'?", "a": "A one-sided or prejudiced view of something"},
        {"q": "What is 'Propaganda'?", "a": "Information used to promote a specific political cause or point of view"},
        {"q": "What is a 'Caption'?", "a": "A title or brief explanation attached to an image"},
        {"q": "What is 'Stereotyping'?", "a": "A fixed, overgeneralized belief about a particular group"},
        {"q": "In cartoons, what does a 'Thought Bubble' look like?", "a": "Like a cloud with small circles leading to the character"},
        {"q": "In cartoons, what does a 'Speech Bubble' look like?", "a": "A solid line with a tail pointing to the character's mouth"},

        # SET 10: Comprehension & Summary
        {"q": "What is the 'Main Idea' of a text?", "a": "The most important point the author is making"},
        {"q": "What is a 'Summary'?", "a": "A brief statement of the main points in your own words"},
        {"q": "What is 'Skimming'?", "a": "Reading a text quickly to get the general idea"},
        {"q": "What is 'Scanning'?", "a": "Looking through a text quickly to find a specific piece of information"},
        {"q": "What is 'Context'?", "a": "The circumstances or setting in which something happens"},
        {"q": "What is an 'Inference'?", "a": "A conclusion reached based on evidence and reasoning (reading between the lines)"},
        {"q": "What is 'Fact'?", "a": "Something that can be proven to be true"},
        {"q": "What is 'Opinion'?", "a": "A personal belief or feeling that cannot be proven"},
        {"q": "What does it mean to 'Paraphrase'?", "a": "To rewrite a sentence in your own words without changing the meaning"},
        {"q": "What is the 'Heading' of a text?", "a": "The title at the top of a page or section"}
    ],
    "EMS": [
        # SET 1: The Economy - Government & Budget
        {"q": "What are the three levels of government in South Africa?", "a": "National, Provincial, and Local government"},
        {"q": "What is the main source of income for the South African government?", "a": "Taxes (Income tax, VAT, etc.)"},
        {"q": "What is the 'National Budget'?", "a": "A plan showing the government's estimated income and spending for the year"},
        {"q": "When the government spends more than it earns, it is called a...", "a": "Budget Deficit"},
        {"q": "When the government earns more than it spends, it is called a...", "a": "Budget Surplus"},
        {"q": "Name the government department responsible for collecting taxes in SA.", "a": "SARS (South African Revenue Service)"},
        {"q": "What does 'Direct Tax' mean?", "a": "Tax paid directly to the government on income or profit (e.g., Personal Income Tax)"},
        {"q": "What does 'Indirect Tax' mean?", "a": "Tax paid on goods and services (e.g., VAT)"},
        {"q": "What is the current VAT rate in South Africa?", "a": "15%"},
        {"q": "What are 'Social Grants'?", "a": "Money paid by the government to help people in need (e.g., child support, old age pension)"},

        # SET 2: Financial Literacy - Accounting Basics
        {"q": "What is an 'Asset'?", "a": "Something of value owned by a business (e.g., vehicles, equipment)"},
        {"q": "What is a 'Liability'?", "a": "Money that a business owes to others (e.g., bank loans, creditors)"},
        {"q": "What is 'Owner's Equity'?", "a": "The value of the owner's investment in the business"},
        {"q": "What is the Basic Accounting Equation?", "a": "Assets = Capital + Liabilities"},
        {"q": "What is 'Income'?", "a": "Money received by a business for providing services or selling goods"},
        {"q": "What is an 'Expense'?", "a": "Costs incurred to run a business (e.g., rent, water, electricity)"},
        {"q": "What is 'Capital'?", "a": "The money or assets the owner puts into the business to start it"},
        {"q": "What are 'Drawings'?", "a": "When the owner takes money or goods from the business for personal use"},
        {"q": "What is a 'Profit'?", "a": "When Income is greater than Expenses"},
        {"q": "What is a 'Loss'?", "a": "When Expenses are greater than Income"},

        # SET 3: Source Documents
        {"q": "What is a 'Source Document'?", "a": "A written proof that a financial transaction took place"},
        {"q": "What document is issued when a customer pays cash for goods?", "a": "Cash Invoice or Receipt"},
        {"q": "What is a 'Cash Register Roll' (CRR)?", "a": "The internal source document for cash sales in a retail shop"},
        {"q": "What document is received when the business pays for something by cheque/EFT?", "a": "Cheque Counterfoil or Bank Statement"},
        {"q": "What is a 'Bank Statement'?", "a": "A document from the bank showing all transactions in the business's account"},
        {"q": "What is a 'Deposit Slip'?", "a": "A document used to put cash or cheques into a bank account"},
        {"q": "Why is it important to keep source documents?", "a": "For record-keeping, auditing, and tax purposes"},
        {"q": "What document is used for small, petty cash payments?", "a": "Petty Cash Voucher"},
        {"q": "True or False: Every transaction must have a source document.", "a": "True"},
        {"q": "Who receives the original receipt in a transaction?", "a": "The person making the payment"},

        # SET 4: Cash Receipts Journal (CRJ)
        {"q": "What is the purpose of the Cash Receipts Journal (CRJ)?", "a": "To record all cash received by the business"},
        {"q": "In the CRJ, what does 'Analysis of Receipts' represent?", "a": "The 'till' or cash drawer where money is kept before being deposited"},
        {"q": "What column in the CRJ shows the total amount put into the bank?", "a": "Bank column"},
        {"q": "When a business provides a service for cash, which account is credited?", "a": "Current Income"},
        {"q": "In which column do we record money received that doesn't have its own column?", "a": "Sundry Accounts"},
        {"q": "What is 'Folio' (Fol) used for in a journal?", "a": "Cross-referencing to the General Ledger"},
        {"q": "If an owner contributes capital, in which journal is it recorded?", "a": "Cash Receipts Journal (CRJ)"},
        {"q": "Where do we get the information to fill in the CRJ?", "a": "Receipts and Cash Register Rolls"},
        {"q": "What is the heading of a CRJ?", "a": "Cash Receipts Journal of [Business Name] for [Month] [Year]"},
        {"q": "If the business receives rent, which account is used in Sundry Accounts?", "a": "Rent Income"},

        # SET 5: Cash Payments Journal (CPJ)
        {"q": "What is the purpose of the Cash Payments Journal (CPJ)?", "a": "To record all cash paid out by the business"},
        {"q": "Which source document is used for the CPJ?", "a": "Cheque counterfoils or Bank Statements (EFT)"},
        {"q": "When the business pays for 'Stationery', which column is used?", "a": "Stationery column"},
        {"q": "When the business pays for something by EFT, which account is credited?", "a": "Bank"},
        {"q": "What are 'Wages'?", "a": "Weekly payments made to employees for manual work"},
        {"q": "What are 'Salaries'?", "a": "Monthly payments made to employees (usually professional/office work)"},
        {"q": "If the business pays for 'Repairs', where is it recorded if there is no specific column?", "a": "Sundry Accounts"},
        {"q": "If the owner pays for his personal home phone using business money, it is recorded as...", "a": "Drawings"},
        {"q": "In the CPJ, the Bank column total should equal...", "a": "The sum of all the other analysis columns"},
        {"q": "What is 'Trading Stock'?", "a": "Goods bought by the business with the intention of selling them"},

        # SET 6: Entrepreneurship
        {"q": "What is an 'Entrepreneur'?", "a": "Someone who starts a business, taking a risk to make a profit"},
        {"q": "Name a characteristic of a successful entrepreneur.", "a": "Risk-taker / Creative / Persistent / Hardworking"},
        {"q": "What is a 'Business Plan'?", "a": "A document describing a business, its goals, and how it will achieve them"},
        {"q": "What is the 'SWOT Analysis' used for?", "a": "To identify Strengths, Weaknesses, Opportunities, and Threats"},
        {"q": "In SWOT, which two factors are internal (inside the business)?", "a": "Strengths and Weaknesses"},
        {"q": "In SWOT, which two factors are external (outside the business)?", "a": "Opportunities and Threats"},
        {"q": "What is a 'Target Market'?", "a": "The specific group of people a business aims to sell its products to"},
        {"q": "What are the '4 Ps' of Marketing?", "a": "Product, Price, Place, and Promotion"},
        {"q": "What is 'Advertising'?", "a": "Telling people about a product or service to encourage them to buy it"},
        {"q": "What is 'Promotion'?", "a": "Activities to boost sales, like discounts or buy-one-get-one-free"},

        # SET 7: Factors of Production
        {"q": "Name the four Factors of Production.", "a": "Natural Resources, Labour, Capital, and Entrepreneurship"},
        {"q": "What is the reward/remuneration for 'Labour'?", "a": "Salaries or Wages"},
        {"q": "What is the reward/remuneration for 'Capital'?", "a": "Interest"},
        {"q": "What is the reward/remuneration for 'Entrepreneurship'?", "a": "Profit"},
        {"q": "What is the reward/remuneration for 'Natural Resources' (Land)?", "a": "Rent"},
        {"q": "What is 'Skilled Labour'?", "a": "Workers who have high levels of training/education (e.g., doctors)"},
        {"q": "What is 'Unskilled Labour'?", "a": "Workers who do physical work that requires little training"},
        {"q": "What is 'Physical Capital'?", "a": "Tools, machinery, and buildings used in production"},
        {"q": "What is 'Human Capital'?", "a": "The knowledge and skills of the people in the workforce"},
        {"q": "True or False: Without an entrepreneur, the other factors of production cannot be combined.", "a": "True"},

        # SET 8: Levels and Functions of Management
        {"q": "Name the three levels of management.", "a": "Top, Middle, and Lower level management"},
        {"q": "Who is usually in 'Top Level' management?", "a": "CEO, Board of Directors, or Owners"},
        {"q": "What is the main task of 'Lower Level' management?", "a": "Supervising daily tasks of workers"},
        {"q": "Name the four functions of management (POLC).", "a": "Planning, Organising, Leading, and Controlling"},
        {"q": "What is the 'Planning' function?", "a": "Setting goals and deciding how to reach them"},
        {"q": "What is the 'Leading' function?", "a": "Motivating and guiding employees to work hard"},
        {"q": "What is the 'Organising' function?", "a": "Arranging resources and people to carry out the plan"},
        {"q": "What is the 'Controlling' function?", "a": "Checking if the business is reaching its goals and fixing problems"},
        {"q": "What makes a 'Good Leader'?", "a": "Communication, integrity, and the ability to inspire others"},
        {"q": "What is 'Autocratic' leadership?", "a": "A leader who makes all decisions without asking others"},

        # SET 9: Forms of Ownership
        {"q": "What is a 'Sole Trader'?", "a": "A business owned and run by one person"},
        {"q": "What is a 'Partnership'?", "a": "A business owned by 2 to 20 people"},
        {"q": "What is 'Unlimited Liability'?", "a": "When the owner is personally responsible for all the business's debts"},
        {"q": "Name one advantage of a Sole Trader.", "a": "Easy to start / All profit goes to the owner / Quick decisions"},
        {"q": "Name one disadvantage of a Partnership.", "a": "Conflict between partners / Shared profits / Unlimited liability"},
        {"q": "What is a 'Close Corporation' (CC)?", "a": "An older form of ownership in SA (no new ones can be started, but old ones still exist)"},
        {"q": "What is a 'Private Company'?", "a": "A company whose name ends in (Pty) Ltd"},
        {"q": "What is a 'Public Company'?", "a": "A company whose name ends in Ltd and can sell shares on the JSE"},
        {"q": "What is the 'JSE'?", "a": "Johannesburg Stock Exchange"},
        {"q": "What is a 'Non-Profit Organisation' (NPO)?", "a": "A business set up to help the community, not to make money for owners"},

        # SET 10: Markets and Sustainable Growth
        {"q": "What is a 'Market'?", "a": "Any place where buyers and sellers meet to trade"},
        {"q": "What is the 'Labour Market'?", "a": "Where people look for work and employers look for workers"},
        {"q": "What is the 'Financial Market'?", "a": "Where people trade money, shares, and foreign currency"},
        {"q": "What is 'Sustainable Growth'?", "a": "Growing a business without harming the environment or future generations"},
        {"q": "How can a business be 'Green'?", "a": "By recycling, reducing waste, and using renewable energy"},
        {"q": "What is 'Productivity'?", "a": "How much work is done compared to the resources used"},
        {"q": "What is the 'Standard of Living'?", "a": "The level of wealth, comfort, and goods available to a person"},
        {"q": "What is 'Inflation'?", "a": "A general increase in prices and a fall in the purchasing value of money"},
        {"q": "What is 'Unemployment'?", "a": "When people who are willing and able to work cannot find a job"},
        {"q": "What is 'Globalisation'?", "a": "The process by which businesses start operating on an international scale"}
    ],
    "Geography": [
        # SET 1: Maps and Globes - Latitude and Longitude
        {"q": "What do we call the imaginary lines that run East to West around the Earth?", "a": "Lines of Latitude"},
        {"q": "What do we call the imaginary lines that run North to South?", "a": "Lines of Longitude (Meridians)"},
        {"q": "What is the 0° line of latitude called?", "a": "The Equator"},
        {"q": "What is the 0° line of longitude called?", "a": "The Greenwich Meridian (Prime Meridian)"},
        {"q": "In which two hemispheres is South Africa located?", "a": "Southern and Eastern Hemispheres"},
        {"q": "What is the latitude of the Tropic of Capricorn?", "a": "23.5° South"},
        {"q": "Which line of latitude is at 23.5° North?", "a": "The Tropic of Cancer"},
        {"q": "How many degrees does the Earth rotate in one hour?", "a": "15 degrees"},
        {"q": "If it is 12:00 at the Greenwich Meridian, what time is it at 30° East?", "a": "14:00 (2 hours ahead)"},
        {"q": "What is the 'International Date Line'?", "a": "The line at 180° longitude where the date changes"},

        # SET 2: Map Skills and Scale
        {"q": "What is a 'Map Scale'?", "a": "The relationship between distance on a map and distance on the ground"},
        {"q": "What is a 'Ratio Scale'?", "a": "A scale shown as numbers, e.g., 1:50 000"},
        {"q": "On a 1:50 000 map, 1cm represents how many kilometers?", "a": "0.5 km (500 meters)"},
        {"q": "What is a 'Line Scale' (Linear Scale)?", "a": "A line divided into units representing actual distance"},
        {"q": "What is the 'Legend' or 'Key' of a map?", "a": "The box that explains what the symbols on a map mean"},
        {"q": "What does a 'Compass Rose' show?", "a": "Cardinal directions (North, South, East, West)"},
        {"q": "What is the direction exactly between South and West?", "a": "South-West"},
        {"q": "What is an 'Alpha-numeric Grid'?", "a": "A grid using letters and numbers to find places (e.g., B4)"},
        {"q": "What do we call the height of land above sea level?", "a": "Altitude"},
        {"q": "What are 'Contour Lines'?", "a": "Lines on a map joining points of equal height"},

        # SET 3: Satellite Imagery and Photos
        {"q": "What is 'Remote Sensing'?", "a": "Collecting information from a distance, usually by satellite"},
        {"q": "What is a 'Geostationary Satellite'?", "a": "A satellite that stays over the same spot on Earth"},
        {"q": "Name one use for satellite images in Geography.", "a": "Weather forecasting / Tracking fires / Urban planning"},
        {"q": "What is an 'Aerial Photograph'?", "a": "A photo taken from a high position, usually an airplane"},
        {"q": "What is an 'Oblique Aerial Photo'?", "a": "A photo taken at an angle (from the side)"},
        {"q": "What is a 'Vertical Aerial Photo'?", "a": "A photo taken from directly above (looking straight down)"},
        {"q": "What is 'Google Earth' used for?", "a": "Viewing 3D maps and satellite imagery of the world"},
        {"q": "In a satellite image, what color usually represents healthy vegetation?", "a": "Green (or red in infrared images)"},
        {"q": "What are 'Pixels'?", "a": "Small dots that make up a digital image"},
        {"q": "Why are satellite images better than old maps for tracking floods?", "a": "They provide real-time, updated data"},

        # SET 4: Settlement - Rural and Urban
        {"q": "What is a 'Settlement'?", "a": "A place where people live and interact"},
        {"q": "What is a 'Rural Settlement'?", "a": "A small settlement in the countryside (farms or villages)"},
        {"q": "What is an 'Urban Settlement'?", "a": "A built-up area like a town or city"},
        {"q": "What is the primary function of most rural settlements?", "a": "Agriculture (farming), mining, or fishing"},
        {"q": "What is a 'Dispersed' (Isolated) settlement pattern?", "a": "Buildings are spread far apart from each other"},
        {"q": "What is a 'Nucleated' (Clustered) settlement pattern?", "a": "Buildings are grouped closely together"},
        {"q": "What is a 'Linear' settlement pattern?", "a": "Buildings follow a line (like a road, river, or coast)"},
        {"q": "Name a 'Pull Factor' of a city.", "a": "Better jobs / Education / Healthcare / Entertainment"},
        {"q": "Name a 'Push Factor' of a rural area.", "a": "Drought / Lack of jobs / Poor services"},
        {"q": "What is 'Urbanisation'?", "a": "The increase in the percentage of people living in cities"},

        # SET 5: Land Use in Urban Areas
        {"q": "What does 'CBD' stand for?", "a": "Central Business District"},
        {"q": "What type of buildings are usually found in the CBD?", "a": "High-rise offices and department stores"},
        {"q": "What is the 'Transition Zone' (Grey Area)?", "a": "The area around the CBD with mixed land use (shops and old houses)"},
        {"q": "What is a 'Residential Area'?", "a": "An area where people live"},
        {"q": "Where are 'Heavy Industries' (factories) usually located?", "a": "On the outskirts of the city, away from houses"},
        {"q": "What is a 'Greenbelt'?", "a": "Open space or parks within an urban area"},
        {"q": "What is an 'Informal Settlement'?", "a": "An unplanned area with temporary housing (shacks)"},
        {"q": "Why is land in the CBD so expensive?", "a": "High demand and limited space"},
        {"q": "What is a 'Commuter'?", "a": "A person who travels between home and work every day"},
        {"q": "What is 'Mixed Land Use'?", "a": "When buildings have different functions (e.g., shops downstairs, flats upstairs)"},

        # SET 6: Transport and Trade
        {"q": "What is 'Public Transport'?", "a": "Transport services like buses, trains, and taxis used by the public"},
        {"q": "What is a 'Transport Mode'?", "a": "A specific type of transport (road, rail, air, or water)"},
        {"q": "Which mode of transport is best for heavy, bulky goods over long distances?", "a": "Rail (Train) or Sea (Ship)"},
        {"q": "What are 'Exports'?", "a": "Goods sold to another country"},
        {"q": "What are 'Imports'?", "a": "Goods bought from another country"},
        {"q": "What is 'Trade'?", "a": "The exchange of goods and services"},
        {"q": "What is a 'Harbour'?", "a": "A place on the coast where ships can dock to load/unload"},
        {"q": "What is 'Bulk Cargo'?", "a": "Unpackaged goods like coal, iron ore, or grain"},
        {"q": "What is 'Containerisation'?", "a": "Using large metal boxes to transport goods easily between ships/trucks"},
        {"q": "How has the internet changed trade?", "a": "It allows for E-commerce (online shopping and global banking)"},

        # SET 7: Migration - People on the Move
        {"q": "What is 'Migration'?", "a": "The movement of people from one place to another"},
        {"q": "What is an 'Emigrant'?", "a": "A person who leaves their own country to live elsewhere"},
        {"q": "What is an 'Immigrant'?", "a": "A person who comes to live permanently in a foreign country"},
        {"q": "What is 'Internal Migration'?", "a": "Moving within the same country (e.g., from Limpopo to Gauteng)"},
        {"q": "What is 'Forced Migration'?", "a": "When people are made to move against their will (e.g., due to war)"},
        {"q": "What is a 'Refugee'?", "a": "Someone who has fled their country to escape danger"},
        {"q": "What is 'Rural-Urban Migration'?", "a": "People moving from farms to cities"},
        {"q": "What is 'Brain Drain'?", "a": "When highly skilled people (doctors, engineers) leave a country"},
        {"q": "What is 'Xenophobia'?", "a": "Dislike or fear of people from other countries"},
        {"q": "Name one social impact of migration on a city.", "a": "Overcrowding / Pressure on clinics and schools"},

        # SET 8: Global Settlement Issues
        {"q": "What is a 'Megacity'?", "a": "A city with more than 10 million people"},
        {"q": "Name one challenge faced by people in informal settlements.", "a": "Lack of clean water / No electricity / Fire risks"},
        {"q": "What is 'Urban Sprawl'?", "a": "The rapid, uncontrolled spread of cities into the surrounding countryside"},
        {"q": "What is 'Gentrification'?", "a": "Improving an old housing area, often driving out poorer residents"},
        {"q": "What is 'Sustainability' in urban planning?", "a": "Designing cities that are good for people and the planet"},
        {"q": "How can cities reduce traffic congestion?", "a": "Better public transport / Cycling lanes / Carpooling"},
        {"q": "What is 'Slum Clearance'?", "a": "When the government removes shacks to build formal housing"},
        {"q": "What is a 'Dormitory Town'?", "a": "A town where people sleep but travel to a nearby city for work"},
        {"q": "What is 'Social Segregation'?", "a": "When different groups of people live in separate areas based on income or race"},
        {"q": "What is 'Infrastructure'?", "a": "Basic systems like roads, power, and water pipes"},

        # SET 9: Climate and Weather in Settlements
        {"q": "What is an 'Urban Heat Island'?", "a": "When a city is much warmer than the surrounding rural areas"},
        {"q": "Why are cities warmer than farms?", "a": "Concrete and tar absorb heat; less trees to cool the air"},
        {"q": "What is 'Smog'?", "a": "A mixture of smoke and fog (air pollution)"},
        {"q": "How does paving affect water drainage?", "a": "It prevents water from soaking in, causing more runoff and floods"},
        {"q": "What is a 'Microclimate'?", "a": "The climate of a very small, specific area"},
        {"q": "How do tall buildings affect wind in a city?", "a": "They can create 'wind tunnels' (canyon effect)"},
        {"q": "What is 'Acid Rain'?", "a": "Rain made acidic by pollution from factories and cars"},
        {"q": "Name one way a 'Green City' helps the environment.", "a": "Planting trees / Roof gardens / Using solar power"},
        {"q": "What is 'Global Warming'?", "a": "The gradual increase in the Earth's average temperature"},
        {"q": "How does air pollution affect health in cities?", "a": "It causes respiratory problems like asthma"},

        # SET 10: South African Settlement Case Studies
        {"q": "Which South African city is known as the 'Mother City'?", "a": "Cape Town"},
        {"q": "Which province in SA is the most urbanised?", "a": "Gauteng"},
        {"q": "What was the 'Group Areas Act'?", "a": "An apartheid law that forced different races to live in separate areas"},
        {"q": "What is a 'Township' in the South African context?", "a": "Residential areas built for black people under apartheid"},
        {"q": "What is the 'Johannesburg CBD' famous for?", "a": "Being the financial heart of South Africa"},
        {"q": "What is a 'Gated Community'?", "a": "A residential area with high security and restricted access"},
        {"q": "Why is the 'Gautrain' important for Gauteng?", "a": "It provides fast, safe transport between Joburg, Pretoria, and the airport"},
        {"q": "Name a major port city in South Africa.", "a": "Durban / Cape Town / Port Elizabeth (Gqeberha)"},
        {"q": "What is 'Land Restitution'?", "a": "A process to return land to people who were forced off it under apartheid"},
        {"q": "What is the purpose of the 'Integrated Development Plan' (IDP)?", "a": "A plan used by local municipalities to improve service delivery"}
    ],
    "History": [
        # SET 1: The Industrial Revolution in Britain (Changes)
        {"q": "What was the Industrial Revolution?", "a": "A period of rapid change from farming to manufacturing with machines"},
        {"q": "In which country did the Industrial Revolution begin?", "a": "Britain"},
        {"q": "What was the 'Cottage Industry'?", "a": "A system where goods were made by hand in people's homes"},
        {"q": "Which invention by James Watt powered the new factories?", "a": "The Steam Engine"},
        {"q": "What is 'Urbanisation' in the context of the Industrial Revolution?", "a": "The movement of people from farms to cities to work in factories"},
        {"q": "What natural resource was essential for fueling steam engines?", "a": "Coal"},
        {"q": "What metal became very important for building machines and bridges?", "a": "Iron"},
        {"q": "What was the 'Spinning Jenny' used for?", "a": "Spinning many threads of cotton at once"},
        {"q": "What is 'Mass Production'?", "a": "Making large quantities of the same item quickly using machines"},
        {"q": "How did transport change during this time?", "a": "Steam trains and steamships made travel faster and cheaper"},

        # SET 2: Social Impact in Britain (Working Conditions)
        {"q": "What were 'Workhouses'?", "a": "Places where the poor were sent to live and work in harsh conditions"},
        {"q": "What was 'Child Labour'?", "a": "Using children to work in dangerous mines and factories"},
        {"q": "Why were children used in coal mines?", "a": "They were small enough to fit into narrow tunnels"},
        {"q": "What were the living conditions like for workers in cities?", "a": "Overcrowded, dirty, and prone to diseases like Cholera"},
        {"q": "What is a 'Trade Union'?", "a": "An organization of workers that fights for better pay and conditions"},
        {"q": "Who were the 'Luddites'?", "a": "Workers who broke machines because they feared losing their jobs"},
        {"q": "What was the 'Mines Act' of 1842?", "a": "A law that stopped women and children under 10 from working underground"},
        {"q": "What is 'Capitalism'?", "a": "An economic system where businesses are owned by private individuals for profit"},
        {"q": "Who were the 'Bourgeoisie'?", "a": "The wealthy middle class who owned the factories"},
        {"q": "Who were the 'Proletariat'?", "a": "The working class who sold their labour to survive"},

        # SET 3: Southern Africa by 1860
        {"q": "Which two European powers had colonies in SA by 1860?", "a": "Britain and the Netherlands (Boers)"},
        {"q": "What were the two British colonies in SA?", "a": "Cape Colony and Natal"},
        {"q": "What were the two Boer Republics?", "a": "Orange Free State and Transvaal (ZAR)"},
        {"q": "What was the main way of life for most people in SA before 1860?", "a": "Subsistence farming (farming for themselves)"},
        {"q": "What was the 'Great Trek'?", "a": "The movement of Boers away from British rule in the Cape"},
        {"q": "Who was the famous King of the Zulu nation in the early 1800s?", "a": "Shaka Zulu"},
        {"q": "What was the 'Mfecane'?", "a": "A period of widespread chaos and warfare among African kingdoms"},
        {"q": "Who founded the Basotho nation?", "a": "King Moshoeshoe"},
        {"q": "What was the main export of the Cape Colony before diamonds?", "a": "Wool and Wine"},
        {"q": "What happened to the Xhosa people during the 'Cattle Killing' of 1856?", "a": "Thousands died of starvation after killing their cattle due to a prophecy"},

        # SET 4: Diamond Mining and the Mineral Revolution
        {"q": "In what year were diamonds discovered in South Africa?", "a": "1867"},
        {"q": "Where were diamonds first discovered in SA?", "a": "Near the Orange River (Hopetown)"},
        {"q": "What city grew rapidly because of the diamond rush?", "a": "Kimberley"},
        {"q": "What was 'The Big Hole'?", "a": "The massive open-pit mine in Kimberley"},
        {"q": "Who was Cecil John Rhodes?", "a": "A British businessman who controlled the diamond industry (De Beers)"},
        {"q": "What was 'De Beers Consolidated Mines'?", "a": "The company that held a monopoly over diamond mining"},
        {"q": "What is a 'Claim' in mining?", "a": "A small piece of land where a person had the right to dig"},
        {"q": "What was the 'Mineral Revolution'?", "a": "The rapid change of SA's economy from farming to mining"},
        {"q": "How did the British take control of the diamond fields?", "a": "They annexed the land (Griqualand West)"},
        {"q": "Who were the 'Griquas'?", "a": "A community of people of mixed ancestry who lived near the diamond fields"},

        # SET 5: Gold Mining and the Witwatersrand
        {"q": "In what year was gold discovered on the Witwatersrand?", "a": "1886"},
        {"q": "Which city was founded as a result of the gold rush?", "a": "Johannesburg"},
        {"q": "What was 'The Rand'?", "a": "The common name for the Witwatersrand gold fields"},
        {"q": "Why was gold mining in SA so difficult compared to other places?", "a": "The gold was deep underground and hard to extract"},
        {"q": "What were the 'Randlords'?", "a": "Wealthy businessmen who controlled the gold mines"},
        {"q": "Who was Paul Kruger?", "a": "The President of the Transvaal during the gold rush"},
        {"q": "What is 'Deep-level Mining'?", "a": "Mining that happens kilometers below the surface"},
        {"q": "What is 'Cyanide Extraction'?", "a": "A chemical process used to get gold out of the rock"},
        {"q": "Why did the gold mines need so much cheap labour?", "a": "To keep costs low because mining deep gold was expensive"},
        {"q": "What was the 'Chamber of Mines'?", "a": "An organization formed by mine owners to cooperate on labour and wages"},

        # SET 6: Labour and Land (The Impact of Mining)
        {"q": "What was the 'Migrant Labour System'?", "a": "Men leaving their rural homes to work in the mines for months at a time"},
        {"q": "What were 'Compound Systems'?", "a": "Hostels where black miners were forced to live in cramped, controlled conditions"},
        {"q": "What was a 'Pass Book'?", "a": "A document black men had to carry to prove they had a job in the city"},
        {"q": "What was 'Closed Compounds'?", "a": "Compounds that workers were not allowed to leave for the duration of their contract"},
        {"q": "Why did the government introduce a 'Hut Tax'?", "a": "To force black farmers to earn money in the mines to pay the tax"},
        {"q": "What was the 'Native Land Act' of 1913?", "a": "A law that restricted black South Africans to owning only 7% of the land"},
        {"q": "How did the migrant labour system affect families?", "a": "It broke up families as men were away for most of the year"},
        {"q": "What is a 'Contract Labour'?", "a": "An agreement to work for a fixed period for a fixed wage"},
        {"q": "What was the 'Colour Bar'?", "a": "A system that reserved skilled, high-paying jobs for white workers"},
        {"q": "Who was Sol Plaatje?", "a": "A famous writer and founder of the ANC who fought against the Land Act"},

        # SET 7: The Scramble for Africa (Causes)
        {"q": "What was the 'Scramble for Africa'?", "a": "The rapid invasion and colonization of Africa by European powers"},
        {"q": "When did the Scramble for Africa mainly take place?", "a": "Between 1881 and 1914"},
        {"q": "What was the 'Berlin Conference' of 1884?", "a": "A meeting where European leaders divided Africa among themselves"},
        {"q": "Why did Europeans want African colonies (Economic)?", "a": "For raw materials (rubber, oil, gold) and new markets"},
        {"q": "What was 'Imperialism'?", "a": "A policy of extending a country's power through diplomacy or military force"},
        {"q": "What was the 'Civilising Mission'?", "a": "The excuse Europeans used that they were 'helping' Africans by bringing Christianity"},
        {"q": "What was 'Social Darwinism'?", "a": "The racist belief that some races were naturally superior to others"},
        {"q": "Which European King owned the Congo as his private property?", "a": "King Leopold II of Belgium"},
        {"q": "What was the 'Cape to Cairo' dream?", "a": "Cecil Rhodes' plan for a British railway across the whole of Africa"},
        {"q": "Which two African countries were NEVER colonized?", "a": "Ethiopia and Liberia"},

        # SET 8: Resistance to Colonialism
        {"q": "Did Africans accept European rule peacefully?", "a": "No, there was widespread resistance across the continent"},
        {"q": "Who were the 'Boers'?", "a": "South Africans of Dutch descent who fought the British"},
        {"q": "What was the 'Battle of Isandlwana'?", "a": "A famous battle where the Zulu army defeated the British in 1879"},
        {"q": "Who was 'Cetshwayo'?", "a": "The Zulu King during the Anglo-Zulu War"},
        {"q": "What was the 'Anglo-Boer War' (1899-1902)?", "a": "A war between the British and the Boer Republics over gold and independence"},
        {"q": "What is 'Guerrilla Warfare'?", "a": "Small groups using hit-and-run tactics against a larger army"},
        {"q": "What were 'Concentration Camps' in the Boer War?", "a": "Camps where British imprisoned Boer women/children and black Africans"},
        {"q": "What was the 'Scorched Earth Policy'?", "a": "The British burning Boer farms to stop them from getting food"},
        {"q": "How did the Anglo-Boer War end?", "a": "With the Treaty of Vereeniging (Boers lost independence)"},
        {"q": "What was the 'Bambatha Rebellion'?", "a": "A 1906 Zulu revolt against a new poll tax in Natal"},

        # SET 9: Social and Cultural Changes in Africa
        {"q": "How did European rule change African borders?", "a": "Borders were drawn by Europeans, often splitting ethnic groups"},
        {"q": "What is 'Missionary Education'?", "a": "Schools run by churches that taught Western values and languages"},
        {"q": "How did the economy of Africa change under colonialism?", "a": "It changed from farming for food to 'Cash Crops' for export"},
        {"q": "What language became dominant in many African countries due to colonialism?", "a": "European languages (English, French, Portuguese)"},
        {"q": "What is 'Direct Rule'?", "a": "When European officials ran the government themselves"},
        {"q": "What is 'Indirect Rule'?", "a": "When Europeans used local traditional leaders to carry out their orders"},
        {"q": "How did medicine change in Africa during this time?", "a": "Europeans introduced Western medicine and vaccines"},
        {"q": "What was the impact of the railway in Africa?", "a": "It allowed for easier transport of minerals and troops"},
        {"q": "What is 'Cultural Imperialism'?", "a": "Imposing one's culture (religion, dress, values) on another group"},
        {"q": "How did many African men's roles change?", "a": "Many became wage earners in mines or on plantations"},

        # SET 10: The Road to the Union of SA
        {"q": "What happened in 1910 in South Africa?", "a": "The Union of South Africa was formed"},
        {"q": "What was the Union of South Africa?", "a": "The joining of the four colonies into one country"},
        {"q": "Who was the first Prime Minister of the Union of SA?", "a": "Louis Botha"},
        {"q": "Who was excluded from voting in the new Union?", "a": "The vast majority of black, coloured, and Indian people"},
        {"q": "What was the 'South African Native National Congress' (SANNC)?", "a": "The organization formed in 1912 to fight for black rights (later the ANC)"},
        {"q": "Why was the SANNC formed?", "a": "In response to the exclusion of black people from the Union government"},
        {"q": "What was the 'Three-fold struggle'?", "a": "The fight against land dispossession, pass laws, and lack of voting rights"},
        {"q": "What was the status of SA within the British Empire in 1910?", "a": "It was a 'Dominion' (self-governing but linked to Britain)"},
        {"q": "What city became the legislative capital (Parliament) in 1910?", "a": "Cape Town"},
        {"q": "What city became the administrative capital in 1910?", "a": "Pretoria"}
    ],
    "Life Orientation": [
        # SET 1: Self-concept and Self-esteem
        {"q": "What is 'Self-concept'?", "a": "The way you see and think about yourself."},
        {"q": "What is 'Self-esteem'?", "a": "How much you value and like yourself."},
        {"q": "Name one factor that can influence your self-esteem.", "a": "Media / Peer feedback / Family / Academic success."},
        {"q": "What is 'Positive Self-talk'?", "a": "Replacing negative thoughts with encouraging, kind ones."},
        {"q": "True or False: Self-esteem can change over time.", "a": "True."},
        {"q": "What is 'Body Image'?", "a": "How you see and feel about your physical appearance."},
        {"q": "How does social media often affect body image?", "a": "It can create unrealistic standards through filters and editing."},
        {"q": "What is 'Self-acceptance'?", "a": "Loving yourself as you are, including your flaws."},
        {"q": "What is an 'Affirmation'?", "a": "A positive statement you say to yourself to build confidence."},
        {"q": "What is 'Personal Potential'?", "a": "The hidden talents and abilities you can develop over time."},

        # SET 2: Peer Pressure and Sexuality
        {"q": "What is 'Peer Pressure'?", "a": "The influence people your age have on your behavior or decisions."},
        {"q": "What is 'Positive Peer Pressure'?", "a": "When friends encourage you to do something good (like studying)."},
        {"q": "What is 'Negative Peer Pressure'?", "a": "When friends push you to do something wrong or dangerous."},
        {"q": "What is 'Assertiveness'?", "a": "Standing up for yourself in a firm but respectful way."},
        {"q": "Name a way to say 'No' to peer pressure.", "a": "Give a reason / Use a firm voice / Suggest a better idea."},
        {"q": "What is 'Sexuality'?", "a": "A person's feelings, thoughts, and behaviors regarding attraction."},
        {"q": "What is 'Gender Identity'?", "a": "How a person feels about being male, female, or another identity."},
        {"q": "What is 'Consent'?", "a": "Giving clear, voluntary permission for something to happen."},
        {"q": "Why is it important to set 'Personal Boundaries'?", "a": "To protect your physical and emotional well-being."},
        {"q": "What is 'Infatuation'?", "a": "An intense but short-lived passion or 'crush' on someone."},

        # SET 3: Relationships and Communication
        {"q": "What is an 'Healthy Relationship'?", "a": "A relationship based on respect, trust, and honesty."},
        {"q": "What is 'Effective Communication'?", "a": "Being able to express yourself clearly and listen to others."},
        {"q": "What is 'Active Listening'?", "a": "Paying full attention and showing you understand what is being said."},
        {"q": "What is 'Conflict Resolution'?", "a": "Finding a peaceful solution to a disagreement."},
        {"q": "Name one sign of an 'Unhealthy Relationship'.", "a": "Control / Dishonesty / Physical or emotional abuse."},
        {"q": "What is 'Empathy'?", "a": "Putting yourself in someone else's shoes to understand their feelings."},
        {"q": "What is 'Non-verbal Communication'?", "a": "Using body language, facial expressions, and eye contact."},
        {"q": "What is a 'Peer Group'?", "a": "A group of people of a similar age and social status."},
        {"q": "What is 'Bullying'?", "a": "Repeated, intentional behavior meant to hurt or intimidate someone."},
        {"q": "What is 'Cyberbullying'?", "a": "Bullying that happens online via social media or messaging."},

        # SET 4: Constitutional Rights and Responsibilities
        {"q": "What is the 'Bill of Rights'?", "a": "A chapter in the SA Constitution that protects human rights."},
        {"q": "Name one basic human right in South Africa.", "a": "Right to Life / Dignity / Education / Safety."},
        {"q": "What is the 'Right to Equality'?", "a": "Everyone must be treated fairly regardless of race, gender, or religion."},
        {"q": "If you have the 'Right to Education', what is your responsibility?", "a": "To attend school, study, and respect teachers."},
        {"q": "What is 'Democracy'?", "a": "A system where people choose their leaders through voting."},
        {"q": "What is the purpose of the 'Constitutional Court'?", "a": "To ensure that laws follow the Constitution."},
        {"q": "What is 'Discrimination'?", "a": "Treating someone unfairly because of who they are."},
        {"q": "What is 'Human Dignity'?", "a": "The belief that everyone has value and deserves respect."},
        {"q": "What is 'Freedom of Expression'?", "a": "The right to voice your opinions, as long as it isn't hate speech."},
        {"q": "Why are 'Rights' and 'Responsibilities' linked?", "a": "Because respecting others' rights is our responsibility."},

        # SET 5: Social and Environmental Responsibility
        {"q": "What is 'Social Justice'?", "a": "Fair treatment and a fair share of resources for everyone in society."},
        {"q": "What is a 'Community'?", "a": "A group of people living in the same area or sharing interests."},
        {"q": "What is 'Volunteering'?", "a": "Giving your time and skills to help others without being paid."},
        {"q": "What is 'Environmental Health'?", "a": "Protecting the planet so that people stay healthy."},
        {"q": "Name one way to care for the environment.", "a": "Recycling / Saving water / Not littering."},
        {"q": "What is 'Pollution'?", "a": "Damage caused to water, air, or land by harmful substances."},
        {"q": "What is 'Global Warming'?", "a": "The increase in the Earth's temperature due to greenhouse gases."},
        {"q": "What is 'Sustainable Living'?", "a": "Using resources in a way that doesn't run out for future generations."},
        {"q": "What is 'Civic Duty'?", "a": "The responsibility of a citizen to participate in their country."},
        {"q": "What is 'Social Activism'?", "a": "Taking action to bring about social or political change."},

        # SET 6: Health, Safety, and Nutrition
        {"q": "What is a 'Balanced Diet'?", "a": "Eating the right amounts of different food groups daily."},
        {"q": "Name the three main food groups.", "a": "Proteins, Carbohydrates, and Fats/Oils."},
        {"q": "Why is 'Physical Activity' important?", "a": "It keeps your heart, muscles, and mind healthy."},
        {"q": "What is 'Personal Hygiene'?", "a": "Keeping your body clean to prevent illness."},
        {"q": "What is an 'STI'?", "a": "A Sexually Transmitted Infection."},
        {"q": "What does 'HIV' stand for?", "a": "Human Immunodeficiency Virus."},
        {"q": "What does 'AIDS' stand for?", "a": "Acquired Immunodeficiency Syndrome."},
        {"q": "How can you prevent the spread of germs?", "a": "Wash your hands regularly with soap."},
        {"q": "What is 'Substance Abuse'?", "a": "The harmful use of drugs, alcohol, or cigarettes."},
        {"q": "What is 'Addiction'?", "a": "Being physically or mentally dependent on a substance."},

        # SET 7: Substance Abuse and Decision Making
        {"q": "What is 'Nicotine'?", "a": "The addictive substance found in cigarettes and vapes."},
        {"q": "Name a long-term effect of smoking.", "a": "Lung cancer / Heart disease / Shortness of breath."},
        {"q": "What is 'Alcoholism'?", "a": "A disease where a person cannot stop drinking alcohol."},
        {"q": "How does drug use affect school performance?", "a": "It leads to poor concentration and failing grades."},
        {"q": "What is 'Risk-taking Behavior'?", "a": "Doing things that could have dangerous consequences."},
        {"q": "What are 'Refusal Skills'?", "a": "Techniques used to say no to harmful behaviors."},
        {"q": "Name a 'Protective Factor' against drug use.", "a": "Strong family bonds / Positive hobbies / Self-confidence."},
        {"q": "What is a 'Rehabilitation Center'?", "a": "A place where people go to get help for addiction."},
        {"q": "What is the legal drinking age in South Africa?", "a": "18."},
        {"q": "Why is 'Vaping' dangerous for teens?", "a": "It contains chemicals that harm developing lungs and brains."},

        # SET 8: World of Work - Career Categories
        {"q": "What is a 'Career'?", "a": "A profession or occupation chosen as one's life's work."},
        {"q": "What are 'Interests'?", "a": "Things you enjoy doing."},
        {"q": "What are 'Aptitudes'?", "a": "Natural talents or things you are good at."},
        {"q": "What are the 6 Holland Career Categories?", "a": "Realistic, Investigative, Artistic, Social, Enterprising, Conventional."},
        {"q": "A person who likes working with machines belongs to which category?", "a": "Realistic."},
        {"q": "A person who loves science and research belongs to which category?", "a": "Investigative."},
        {"q": "A person who is creative and loves music/art belongs to which category?", "a": "Artistic."},
        {"q": "A person who likes helping and teaching others belongs to which category?", "a": "Social."},
        {"q": "A person who likes leading and business belongs to which category?", "a": "Enterprising."},
        {"q": "A person who likes organizing data and rules belongs to which category?", "a": "Conventional."},

        # SET 9: Learning Skills and Time Management
        {"q": "What is a 'Learning Style'?", "a": "The way a person learns best (Visual, Auditory, or Kinesthetic)."},
        {"q": "What is a 'Visual Learner'?", "a": "Someone who learns best by seeing pictures, charts, or reading."},
        {"q": "What is an 'Auditory Learner'?", "a": "Someone who learns best by listening and talking."},
        {"q": "What is a 'Kinesthetic Learner'?", "a": "Someone who learns best by doing or moving."},
        {"q": "What is 'Time Management'?", "a": "Planning how much time you spend on different activities."},
        {"q": "What is a 'Study Timetable'?", "a": "A schedule used to plan study sessions and breaks."},
        {"q": "What is 'Procrastination'?", "a": "Delaying or putting off tasks that need to be done."},
        {"q": "Name one 'Study Method'.", "a": "Mind-mapping / Flashcards / Summarizing / Quizzing."},
        {"q": "Why are 'Breaks' important during studying?", "a": "They help your brain rest and absorb information."},
        {"q": "What is 'Prioritization'?", "a": "Deciding which tasks are most important and doing them first."},

        # SET 10: Examination Writing Skills
        {"q": "What should you do first when you receive an exam paper?", "a": "Read the instructions carefully."},
        {"q": "Why is 'Mark Allocation' important?", "a": "It tells you how much detail you need to provide."},
        {"q": "What does the keyword 'Discuss' mean in an exam?", "a": "Examine a topic by looking at different sides or giving details."},
        {"q": "What does the keyword 'Identify' mean in an exam?", "a": "Simply name the fact or object required."},
        {"q": "What is 'Exam Stress'?", "a": "Feeling anxious or worried about an upcoming test."},
        {"q": "Name a way to reduce exam stress.", "a": "Start studying early / Get enough sleep / Exercise."},
        {"q": "What should you do if you finish your exam early?", "a": "Check your answers for mistakes or missing details."},
        {"q": "Why is it important to use a black or blue pen?", "a": "To ensure your answers are clear and easy to read."},
        {"q": "What is 'Plagiarism'?", "a": "Copying someone else's work and pretending it is your own."},
        {"q": "What is the best way to prepare for a multiple-choice question?", "a": "Read all options before choosing the best one."}
    ],
    "Technology": [
        # SET 1: The Design Process
        {"q": "What are the 5 stages of the Design Process?", "a": "Investigate, Design, Make, Evaluate, Communicate"},
        {"q": "What is a 'Design Brief'?", "a": "A short statement explaining the problem and what needs to be made"},
        {"q": "What are 'Specifications'?", "a": "Specific requirements the solution must meet (e.g. size, materials)"},
        {"q": "What are 'Constraints'?", "a": "Things that limit your design (e.g. budget, time, tools)"},
        {"q": "What is an 'Initial Sketch'?", "a": "A quick, rough drawing of a design idea"},
        {"q": "Why do we 'Evaluate' a product?", "a": "To see if it solves the problem and meets the specifications"},
        {"q": "What is 'Ergonomics'?", "a": "Designing products so they are comfortable and safe for humans to use"},
        {"q": "What is a 'Prototype'?", "a": "A first full-scale and functional version of a new design"},
        {"q": "What is 'Aesthetics'?", "a": "How a product looks (its visual beauty or style)"},
        {"q": "Why is 'Investigation' the first step?", "a": "To gather information and understand the problem before building"},

        # SET 2: Structures - Types and Forces
        {"q": "What is a 'Frame Structure'?", "a": "A structure made of connected parts forming a skeleton (e.g. a crane)"},
        {"q": "What is a 'Shell Structure'?", "a": "A structure that is strong because of its outer layer (e.g. an egg or helmet)"},
        {"q": "What is a 'Solid Structure'?", "a": "A structure made entirely of one piece of material (e.g. a brick or dam)"},
        {"q": "What is 'Compression'?", "a": "A force that squeezes or pushes a material together"},
        {"q": "What is 'Tension'?", "a": "A force that pulls or stretches a material apart"},
        {"q": "What is 'Torsion'?", "a": "A twisting force applied to an object"},
        {"q": "What is 'Shear Force'?", "a": "Opposing forces pushing in different directions (like scissors cutting)"},
        {"q": "What is 'Triangulation'?", "a": "Using triangle shapes to make a frame structure rigid and strong"},
        {"q": "What is a 'Tie' in a structure?", "a": "A member that resists pulling (tension)"},
        {"q": "What is a 'Strut' in a structure?", "a": "A member that resists squeezing (compression)"},

        # SET 3: Structural Stability and Failure
        {"q": "What is the 'Center of Gravity'?", "a": "The point where the weight of an object is balanced"},
        {"q": "How can you make a structure more 'Stable'?", "a": "Give it a wider base and a lower center of gravity"},
        {"q": "What is 'Structural Failure'?", "a": "When a structure breaks or loses its shape under a load"},
        {"q": "Define 'Fracture' in a structure.", "a": "When a material snaps or breaks apart completely"},
        {"q": "Define 'Bending' in a structure.", "a": "When a force causes a straight member to curve"},
        {"q": "What is 'Toppling'?", "a": "When a structure falls over because its center of gravity moves outside its base"},
        {"q": "What is 'Buckling'?", "a": "When a long, thin member fails by bending under compression"},
        {"q": "What is a 'Static Load'?", "a": "A load that does not move (e.g. the weight of a bridge itself)"},
        {"q": "What is a 'Dynamic Load'?", "a": "A moving load (e.g. cars driving across a bridge)"},
        {"q": "What is a 'Reinforced' material?", "a": "A material strengthened by adding another (e.g. steel in concrete)"},

        # SET 4: Mechanical Systems - Levers
        {"q": "What is a 'Lever'?", "a": "A simple machine consisting of a rigid bar turning on a pivot"},
        {"q": "What is the 'Fulcrum'?", "a": "The pivot point around which a lever turns"},
        {"q": "Where is the fulcrum in a First Class Lever?", "a": "In the middle (between the load and the effort)"},
        {"q": "Give an example of a First Class Lever.", "a": "A see-saw or a pair of scissors"},
        {"q": "Where is the load in a Second Class Lever?", "a": "In the middle (between the fulcrum and the effort)"},
        {"q": "Give an example of a Second Class Lever.", "a": "A wheelbarrow or a nutcracker"},
        {"q": "Where is the effort in a Third Class Lever?", "a": "In the middle (between the fulcrum and the load)"},
        {"q": "Give an example of a Third Class Lever.", "a": "A pair of tweezers or a human arm"},
        {"q": "What is 'Mechanical Advantage' (MA)?", "a": "The ratio of the output force to the input force"},
        {"q": "Formula for MA in a lever?", "a": "MA = Load ÷ Effort"},

        # SET 5: Mechanical Systems - Gears
        {"q": "What is a 'Spur Gear'?", "a": "A wheel with teeth around its edge used to transfer motion"},
        {"q": "What is the 'Driver Gear'?", "a": "The gear that receives the input power (starts the motion)"},
        {"q": "What is the 'Driven Gear'?", "a": "The gear that is moved by the driver gear (the output)"},
        {"q": "If a driver gear turns clockwise, which way does the driven gear turn?", "a": "Anti-clockwise (opposite direction)"},
        {"q": "What is an 'Idler Gear'?", "a": "A gear between the driver and driven gear to make them turn in the same direction"},
        {"q": "What is a 'Gear Train'?", "a": "Two or more gears meshed together"},
        {"q": "If a small gear drives a larger gear, does speed increase or decrease?", "a": "Decrease (but force increases)"},
        {"q": "What is 'Gearing Down'?", "a": "Using a small driver to turn a large driven gear for more force"},
        {"q": "What is 'Gearing Up'?", "a": "Using a large driver to turn a small driven gear for more speed"},
        {"q": "What is a 'Bevel Gear'?", "a": "Gears used to change the direction of motion by 90 degrees"},

        # SET 6: Mechanical Systems - Pulleys and Cams
        {"q": "What is a 'Pulley'?", "a": "A wheel with a groove for a rope used to lift loads"},
        {"q": "What is a 'Fixed Pulley'?", "a": "A pulley that stays in one place and only changes the direction of force"},
        {"q": "What is a 'Movable Pulley'?", "a": "A pulley that moves with the load and provides mechanical advantage"},
        {"q": "What is a 'Block and Tackle'?", "a": "A system of fixed and movable pulleys working together"},
        {"q": "What is a 'Cam'?", "a": "A shaped piece that turns to create a 'following' motion (up and down)"},
        {"q": "What is a 'Follower'?", "a": "The rod that rests on a cam and moves as the cam rotates"},
        {"q": "What is 'Reciprocating Motion'?", "a": "Back and forth or up and down motion in a straight line"},
        {"q": "What is 'Rotary Motion'?", "a": "Motion that goes in a circle (like a wheel)"},
        {"q": "What is 'Linear Motion'?", "a": "Motion in a straight line in one direction"},
        {"q": "What is 'Oscillating Motion'?", "a": "Swinging back and forth (like a pendulum)"},

        # SET 7: Electrical Systems - Basics
        {"q": "What is a 'Circuit'?", "a": "A complete, closed path through which electricity can flow"},
        {"q": "What is a 'Conductor'?", "a": "A material that allows electricity to flow through it easily (e.g. Copper)"},
        {"q": "What is an 'Insulator'?", "a": "A material that does not allow electricity to flow (e.g. Plastic)"},
        {"q": "What is a 'Switch' used for?", "a": "To open or close a circuit (turn it on or off)"},
        {"q": "What is a 'Series Circuit'?", "a": "A circuit where components are connected in a single path"},
        {"q": "What is a 'Parallel Circuit'?", "a": "A circuit with multiple paths for the electricity to flow"},
        {"q": "What happens if one bulb in a series circuit blows?", "a": "All the other bulbs will go out too"},
        {"q": "What is a 'Resistor'?", "a": "A component that resists the flow of current to protect parts from damage"},
        {"q": "What is an 'LDR' (Light Dependent Resistor)?", "a": "A resistor that changes its resistance based on light levels"},
        {"q": "What is a 'Diode'?", "a": "A component that only allows electricity to flow in one direction"},

        # SET 8: Processing Materials
        {"q": "What is 'Processing' in technology?", "a": "Changing a raw material to make it more useful"},
        {"q": "What is 'Curing'?", "a": "A chemical process used to toughen or harden materials (like rubber or concrete)"},
        {"q": "What is 'Preserving'?", "a": "Treating materials to stop them from rotting or rusting"},
        {"q": "Name one way to preserve wood.", "a": "Painting, varnishing, or using Creosote"},
        {"q": "What is 'Galvanising'?", "a": "Coating iron or steel with zinc to prevent rust"},
        {"q": "What is an 'Alloy'?", "a": "A mixture of two or more metals (e.g. Brass or Bronze)"},
        {"q": "What is 'Electroplating'?", "a": "Using electricity to coat one metal with a thin layer of another"},
        {"q": "Why do we 'Laminate' materials?", "a": "To make them stronger or more durable by gluing layers together"},
        {"q": "What is 'Recycling'?", "a": "Processing waste materials into new products to save resources"},
        {"q": "What is 'Biodegradable'?", "a": "Material that can be broken down naturally by bacteria"},

        # SET 9: Graphic Communication (Drawing)
        {"q": "What is an 'Isometric Drawing'?", "a": "A 3D drawing where lines are drawn at a 30-degree angle"},
        {"q": "What is an 'Oblique Drawing'?", "a": "A 3D drawing where the front is flat and sides go back at 45 degrees"},
        {"q": "What are 'Orthographic Projections'?", "a": "2D drawings showing the front, top, and side views of an object"},
        {"q": "What is a 'Scale Drawing'?", "a": "A drawing that is either larger or smaller than the real object, but in proportion"},
        {"q": "What does a 'Hidden Detail Line' look like?", "a": "A dashed or broken line (------)"},
        {"q": "What is a 'Dimension Line'?", "a": "A line with arrows showing the measurement of a part"},
        {"q": "What is 'Perspective Drawing'?", "a": "A drawing that uses vanishing points to make it look realistic"},
        {"q": "Why do we use 'Exploded Views'?", "a": "To show how different parts of an object fit together"},
        {"q": "What is a 'Sectional View'?", "a": "A drawing showing what the inside of an object looks like if it were cut open"},
        {"q": "What is 'CAD'?", "a": "Computer-Aided Design (using software to create technical drawings)"},

        # SET 10: Impact of Technology
        {"q": "What is 'Indigenous Technology'?", "a": "Traditional knowledge and tools used by local people for generations"},
        {"q": "Give an example of an indigenous structure in SA.", "a": "The Zulu beehive hut or the Ndebele house"},
        {"q": "What is 'Sustainable Technology'?", "a": "Tech that meets our needs without harming the environment or future"},
        {"q": "How can technology have a 'Negative Impact' on the environment?", "a": "Pollution, deforestation, and global warming"},
        {"q": "How can technology have a 'Positive Impact' on society?", "a": "Better healthcare, faster transport, and easier communication"},
        {"q": "What is 'Biotechnology'?", "a": "Using living organisms to make or modify products (like vaccines)"},
        {"q": "What is 'Automation'?", "a": "Using machines or robots to do work instead of humans"},
        {"q": "What is 'Ethics' in technology?", "a": "Considering whether a new invention is 'right' or 'wrong' for people"},
        {"q": "Why is it important to dispose of batteries correctly?", "a": "They contain toxic chemicals that can leak into the ground"},
        {"q": "What is 'Technological Literacy'?", "a": "Understanding how to use and evaluate technology in daily life"}
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
