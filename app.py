import streamlit as st
from docx import Document
import datetime

def fill_form24(data, template_path='form_24_template.docx'):
    doc = Document(template_path)

    today = datetime.date.today()
    filled_date = today.strftime("%-d %B %Y")
    day = today.day
    month = today.strftime("%B")
    year = today.year

    replacements = {
        "LABUAN COMPANY NAME": data['company_name'],
        "CLIENT NAME": data['client_name'],
        "CLIENT ADDRESS": data['client_address'],
        "XXXXXXX": data['passport_number'],
        "_______ day of _______________, in the year of 2023": f"{day} day of {month}, in the year of {year}"
    }

    for paragraph in doc.paragraphs:
        for key, val in replacements.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, val)

    output_path = f"{data['client_name'].replace(' ', '_')}_Form24.docx"
    doc.save(output_path)
    return output_path

st.title("BBS Trust Ltd Form 24 Agent")

st.write("Fill in director details to generate a completed Form 24.")

# form inputs
with st.form("form24"):
    company_name = st.text_input("Labuan Company Name")
    client_name = st.text_input("Director's Name")
    client_address = st.text_area("Director's Address")
    passport_number = st.text_input("NRIC/Passport/Company No.")
    submitted = st.form_submit_button("Generate Form 24")

# generate docx and provide download button
if submitted:
    filled_file = fill_form24({
        "company_name": company_name,
        "client_name": client_name,
        "client_address": client_address,
        "passport_number": passport_number
    })
    with open(filled_file, "rb") as f:
        st.download_button(
            label="📄 Download Filled Form 24",
            data=f,
            file_name=filled_file,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

