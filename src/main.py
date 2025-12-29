# entry point

from pathlib import Path
from ocr.ocr_engine import extract_text

def main():
    print("PAN & Adhaar Reader Started")
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
    image_path = BASE_DIR / "data/samples/pan/pan1.jpg"
    print(image_path)
    text = extract_text(image_path)
    print("----RAW OCR OUTPUT----")
    print(text)

if __name__ == "__main__":
    main()