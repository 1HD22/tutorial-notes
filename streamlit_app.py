import streamlit as st

st.set_page_config(page_title="GPA Calculator — Streamlit Element Exercises")

# ---------------------------------------------------------------
# Exercise Sheet Header
# ---------------------------------------------------------------
st.title("GPA Calculator — Streamlit Elements Exercise Sheet")

st.write("""
Welcome! This exercise sheet guides you step-by-step through recreating key 
Streamlit elements used in the GPA Calculator application. 

Follow each task carefully.  
For every task, you will see:
- A description of what you must implement  
- Space for inserting example screenshots later  
- References to the skeleton code where your implementation must go  
""")

st.subheader("How to Use This Sheet")
st.write("""
Work through Tasks 1 → 3 in order.  
Each task builds on the previous one.  
Replace the **Write your code here** sections in the skeleton with your own solutions.
""")

# =====================================================================
# TASK 1 — PAGE SETUP
# =====================================================================
st.header("Task 1 — Page Setup")

st.subheader("1.1 Configure the Page")
st.write("""
Use `st.set_page_config` to:
- Give your page a title  
- Optionally add an icon  
- Make the layout wide if you prefer  

This corresponds to **Task 1.1** in the skeleton.

**What you must do:**  
- Add a `st.set_page_config(...)` line at the top of your script before anything else.
""")

st.image("images/header.png")

st.subheader("1.2 Add a Main Title and Description")
st.write("""
Use:
- `st.title` for the page's main title  
- `st.write` to provide an introduction or caption  

This corresponds to **Task 1.2**.

**What you must do:**  
- Create your own title  
- Add 2–3 lines explaining the purpose of the page  
""")

st.image("images/title.png")


# =====================================================================
# TASK 2 — FORMS & INPUT ELEMENTS
# =====================================================================
st.header("Task 2 — Forms and Input Fields")

st.subheader("2.1 Create the Course Count Form")
st.write("""
You must create a form that asks the user:

**“How many courses have you taken?”**

Inside the form:
- Use `st.number_input`  
- Save the result in variable `num_subjects`  
- Add a submit button named `submit_subjects`  

This corresponds to **Task 2.1**.

**What you must do:**  
- Use the `with st.form(...):` syntax  
- Name variables **exactly** as required  
""")

st.image("images/forms.png")


st.subheader("2.2 Create Inputs for Each Course")
st.write("""
After the user submits the number of subjects, dynamically create 
input sections for each course.

For each course *i*, create:
- A subheader  
- A `st.text_input` for course code (with `on_change=autofill_name`)  
- A `st.text_input` for course name  
- A `st.selectbox` for grade (use `grade_to_points.keys()`)  
- A `st.number_input` for credit value  

This corresponds to **Task 2.2**.

**Important:**  
- Use `args=(i,)` so the autofill function knows which item to update  
""")

st.image("images/course.png")


st.subheader("2.3 Add the GPA Calculation Button")
st.write("""
At the bottom of all course input fields, add a button that will trigger 
the GPA calculation.

This corresponds to **Task 2.3**.

**What you must do:**  
- Create a variable `submit_grades = st.button("...")`  
""")

st.text("images/calculate.png")


# =====================================================================
# TASK 3 — GPA CALCULATION
# =====================================================================
st.header("Task 3 — GPA Calculation")

st.subheader("3.1 Compute Total Points and Credits")
st.write("""
When the user presses the GPA button:

Loop through the session state values for each course and compute:
- `total_points`  
- `total_credits`  

This corresponds to **Task 3.1**.

**What you must do:**  
- Multiply each grade's point value by its credit value  
- Add to cumulative totals  
""")


st.subheader("3.2 Compute the GPA and Display It")
st.write("""
Now compute:


Then display it using `st.write`, `st.success`, etc.

This corresponds to **Task 3.2**.
""")

st.image("images/gpa.png")


st.subheader("3.3 Show Conditional Messages")
st.write("""
Add messages that change depending on the GPA.

Example already provided:
- If GPA ≥ 3.7 → `st.success("Excellent performance!")`  

This corresponds to **Task 3.3**.

**What you must do:**  
- Add at least 3 categories (e.g., excellent / good / needs improvement)
""")

st.image("images/result.png")


# =====================================================================
# END
# =====================================================================
st.write("---")
st.write("You're ready to fill in the code skeleton now! Follow each task carefully and test frequently.")
