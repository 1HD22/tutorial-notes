import streamlit as st

st.title("Lesson 2: Inputs - Text, Numbers, and Selections")
st.write("These gather user data. In the GPA app, they're used for course codes, names, grades, and credits.")

st.subheader("1. st.text_input")
st.write("""
For string input. Supports keys for state and on_change callbacks (covered later).
Used for course code and name.
""")
st.code("""
name = st.text_input("Enter name", key="my_key")
""")
demo_code = st.text_input("Enter a course code")
st.write(f"You entered: {demo_code}")

st.subheader("2. st.number_input")
st.write("""
For numeric input with min/max/step. Used for subjects count and credits.
""")
st.code("""
num = st.number_input("Enter number", min_value=1, max_value=10, step=1)
""")
demo_num = st.number_input("How many courses?", min_value=1, max_value=5, step=1)
st.write(f"You selected: {demo_num}")

st.subheader("3. st.selectbox")
st.write("""
Dropdown for choices. Used for grades.
""")
st.code("""
option = st.selectbox("Choose", ["A", "B", "C"])
""")
grades = ['A+', 'A', 'A-']
demo_grade = st.selectbox("Select grade", grades)
st.write(f"You chose: {demo_grade}")

st.write("""
Tips:
- Add placeholders with value="".
Alternatives:
- st.multiselect for multiple choices.
- st.slider for range-based numbers instead of number_input.
- st.radio for button-style selections.
""")