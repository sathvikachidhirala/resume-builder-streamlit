# Resume Builder (Streamlit)

A simple Python-based web application that helps students create professional resumes and download them as PDF files.

## Features

- **User-Friendly Interface:** Enter personal details, contact information, education, experience, skills, and achievements through a Streamlit interface.
- **PDF Resume Generation:** Automatically generates a downloadable PDF resume using the information provided by the user.
- **Experience Wording Suggestions:** Provides template-based sentence suggestions to help improve the presentation of experience details.
- **Resume Feedback:** Displays predefined resume suggestions and a sample score to demonstrate a basic feedback feature.
- **Input Validation:** Checks that the user's name is provided before generating a resume.
- **Safe PDF Text Handling:** Handles characters unsupported by the default PDF font to reduce encoding errors.

## Technologies Used

- **Python** – Application logic
- **Streamlit** – Web interface
- **FPDF** – PDF generation
- **Random module** – Selection of predefined sentence templates

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/sathvikachidhirala/resume-builder-streamlit.git
   ```

2. Navigate to the project directory:

   ```bash
   cd resume-builder-streamlit
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run ai_resume_builder.py
   ```

5. Open the local URL displayed in your terminal to use the application.

## How to Use

1. Enter your name and contact information.
2. Add your education and experience details.
3. Enter your skills and achievements or projects.
4. Click **Generate Resume**.
5. Review the displayed feedback and download your PDF resume.

## Future Improvements

- Integrate a real AI service to generate personalized resume feedback.
- Add multiple resume templates and customization options.
- Improve PDF formatting and Unicode character support.
- Add downloadable resume previews and stronger input validation.

## Project Purpose

This project demonstrates the development of a Python web application that collects user input, generates structured PDF documents, and provides basic template-based resume assistance.

