import PyPDF2
import re

def extract_panel_info(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Define regex patterns for each field
    patterns = {
        'PANEL': r'PANEL:\s*(.+)',
        'VOLTAGE': r'VOLTAGE:\s*(.+)',
        'FEED': r'FEED:\s*(.+)',
        'CIRCUITS': r'CIRCUITS:\s*(.+)',
        'LOAD NAME': r'LOAD NAME:\s*(.+)',
        'TRIP': r'TRIP:\s*(.+)',
        'POLE': r'POLE:\s*(.+)',
        'EQUIPMENT REFERENCE': r'EQUIPMENT REFERENCE:\s*(.+)'
    }

    # Extract information
    extracted_info = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            extracted_info[key] = match.group(1)
        else:
            extracted_info[key] = "Not found"

    return extracted_info

if __name__ == "__main__":
    pdf_path = "path/to/your/pdf/file.pdf"  # Replace with your PDF file path
    info = extract_panel_info(pdf_path)
    
    for key, value in info.items():
        print(f"{key}: {value}")