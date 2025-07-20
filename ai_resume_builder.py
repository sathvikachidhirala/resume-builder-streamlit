# ai_resume_builder.py

import streamlit as st
from datetime import datetime
from fpdf import FPDF
import random
import time  # For simulating API delay

# ----------- AI-enhanced sentence expansion -----------
def improve_point(point):
    templates = [
        f"Successfully led projects involving {point}.",

        f"Gained hands-on experience in {point} with notable outcomes.",
        f"Applied theoretical knowledge to practical scenarios in {point}.",
        f"Contributed effectively to tasks related to {point} in academic/industrial settings."
    ]
    return random.choice(templates)

# ----------- Mock Entelligence.ai API Simulation -----------
def analyze_with_entelligence(resume_text):
    # Simulate processing delay
    time.sleep(1)


    # Return fake but realistic AI feedback
    return {
        "suggestions": "Consider adding more technical keywords and quantifying your achievements.",
        "score": 78
    }

# ----------- PDF generator -----------
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Resume', ln=True, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# ----------- Streamlit UI -----------
st.title("AI Resume Builder for Tier-2/Tier-3 Students")
st.write("Fill in the form below to generate your professional resume:")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

st.subheader("Education")
edu = st.text_area("Education Details")

st.subheader("Experience")
exp_points = st.text_area("Briefly describe your work/experience")

st.subheader("Skills")
skills = st.text_input("List your key skills (comma separated)")

st.subheader("Achievements/Projects")
achievements = st.text_area("Mention any key achievements or projects")

# ----------- Resume Generation Button -----------
if st.button("Generate Resume"):
    # Combine all inputs into one text block
    resume_text = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}

    Education:
    {edu}

    Experience:
    {exp_points}

    Skills:
    {skills}

    Achievements/Projects:
    {achievements}
    """

    # Simulate Entelligence.ai feedback
    entelligence_feedback = analyze_with_entelligence(resume_text)

    # Display AI feedback on screen
    if entelligence_feedback:
        st.subheader("📌 AI Feedback from Entelligence.ai")
        st.write(entelligence_feedback.get("suggestions", "No suggestions returned."))
        st.write(f"Score: {entelligence_feedback.get('score', 'N/A')}")

    # Generate the PDF
    pdf = PDF()
    pdf.add_page()

    pdf.chapter_title("Name")
    pdf.chapter_body(name)

    pdf.chapter_title("Contact")
    pdf.chapter_body(f"Email: {email}\nPhone: {phone}")

    pdf.chapter_title("Education")
    pdf.chapter_body(edu)

    pdf.chapter_title("Experience")
    expanded_exp = improve_point(exp_points)
    pdf.chapter_body(expanded_exp)

    pdf.chapter_title("Skills")
    pdf.chapter_body(skills.replace(',', ', '))

    pdf.chapter_title("Achievements/Projects")
    pdf.chapter_body(achievements)

    # Include mock AI feedback in PDF
    if entelligence_feedback:
        pdf.chapter_title("AI Suggestions from Entelligence")
        pdf.chapter_body(entelligence_feedback.get("suggestions", "No suggestions provided."))

    # Save PDF
    file_name = f"Resume_{name.replace(' ', '_')}.pdf"
    pdf.output(file_name)

    with open(file_name, "rb") as f:
        st.download_button(
            label="Download Resume as PDF",
            data=f,
            file_name=file_name,
            mime="application/pdf"
        )
