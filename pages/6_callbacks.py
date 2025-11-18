import streamlit as st

st.title("Lesson 6: Callbacks")
st.write("Run functions on widget changes. Used in GPA app to autofill course names on code change.")

st.subheader("Using on_change")
st.write("""
Attach a function to widgets like text_input.
Pass args if needed.
""")
st.code("""
def my_func(arg):
    st.write(f"Changed with {arg}")

st.text_input("Input", on_change=my_func, args=("demo",))
""")

def demo_autofill():
    if st.session_state.demo_code == "ABC":
        st.session_state.demo_name = "Auto-Filled Name"
    else:
        st.session_state.demo_name = ""

if 'demo_code' not in st.session_state:
    st.session_state.demo_code = ""
if 'demo_name' not in st.session_state:
    st.session_state.demo_name = ""

st.text_input("Enter code (try 'ABC')", key="demo_code", on_change=demo_autofill)
st.text_input("Name (autofills)", key="demo_name", disabled=True)
st.write(f"Name: {st.session_state.demo_name}")

st.write("""
Tips:
- Combine with session_state to update other widgets.
Alternatives:
- Use key and manual checks in the main script for simple cases.
- For complex logic, consider Streamlit's experimental features like fragments.
""")