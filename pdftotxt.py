# Importing required modules
from pypdf import PdfReader
import re
from noisy import is_noisy_line

# Creating a PDF reader object
reader = PdfReader('test2.pdf')

# Printing number of pages in the PDF file
print(f'Number of pages in the PDF: {len(reader.pages)}')

# Opening a file to write the extracted text
with open('ocr-output.txt', 'w', encoding='utf-8') as file:
    # Looping through all pages in the PDF
    for page_number in range(len(reader.pages)):
        # Getting a specific page from the PDF file
        page = reader.pages[page_number]
        
        # Extracting text from the page
        text = page.extract_text()
        
        # Checking if text extraction was successful
        if text:  # Only write if text is not None
            text = text.replace(' า', 'ำ')
            text = text.replace('  ', ' ')
            text = text.replace(' ้หนา', 'หน้า')
            text = text.replace('่เลม', 'เล่ม')
            print(text)
            if is_noisy_line(text):
                print(f"Noisy text found on page {page_number + 1}")
                continue
            file.write(text + '\n')  # Write text and add a newline
        else:
            print(f"No text found on page {page_number + 1}")

print("Text extraction completed. Check 'ocr-output.txt' for the output.")