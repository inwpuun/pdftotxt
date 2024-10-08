import pytesseract # type: ignore
from PIL import Image

def convert_jpg_to_txt(img):
    custom_oem_psm_config = r'--oem 1 --psm 6'
    return pytesseract.image_to_string(img, lang='tha', config=custom_oem_psm_config)