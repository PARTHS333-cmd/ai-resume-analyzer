import pdfplumber
import os

# Input PDF path
PDF_PATH = "data/resumes/resume.pdf"

# Output extracted text path
OUTPUT_PATH = "data/extracted/extracted_resume.txt"


def extract_text_from_pdf(pdf_path):
    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()

            if text:
                extracted_text += f"\n--- Page {page_number} ---\n"
                extracted_text += text

    return extracted_text


def save_extracted_text(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


if __name__ == "__main__":
    print("Starting resume extraction...")

    extracted_text = extract_text_from_pdf(PDF_PATH)

    save_extracted_text(extracted_text, OUTPUT_PATH)

    print("Resume text extracted successfully!")
    print(f"Saved to: {OUTPUT_PATH}")