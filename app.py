import streamlit as st

st.set_page_config(page_title="AI Resume Builder")

st.title("AI Resume & Portfolio Builder")

name = st.text_input("Full Name")

education = st.selectbox(
    "Education",
    ["BBA","BCA","BTech","MBA","BCom"]
)

skills = st.number_input(
    "Skills Count",
    min_value=0,
    max_value=20
)

projects = st.number_input(
    "Projects Count",
    min_value=0,
    max_value=20
)

certs = st.number_input(
    "Certificates",
    min_value=0,
    max_value=20
)

exp = st.number_input(
    "Experience Years",
    min_value=0,
    max_value=20
)

# PASTE THE CODE HERE
if st.button("Generate Resume"):

    st.success("Generating...")

    level = "Intermediate"

    st.success(
        f"Candidate Level: {level}"
    )

    resume_text = f"""
    Name: {name}

    Education: {education}

    Skills Count: {skills}

    Projects Count: {projects}

    Certifications: {certs}

    Experience: {exp} years
    """

    st.subheader("Resume")

    st.write(resume_text)

    st.subheader("Cover Letter")

    st.write(
        f"Dear Hiring Manager, I am {name}..."
    )

    st.subheader("Portfolio Summary")

    st.write(
        f"{name} has completed {projects} projects."
    )

    st.download_button(
        "Download Resume",
        resume_text,
        file_name="resume.txt"
    )