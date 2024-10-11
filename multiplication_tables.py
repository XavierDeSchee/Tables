import streamlit as st
from functions import generate_random_tables

title = ":bulb: Oefen je maaltafels!"
st.title(title)

st.write("")

choose = ":pencil: Kies de maaltafels die je wilt oefenen"
st.write(choose)

tables = st.multiselect(
    choose,
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    placeholder="Selecteer een of meerdere maaltafels",
    label_visibility="collapsed",
)

# Initialize session state variables
if 'question_number' not in st.session_state:
    st.session_state.question_number = 0
    st.session_state.right_answers = []
    st.session_state.wrong_answers = []

# Initialize and shuffle multiplication tables if not already done
if (
    'multiplication_tables' not in st.session_state or  # first pass through the script
    st.session_state.multiplication_tables == [] or  # no user input yet
    tables != st.session_state.tables  # new user input
):
    st.session_state.multiplication_tables = generate_random_tables(tables)
    st.session_state.tables = tables


# Define the callback function
def check_answer():
    current_table = st.session_state.multiplication_tables[st.session_state.question_number]
    response = st.session_state.response
    if response == current_table.answer:
        st.session_state.right_answers.append(current_table)
    else:
        st.session_state.wrong_answers.append(current_table)
    
    st.session_state.question_number += 1
    st.session_state.response = None  # Reset the input field
    

st.write("")

# Display the current question
if st.session_state.multiplication_tables is not None and st.session_state.question_number < len(st.session_state.multiplication_tables):
    current_table = st.session_state.multiplication_tables[st.session_state.question_number]
    st.write(current_table.question)
    st.number_input(
	    current_table.question,
	    label_visibility="collapsed",
	    key='response', 
	    placeholder="Vul je antwoord hier in en druk op Enter",
	    step=1,
	    value=None,
        on_change=check_answer,  # Set the callback function to verify answer and increment question number
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

# Display the final score
elif st.session_state.question_number > 0:
    if (len(st.session_state.right_answers) == len(st.session_state.multiplication_tables)):
        st.write("Je hebt alle vragen juist beantwoord! :trophy: :trophy: :trophy:")
    else:
        st.write(f"Je hebt {len(st.session_state.right_answers)} :star: van de {len(st.session_state.multiplication_tables)} goed!")
        wrong_questions = ", ".join([qa.question for qa in st.session_state.wrong_answers])
        st.write(f"Fout beantwoorde vragen :x: : {wrong_questions}")

    st.write("")

    if st.button(":repeat: Opnieuw beginnen"):
        st.session_state.question_number = 0
        st.session_state.right_answers = []
        st.session_state.wrong_answers = []
        st.session_state.multiplication_tables = []