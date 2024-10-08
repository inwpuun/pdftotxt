import re

def is_noisy_line(line):
    # Define patterns that identify noisy lines
    # - Lines with too many symbols
    # - Lines that are very short or fragmented
    # - Lines with mixed numbers and special characters
    noise_patterns = [
        # r'^หน้า',
        # r'^เล่ม',
        r'^[0-9]',
        # r'[0-9]+', # lines with arabic numbers
        # r'\s{2,}',
        # r'^.{1,2}$',  # lines that are too short (less than 3 characters)
        # r'ซ่=|ซ่\||..|= =|«\|',
        # r'ณฒณ|จฮ่|บญ์|บูญ|” ญู',  # specific patterns of noise in the text
    ]
    
    # Check for any noisy pattern
    for pattern in noise_patterns:
        if re.search(pattern, line):
            return True
    return False

def clean_text_by_line(text):
    # Split text into lines
    lines = text.split('\n')
    
    # List to hold cleaned lines
    cleaned_lines = []
    
    for line in lines:
        # Remove extra whitespace from the line
        line = line.strip()
        
        # Skip noisy lines and keep only valid ones
        if is_noisy_line(line):
            if "สรุปราคาประเมิน" in line:
               line = line[0:line.index("สรุปราคาประเมิน")]
            cleaned_lines.append(line)
    
    # Join the cleaned lines back into a single text block
    cleaned_text = '\n'.join(cleaned_lines)
    
    return cleaned_text

with open('ocr-output.txt', 'r') as file:
    text = file.read()

# text = """
# 423ซอยรัชดาภิเษก70 53,000
# 424ซอยรัชดาภิเษก72 53,000
# 425ซอยรัชดาภิเษก74 53,000
# ล ำดับที่ ชื่อหน่วยที่ดินรำคำประเมิน
# (บำท/ตำรำงวำ)
# 426ซอยรัชดาภิเษก76 53,000
# 427ซอยรัชดาภิเษก78 53,000
# 428ซอยลาดพร้าว35แยก10 53,000
# 429ซอยลาดพร้าว35แยก2-1 53,000"""

cleaned_text = clean_text_by_line(text)

with open('cleaned-ocr-output.txt', 'w') as file:
    file.write(cleaned_text)
# print(clean_text_by_line(text))