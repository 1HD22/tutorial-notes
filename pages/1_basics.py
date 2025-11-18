import streamlit as st

st.title("Lesson 1: Basics - Configuration, Titles, and Text")
st.write("These elements set up the app's look and display simple content. They're used in the GPA app for the title and instructions.")

st.subheader("1. st.set_page_config")
st.write("""
Configures the page title, layout, etc. Call it once at the top.
Example: Sets the browser tab title.
""")
st.code("""
import streamlit as st
st.set_page_config(page_title="My App")
""")
st.write("Demo: This page's title is set via this.")

st.subheader("2. st.title")
st.write("Displays a large heading. Used for the main 'GPA Calculator' title.")
st.code("""
st.title("My Title")
""")
st.title("Live Demo Title")

st.subheader("3. st.write")
st.write("Displays text, variables, or markdown. Versatile for instructions or results.")
st.code("""
st.write("Hello, world!")
st.write(f"Calculated value: {3.14}")
""")
demo_text = "This is a demo using st.write."
st.write(demo_text)

st.subheader("4. st.subheader")
st.write("Smaller heading for sections, like 'Course 1' in the GPA app.")
st.code("""
st.subheader("Section Header")
""")
st.subheader("Live Demo Subheader")

st.write("""
Tips:
- Use markdown in st.write for formatting: **bold**, *italic*.
Alternatives:
- st.markdown for raw markdown if you need more control.
- st.header for mid-level headings between title and subheader.
""")