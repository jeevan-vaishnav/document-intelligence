# image path 
# output raw
# noparsing logic here

# import bring libary
# def extrat_text -> function 
# image_path:str -> type hint (optional, just for clarity)
# Image.open() -< load image 
# image_to_string() -> OCR
#  return text -> give result back

import pytesseract
from PIL import Image

def extract_text(image_path:str) -> str:
    """
    Takes image path and returns raw OCR text
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text




