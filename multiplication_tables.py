import streamlit as st
from dataclasses import dataclass
import random

st.title("Oefen je maaltafels!")
choose = "Kies de maaltafels die je wilt oefenen"
st.write(choose)

tables = st.multiselect(
    choose,
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    placeholder="Selecteer een of meerdere maaltafels",
    label_visibility="collapsed",
)


@dataclass
class MultiplicationTable:
    table: str
    question: str
    answer: int


# Initialize the multiplication tables
multiplication_tables = []

for table in tables:
    for i in range(1, 11):
        multiplication_tables.append(MultiplicationTable(table, f"{table} x {i} =", int(table) * i))

# Shuffle the list of multiplication tables
random.shuffle(multiplication_tables)

# Initialize session state variables
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.right_answers = []
    st.session_state.wrong_answers = []


# Define the callback function
def check_answer():
    current_table = multiplication_tables[st.session_state.current_question]
    response = st.session_state.response
    if response == current_table.answer:
        st.session_state.right_answers.append(current_table)
    else:
        st.session_state.wrong_answers.append(current_table)
    
    st.session_state.current_question += 1
    st.session_state.response = None  # Reset the input field
    

st.write("")

# Display the current question
if st.session_state.current_question < len(multiplication_tables):
    current_table = multiplication_tables[st.session_state.current_question]
    st.write(current_table.question)
    st.number_input(
	    current_table.question,
	    label_visibility="collapsed",
	    key='response', 
	    placeholder="Vul je antwoord hier in en druk op Enter",
	    step=1,
	    value=None,
        on_change=check_answer,  # Set the callback function
    )

# JavaScript to set focus on the input element (not working)
    st.markdown(
        """
        <script>
        document.getElementById('response').focus();
        });
        </script>
        """,
        unsafe_allow_html=True
    )
elif st.session_state.current_question > 0:
    st.write("")
    st.write(f"Je hebt {len(st.session_state.right_answers)} van de {len(multiplication_tables)} goed!")
    
# Concatenate all the wrongly answered questions into a single string
    wrong_questions = ", ".join([qa.question for qa in st.session_state.wrong_answers])
    st.write(f"Fout beantwoorde vragen: {wrong_questions}")

    if st.button("Opnieuw beginnen"):
        st.session_state.current_question = 0
        st.session_state.right_answers = []
        st.session_state.wrong_answers = []