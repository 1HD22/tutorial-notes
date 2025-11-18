import streamlit as st

st.title("Lesson 5: Feedback Messages")
st.write("Display styled alerts. Used in GPA app for results like 'Excellent performance!' or errors.")

st.subheader("1. st.success")
st.write("Green success message.")
st.code("st.success('Well done!')")
st.success("Demo success message.")

st.subheader("2. st.warning")
st.write("Yellow warning.")
st.code("st.warning('Be careful.')")
st.warning("Demo warning message.")

st.subheader("3. st.error")
st.write("Red error.")
st.code("st.error('Something went wrong.')")
st.error("Demo error message.")

st.write("""
Tips:
- Use for conditional feedback based on calculations.
Alternatives:
- st.info for blue informational notes.
- Custom HTML via st.markdown for more styling.
""")

demo_gpa = st.number_input("Enter a GPA to simulate", min_value=0.0, max_value=4.3, step=0.1)
if st.button("Show Feedback"):
    if demo_gpa >= 3.7:
        st.success("Excellent!")
    elif demo_gpa >= 3.0:
        st.success("Good job!")
    elif demo_gpa >= 2.0:
        st.warning("Room for improvement.")
    else:
        st.error("Below 2.0.")