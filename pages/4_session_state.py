import streamlit as st

st.title("Lesson 4: Session State")
st.write("Stores data across reruns. Critical in the GPA app for preserving inputs when changing subject count.")

st.subheader("Using st.session_state")
st.write("""
Like a dictionary. Set/get values with keys.
Used to store num_subjects, codes, names, etc.
""")
st.code("""
if 'count' not in st.session_state:
    st.session_state.count = 0
st.session_state.count += 1
st.write(st.session_state.count)
""")

if 'demo_count' not in st.session_state:
    st.session_state.demo_count = 0

if st.button("Increment Counter"):
    st.session_state.demo_count += 1

st.write(f"Counter value: {st.session_state.demo_count}")

if st.button("Reset Counter"):
    st.session_state.demo_count = 0

st.write("""
Tips:
- Check existence with 'key' in st.session_state.
- Delete keys with del st.session_state['key'] (as in GPA app).
Alternatives:
- For simple cases, use widget values directly.
- For complex apps, consider external storage like databases.
""")