# entry point
# OCR engine 
from pathlib import Path
from ocr.ocr_engine import extract_text
# Text normalizer 
from utils.text_normalizer import normalize_text


def main():
    print("PAN & Adhaar Reader Started")
    # access the root path 
    BASE_DIR = Path(__file__).resolve().parent.parent
    # access the file path 
    image_path = BASE_DIR / "data/samples/pan/pan1.jpg"
    # priting the path 
    print(image_path)
    # calling the function to get the details of pan 
    raw_text = extract_text(image_path)
    print("----RAW OCR OUTPUT----")
    # clean text 
    clean_text = normalize_text(raw_text)
    print(clean_text)
      
if __name__ == "__main__":
    main()


# notes!
# Important things :
# OCR gives raw data 
# Normalizer makes it usable 
# We never extract fields from raw OCR