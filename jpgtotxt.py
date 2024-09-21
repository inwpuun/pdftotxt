import pytesseract # type: ignore
from PIL import Image

def convert_jpg_to_txt(jpg_path):
    img = Image.open(jpg_path)
    custom_oem_psm_config = r'--dpi 2400'
    return pytesseract.image_to_string(img, lang='tha', config=custom_oem_psm_config)