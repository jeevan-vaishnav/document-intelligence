# uppercase 
# Fix OCR mistakes (o-0m i-1)
# removal extra space 

def normalize_text(text:str) -> str:
    """
    Cleans OCR Text
    """
    text = text.upper()
    text = text.replace("\n\n","\n")
    text= text.strip()

    return text

