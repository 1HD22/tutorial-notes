
import streamlit as st

st.title("Lesson 3: Forms and Buttons")
st.write("These handle submissions. The GPA app uses forms for subject count and buttons for calculation.")

st.subheader("1. st.form and st.form_submit_button")
st.write("""
Groups inputs; submits all at once. Prevents partial updates.
Used for the initial subjects form.
""")
st.code("""
with st.form("my_form"):
    num = st.number_input("Input")
    submit = st.form_submit_button("Submit")
if submit:
    st.write("Submitted!")
""")

with st.form("demo_form"):
    demo_input = st.text_input("Enter something")
    demo_submit = st.form_submit_button("Submit Form")
if demo_submit:
    st.write(f"Form submitted with: {demo_input}")

st.subheader("2. st.button")
st.write("""
Simple button for actions outside forms. Used for 'Calculate GPA'.""")
st.code('''
if st.button('Click me'):
    st.write('Clicked!')
''')
if st.button("Demo Button"):
    st.write("You clicked the button!")

st.write("""
Tips:
- Forms are great for batch submissions to avoid reruns.
Alternatives:
- st.checkbox or st.toggle for boolean triggers.
- Combine with session state (next lesson) for persistent actions.
""")